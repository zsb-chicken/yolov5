from collections import deque
from redis_command import Redis_Command
import time

rds = Redis_Command()

class Interpreter:    
    def __init__(self,fieldkey) -> None:
        self.special_deque = deque(maxlen=8)
        self.streamkey = rds.commonkey_get()
        print(rds.commonkey_get())
        self.fieldkey = fieldkey

    # def special_itprt(names):
    #     fields_key = "special"
    #     fields = rds.redis_stream_data_readgroup(names,streamkey)
    #     special_num = fields[1][fields_key]
    #     return  print(special_num)

    def redis_read(self):
        fields = rds.r.xread({self.streamkey:"$"},block=0,count=1)
        return fields

    def queue(self):
        b = self.redis_read()[0][1][0][1][self.fieldkey]
        self.special_deque.append(int(b))
        return self.special_deque

if __name__ == "__main__":
    #Interpreterの起動時間
    itprt = Interpreter("special")
    
    while time.time() - time.time() <= 30:
        time.sleep(0.1)

        # 実際の処理はここから

        #redis_readの中身を確認するなら
        # print("fields",itprt.redis_read())

        d = itprt.queue()
        print(d)

        if max(d) == 1 or max(d) == 2:
            rds.redis_stream_data_set_2({"instruction1":"スペシャルあるぞ"})

        elif max(d) == 3:
            rds.redis_stream_data_set_2({"instruction1":"スペシャル合わせろ"})

        elif max(d) >= 4:
            rds.redis_stream_data_set_2({"instruction1":"スペシャル合わせろよ！！！！"})

        else:
            pass

    #終わり
    else:
        print("!!FINISH!!")