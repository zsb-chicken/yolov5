####　構成 ####
# クラス化
# イニシャライズ　redisへ接続
# - - - - - - - - - - - - - - - - - - -
# ・キーを自動生成
# ・バリューは検知結果（できればJSON）

import redis
import datetime
from collections import deque


class Redis_Command:
    r = redis.Redis(host='localhost', port=6379, decode_responses = True, db=0) 
    r2 = redis.Redis(host='localhost', port=6379, decode_responses = True, db=1) 

    def __init__(self):
        """
        streamkeyをタイムスタンプにして、毎回動作のたびにストリームを分けて動作するようにする
        """
        today =  datetime.datetime.now()
        self.streamkey = today.strftime('%Y-%m-%d-%H:%M:%S')
        #redis streamのstreamIDとするキーとしてcommonkeyを定義

    def commonkey_set(self):
        self.r.set("commonkey",self.streamkey)
        return self.r.get("commonkey")

    def commonkey_get(self):
        self.commonkey = self.r.get("commonkey")
        return self.commonkey

    def redis_data_set(self, detect_values):
        #r.set('hoge', 'moge')
        today =  datetime.datetime.now()
        keys = today.strftime('%Y-%m-%d %H:%M:%S.%f')
        values = detect_values
        self.r.set(keys, values)

    def redis_stream_data_set(self, dict):
        self.redisid_db0 = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')
        self.r.xadd(self.commonkey_get(),dict,id=self.redisid_db0[:-1]) #redisに入るように

    def redis_stream_data_set_2(self, dict):
        self.redisid_db1 = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')
        self.r2.xadd(self.commonkey_get(),dict,id=self.redisid_db1[:-1])
       

    # def redis_stream_data_read(self):
    #     fields = self.r.xread(self.commonkey,block=0)
    #     return fields

    # def redis_stream_data_readgroup(self,names,streamkey):
    #     fields = self.r.xreadgroup(names,names+"-1",{streamkey:0},1,block=None)
    #     print("consumer_groupname:",names)
    #     print("consumername:",names+"-"+1)
    #     return fields
    
    
if __name__ == '__main__':
    """
    .pyを動かすと、この結果が返る
    """
    Rtest = Redis_Command()
    Rtest.redis_stream_data_set({"testkey":"testvalue"})
    # Rtest.redis_stream_data_set_2({"testkey_2":"testvalue_2"})