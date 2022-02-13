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

    def __init__(self) -> None:
        """
        streamkeyをタイムスタンプにして、毎回動作のたびにストリームを分けて動作するようにする
        """
        today =  datetime.datetime.now()
        self.streamkey = today.strftime('%Y-%m-%d-%H:%M:%S')
        print(self.streamkey)

    def redis_data_set(self, detect_values):
        #r.set('hoge', 'moge')
        today =  datetime.datetime.now()
        keys = today.strftime('%Y-%m-%d %H:%M:%S.%f')
        values = detect_values
        self.r.set(keys, values)

    def redis_stream_data_set(self, dict):
        self.r.xadd(self.streamkey,dict,"*")
        print("def_redis_stream_data_set...",dict)

    # def redis_stream_data_read(self):
    #     fields = self.r.xread(self.streamkey,block=0)
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