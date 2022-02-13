

from collections import deque
from tokenize import Special
import redis
from redis_command import Redis_Command
rds = Redis_Command()
import time


streamkey = "2022-02-13-21:00:52"

class Interpreter:
    
    def __init__(self) -> None:
        self.special_d = deque
        pass

    def special_itprt(names):
        fields_key = "special"
        fields = rds.redis_stream_data_readgroup(names,streamkey)
        special_num = fields[1][fields_key]
        return  print(special_num)

    def queue(self):
        self.special_d.append(self.special_itprt())
        return print(self.special_d)

if __name__ == "__main__":
    while time.time() - time.time() <= 30:
        time.sleep(1)
        Interpreter.special_itprt(names="special")
    else:
        print("!!FINISH!!")