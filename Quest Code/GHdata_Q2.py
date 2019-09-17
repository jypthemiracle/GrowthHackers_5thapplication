%matplotlib inline
import numpy as np
import pandas as pd

youtubers = pd.read_csv("youtubers.csv")
youtubers.describe(include="all")
youtubers['realLike'] = youtubers['avgLike'] / youtubers['subscriberCount']

#realLike, realComment, realLikepareDisLike 변수 생성
youtubers['realLike'] = youtubers['avgLike'] / youtubers['subscriberCount']
youtubers['realComment'] = youtubers['avgComment'] / youtubers['subscriberCount']
youtubers['realDisLike'] = youtubers['avgDislike'] / youtubers['subscriberCount']
youtubers['metrics'] = youtubers['realDisLike'] / youtubers['realLike']

youtubers.drop(['videoCount','avgLike','avgDislike','avgComment','realLike','realComment','realDisLike'], axis=1, inplace=True)
youtubers_new = youtubers[youtubers['recentFrequency']>2]
youtubers_new.sort_values(by='metrics', axis=0).head(3)