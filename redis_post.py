####　構成 ####
# クラス化
# イニシャライズ　redisへ接続
# - - - - - - - - - - - - - - - - - - -
# ・キーを自動生成
# ・バリューは検知結果（できればJSON）

import redis
import datetime


class Redis_Data_Set:
    r = redis.Redis(host='localhost', port=6379,  decode_responses = True, db=0) 

    def redis_data_set(self, detect_values):
        #r.set('hoge', 'moge')
        today =  datetime.datetime.now()
        keys = today.strftime('%Y-%m-%d %H:%M:%S.%f')
        print(keys)

        values = detect_values
        print(values)
                
        self.r.set(keys, values)


if __name__ == '__main__':
    R = Redis_Data_Set()
    R.redis_data_set("testvalue")