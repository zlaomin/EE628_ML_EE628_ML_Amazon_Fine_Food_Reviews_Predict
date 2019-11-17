import sqlite3
import constant
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
from scipy.optimize import leastsq
from scipy import stats


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
def graphic(cursor, product_ids):
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
        x_ticks = time[::5]
        plt.xticks(x[::5], x_ticks)
        value = par[0] * pow(x, 3) + par[1] * pow(x, 2) + par[2] * x + par[3]
        # plt.plot(x, value, '-r', label='line')
        plt.plot(x, value, color="blue", linewidth=1.5)
        value = par[0] * pow(x, 3) + par[1] * pow(x, 2) + par[2] * x + par[3]
        p0 = [1, 1, 1, 1, 1]
        par, i = leastsq(err_4, p0, args=(x, y))
        value = par[0] * pow(x, 4) + par[1] * pow(x, 3) + par[2] * pow(x, 2) + par[3] * x + par[4]
        plt.plot(x, value, color="red", linewidth=1.5)
        plt.scatter(x, y, c='r', marker='o')
        plt.savefig("/images/" + p_id + ".png")


if __name__ == "__main__":
    conn = sqlite3.connect('database.sqlite')
    command = conn.cursor()
    graphic(command, constant.top_product_id)
    conn.close()
    print("Opened database successfully")
