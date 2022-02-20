from redis_command import Redis_Command
import datetime
import pandas as pd

rds = Redis_Command()

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
    columns = []
    values = []
    
    for time,dicts in all:
        index.append(time[:-2])

        for key,value in dicts.items():
            columns.append(key)
            values.append(value)

    # pd_data = pd.DataFrame(data=values,index=index,columns=columns)
    print(index)
    print(columns)
    print(values)