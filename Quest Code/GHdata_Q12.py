import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import statsmodels.api as sm

youtubers = pd.read_csv("youtubers.csv")
df = pd.DataFrame(youtubers, columns = ["youtuber", "subscriberCount", "videoCount", "avgLike", "avgDislike", "avgComment", "recentFrequency", "idconcentration"])
body = df[["avgDislike","avgComment"]]
body.tail()

reg = sm.OLS.from_formula("avgComment ~ avgDislike", body).fit()
reg.summary()