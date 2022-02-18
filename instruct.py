from collections import deque
from redis_command import Redis_Command
import time

rds = Redis_Command()

class Instruction:    
    def __init__(self,fieldkey) -> None:
        self.streamkey = rds.commonkey_get()
        print(rds.commonkey_get())
        self.fieldkey = fieldkey

    def message(self):
        fields = rds.r2.xread({self.streamkey:"$"},block=0,count=1)
        msg = fields[0][1][0][1][self.fieldkey]
        return msg

if __name__ == "__main__":

    instr = Instruction("instruction1")
    
    while time.time() - time.time() <= 30:
        time.sleep(0.1)

        # 実際の処理はここから        
        print(instr.message())

    #終わり
    else:
        print("!!FINISH!!")