from redis_command import Redis_Command
from mongo_command import Mongo_Command

import datetime
import pandas as pd
import numpy as np
import pymongo
from pymongo import MongoClient

rds = Redis_Command()
mng = Mongo_Command()

class Sweeper:
    """
    Redisに保存した検知情報をすべて取得し、分解してリストにしていく。
    """
    def __init__(self) -> None:
        self.streamkey = rds.commonkey_get()
        print(rds.commonkey_get())
        pass

    def sweeper(self):
        self.all_date = rds.r.xrange(self.streamkey,"-","+")
        return self.all_date

if __name__ == "__main__":
    swep = Sweeper()
    all = swep.sweeper()
    index = []
    columns_list = ["special","special_value"] # ここのリストは都度増えるように変えないとだめ
    column_1 = [] 
    value_1 = []
    
    """
    # 改修メモ
    カラムリストは、検知リストに何があるかを取ってくるようにした方が良い
    そのリスト名を取得して、変数名にできると良い。exec関数を使うと行けそう。
    """ 

    for time,dicts in all:
        index.append(time[:-2])

        for key,value in dicts.items():
            column_1.append(key)
            value_1.append(value)

    one_game_results = pd.DataFrame(data=zip(column_1,value_1),
                                    columns=columns_list,
                                    index=index)
    
    one_game_results = one_game_results.to_json(orient = 'index')

    # print(one_game_results)
    mng.collection.insert_one({"one_game_results":one_game_results})