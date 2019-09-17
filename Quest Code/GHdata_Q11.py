import pandas as pd
import numpy as np
import matplotlib.pylab as plt

youtubers = pd.read_csv("youtubers.csv")
df = pd.DataFrame(youtubers, columns = ["youtuber", "subscriberCount", "videoCount", "avgLike", "avgDislike", "avgComment", "recentFrequency", "idconcentration"])
body = df[["avgLike","avgDislike"]]

plt.scatter( body['avgLike'], body['avgDislike'], label = "data")
plt.legend(loc = "best")
plt.xlabel('avgLike')
plt.ylabel('avgDislike')
plt.show()