import sqlite3
import constant
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
from scipy import stats


def graphic(cursor, productid_ids):
    for p_id in productid_ids:
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
        line = stats.linregress(x, y)
        x_ticks = time[::5]
        plt.xticks(x[::5], x_ticks)
        value = x * line.slope + line.intercept
        plt.plot(x, value, '-r', label='line')
        plt.scatter(x, y, c='r', marker='o')
        plt.show()


if __name__ == "__main__":
    conn = sqlite3.connect('database.sqlite')
    command = conn.cursor()
    graphic(command, constant.top_product_id)
    conn.close()
    print("Opened database successfully")
