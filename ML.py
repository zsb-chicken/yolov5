from mongo_command import Mongo_Command
from bson.objectid import ObjectId

import pandas as pd
import numpy as np
import json

mng = Mongo_Command()
post_id = "622468246a0e4c69e8764f12"

one_game_results = mng.collection.find_one({"_id":ObjectId(post_id)})
one_game_results = json.loads(one_game_results['one_game_results'])
one_game_results = pd.DataFrame.from_dict(one_game_results,orient="index")

print(one_game_results)
print(type(one_game_results))