import math
import sqlite3
import sys

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.optimize import leastsq
from sklearn import neighbors
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import normalize

import constant
import error_raw_data
import error_stopwords


def cal(p, x):
    res = 0;
    for i in range(len(p)):
        res += pow(p[-i-1], i)
    return res


def fun_3(p, x):
    a, b, c, d = p    # 从参数p获得拟合的参数
    return a * pow(x, 3) + b * pow(x, 2) + c * x + d


def err_3(p, x, y):
    return fun_3(p, x) - y


def fun_4(p, x):
    e, a, b, c, d = p    # 从参数p获得拟合的参数
    return e * pow(x, 4) + a * pow(x, 3) + b * pow(x, 2) + c * x + d


def err_4(p, x, y):
    return fun_4(p, x) - y


# get a list of string(product_id). Result is a graphic
def regression(cursor, product_ids):
    for p_id in product_ids:
        products = cursor.execute(
            "SELECT Time, Score FROM reviews Where Productid={Productid}".format(Productid="'"+p_id+"'")
            ).fetchall()
        df_products = pd.DataFrame(products)
        df_products.columns = ['Time', 'Score']
        df_products['Time'] = pd.to_datetime(df_products['Time'], unit='s')
        df_products = df_products.set_index('Time')
        # daily = df_products.groupby('Time')
        group_by_describe = df_products.groupby(pd.Grouper(freq='QS-DEC')).describe()
        season = group_by_describe[('Score', 'mean')]
        season = season.reset_index()
        score = list(season.Score['mean'])
        time = (list(season.Time))

        time_list = []
        score_list = []
        for i,j in zip(time, score):
            if not math.isnan(j):
                score_list.append(j)
                time_list.append(i.timestamp())
        y = np.array(score_list)
        x = np.array(time_list)
        # line = stats.linregress(x, y)
        p0 = [1, 1, 1, 1]
        par, i = leastsq(err_3, p0, args=(x, y))
        # combine 5 'time' into 1 x_ticks
        time = time[::4]
        x_ticks = []
        plt.clf()
        plt.cla()
        for i in time:
            x_ticks.append(i.to_period('M').strftime('%F-Q%q'))
        plt.xticks(x[::4], x_ticks)
        # draw
        value = par[0] * pow(x, 3) + par[1] * pow(x, 2) + par[2] * x + par[3]
        # plt.plot(x, value, '-r', label='line')
        plt.plot(x, value, color="blue", linewidth=1.5)
        value = par[0] * pow(x, 3) + par[1] * pow(x, 2) + par[2] * x + par[3]
        p0 = [1, 1, 1, 1, 1]
        par, i = leastsq(err_4, p0, args=(x, y))
        value = par[0] * pow(x, 4) + par[1] * pow(x, 3) + par[2] * pow(x, 2) + par[3] * x + par[4]
        plt.plot(x, value, color="red", linewidth=1.5)
        plt.scatter(x, y, c='r', marker='o')
        plt.savefig("images/" + p_id + ".png")


def data_ana(cursor, product_ids):
    words = {}
    with open('X_test.txt', 'rt') as f:
        data = f.read()
        products_reviews = data.split("\n")
        for comment in products_reviews:
            for stop_word in constant.ori_stopwords:
                occur = comment.count(stop_word)
                if occur > 0:
                    if stop_word in words:
                        words[stop_word] += occur
                    else:
                        words[stop_word] = occur
    print(words)
    error_stop_words = {}
    for comment in error_raw_data.error_raw_data:
        for stop_word in constant.ori_stopwords:
            occur = comment.count(stop_word)
            if occur > 0:
                if stop_word in error_stop_words:
                    error_stop_words[stop_word] += occur
                else:
                    error_stop_words[stop_word] = occur
    print(error_stop_words)


def find_stopwords(cursor, product_ids):
    res = {}
    for key in error_stopwords.stopwords.keys():
        num_in_error = error_stopwords.error_stopwords.get(key, 0)
        res[key] = num_in_error / error_stopwords.stopwords[key]
    order = sorted(res.items(), key=lambda item:item[1], reverse = True)
    print(order)
    # print(order[-10:])
    # for i in order:
    #     print("key: " + i + "res: " + str(
    #         res[i]
    #     ))
    # print(order)


def k_means(cursor, product_ids):
    train = []
    label = []
    for p_id in constant.top_product_id:
        products_review = cursor.execute(
            # "SELECT Text, Score FROM reviews Where Productid={Productid}".format(Productid="'"+p_id+"'")
            "SELECT Text, Score FROM reviews"
        ).fetchall()
        pd_products_review = pd.DataFrame(products_review)
        t_list = pd_products_review[0].tolist()
        train += t_list
        label = pd_products_review[1].tolist()
        label += label
    tf_idf_vectorizor = TfidfVectorizer(stop_words='english',#tokenizer = tokenize_and_stem,
                                        max_features=20000)
    tf_idf = tf_idf_vectorizor.fit_transform(train)
    tf_idf_norm = normalize(tf_idf)
    tf_idf_array = tf_idf_norm.toarray()
    sklearn_pca = PCA(n_components = 2)
    Y_sklearn = sklearn_pca.fit_transform(tf_idf_array)

    km = KMeans(n_clusters=5, init='k-means++', max_iter=300, n_init=1,
                verbose=False)
    fitted = km.fit(Y_sklearn)
    prediction = km.predict(Y_sklearn)
    test = 0
    for p_id in constant.test:
        products_review = cursor.execute(
            "SELECT Text, Score FROM reviews Where Productid={Productid}".format(Productid="'"+p_id+"'")
        ).fetchall()
        test += len(products_review)


def knn(cursor, product_ids):
    train = []
    label = []
    for p_id in constant.top_product_id:
        products_review = cursor.execute(
            "SELECT Text, Score FROM reviews Where Productid={Productid}".format(Productid="'"+p_id+"'")
            # "SELECT Text, Score FROM reviews"
        ).fetchall()
        pd_products_review = pd.DataFrame(products_review)
        t_list = pd_products_review[0].tolist()
        train += t_list
        t_label = pd_products_review[1].tolist()
        label += t_label
    # tf_idf_vectorizor = TfidfVectorizer(stop_words='english',#tokenizer = tokenize_and_stem,
    #                                     max_features=20000)
    tf_idf_vectorizor = TfidfVectorizer(max_features=20000, stop_words=constant.stopwords)
    tf_idf = tf_idf_vectorizor.fit_transform(train)
    tf_idf_norm = normalize(tf_idf)
    tf_idf_array = tf_idf_norm.toarray()
    sklearn_pca = PCA(n_components = 1)
    Y_sklearn = sklearn_pca.fit_transform(tf_idf_array)
    x_train, x_test, y_train, y_test = train_test_split(Y_sklearn, label, test_size = 0.2)
    clf = neighbors.KNeighborsClassifier(algorithm='kd_tree')
    clf.fit(x_train, y_train)
    # precision, recall, thresholds = precision_recall_curve(y_test, clf.predict(x_test))
    y_predict = clf.predict(x_test)
    res = 0
    for i in range(len(y_predict)):
        if y_predict[i] == y_test[i]:
            res += 1
    precision = res/len(y_predict)
    print("precision", precision)


if __name__ == "__main__":
    conn = sqlite3.connect('database.sqlite')
    command = conn.cursor()
    if len(sys.argv) > 2:
        cmd = sys.argv[1]
        op = sys.argv[2]
        if op == "test":
            data = constant.test
        else:
            data = constant.train
    else:
        cmd = sys.argv[1]
        data = constant.top_product_id
    try:
        globals()[cmd](command, data)
    except Exception as e:
        print("You must input regression, data_ana or k_means")
        raise(e)
    conn.close()
    print("Opened database successfully")
