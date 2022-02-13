

from collections import deque
from optparse import Values
from tokenize import Special
from pandas import array
import redis
from redis_command import Redis_Command
import time

rds = Redis_Command()

streamkey = "2022-02-13-21:00:52"

class Interpreter:    
    def __init__(self,streamkey,group) -> None:
        self.special_d = deque(maxlen=8)
        self.streamkey = streamkey
        self.group = group

    # def special_itprt(names):
    #     fields_key = "special"
    #     fields = rds.redis_stream_data_readgroup(names,streamkey)
    #     special_num = fields[1][fields_key]
    #     return  print(special_num)

    def redis_read(self):
        fields = rds.r.xread({self.streamkey:0},block=0,count=1)
        return fields

    def queue(self):
        b = self.redis_read()[0][1][0][1][self.group]
        self.special_d.append(b)
        return self.special_d

if __name__ == "__main__":
    #Interpreterの起動時間
    itprt = Interpreter("2022-02-13-21:00:52","special")

    while time.time() - time.time() <= 30:
        time.sleep(0.1)

        # 実際の処理はここから        
        c = itprt.redis_read()
        print(c)

        # print(c[0][1][0][1]["special"]) と同義
        d = itprt.queue()
        print(d)

    #終わり
    else:
        print("!!FINISH!!")