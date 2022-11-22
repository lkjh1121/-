# 화면 나눠서 여러개 차트 동시에  그리기
from datetime import date
from logging.config import valid_ident
from multiprocessing.sharedctypes import Value
from optparse import Values
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


aapl = pd.read_csv("./aapl_Data.csv")
amzn = pd.read_csv("./amzn_Data.csv")
googl = pd.read_csv("./googl_Data.csv")
nflx = pd.read_csv("./nflx_Data.csv")
fb = pd.read_csv("./fb_Data.csv")
goog = pd.read_csv("./goog_Data.csv")
print( aapl.head() )
print( aapl.info() )

print("===================================================")
def changeDate(date1):
    return date1[0:7]+"-01"

print(  changeDate(aapl.loc[0,'Date']) )

aapl["aapl"] = aapl["Date"].apply( changeDate)
print( aapl.head())

#############################################################################

def changeDate(date2):
    return date2[0:7]+"-01"

print(  changeDate(amzn.loc[0,'Date']) )

amzn["amzn"] = amzn["Date"].apply( changeDate)
print( amzn.head() )

#############################################################################

def changeDate(date3):
    return date3[0:7]+"-01"

print(  changeDate(googl.loc[0,'Date']) )

googl["googl"] = googl["Date"].apply( changeDate)
print( googl.head() )

#############################################################################

def changeDate(date4):
    return date4[0:7]+"-01"

print(  changeDate(nflx.loc[0,'Date']) )

nflx["nflx"] = nflx["Date"].apply( changeDate)
print( nflx.head() )

#############################################################################

def changeDate(date5):
    return date5[0:7]+"-01"

print(  changeDate(fb.loc[0,'Date']) )

fb["fbook"] = fb["Date"].apply( changeDate)
print( fb.head() )

#############################################################################

def changeDate(date6):
    return date6[0:7]+"-01"

print(  changeDate(goog.loc[0,'Date']) )

goog["goog"] = goog["Date"].apply( changeDate)
print( goog.head() )

#############################################################################
print("------------------------------------------------------------------------")
aapl2 =  aapl.groupby("aapl").agg(mean_open=('Open', 'mean'),
                                 mean_High=('High', 'mean'),
                                 mean_Low=('Low', 'mean'),
                                 mean_close=('Close', 'mean'))
aapl2.to_csv("aapl2.csv", encoding="cp949")
######################################################################
amzn2 =  amzn.groupby("amzn").agg(mean_open=('Open', 'mean'),
                                 mean_High=('High', 'mean'),
                                 mean_Low=('Low', 'mean'),
                                 mean_close=('Close', 'mean'))
amzn2.to_csv("amzn2.csv", encoding="cp949")
######################################################################
fb2 =  fb.groupby("fbook").agg(mean_open=('Open', 'mean'),
                                 mean_High=('High', 'mean'),
                                 mean_Low=('Low', 'mean'),
                                 mean_close=('Close', 'mean'))
fb2.to_csv("fb2.csv", encoding="cp949")
######################################################################
goog2 =  goog.groupby("goog").agg(mean_open=('Open', 'mean'),
                                 mean_High=('High', 'mean'),
                                 mean_Low=('Low', 'mean'),
                                 mean_close=('Close', 'mean'))
goog2.to_csv("goog2.csv", encoding="cp949")
######################################################################
googl2 =  googl.groupby("googl").agg(mean_open=('Open', 'mean'),
                                 mean_High=('High', 'mean'),
                                 mean_Low=('Low', 'mean'),
                                 mean_close=('Close', 'mean'))
googl2.to_csv("googl2.csv", encoding="cp949")
######################################################################
nflx2 =  nflx.groupby("nflx").agg(mean_open=('Open', 'mean'),
                                 mean_High=('High', 'mean'),
                                 mean_Low=('Low', 'mean'),
                                 mean_close=('Close', 'mean'))
nflx2.to_csv("nflx2.csv", encoding="cp949")
######################################################################


# 출력
# print( aapl.groupby("aapl").agg(mean_open=('Open', 'mean'),
#                                  mean_close=('Close', 'mean')).head ())

# print( googl.groupby("googl").agg(mean_open=('Open', 'mean'),
#                                  mean_close=('Close', 'mean')).head ())

# print( amzn.groupby("amzn").agg(mean_open=('Open', 'mean'),
#                                  mean_close=('Close', 'mean')).head ())

# print( nflx.groupby("nflx").agg(mean_open=('Open', 'mean'),
#                                  mean_close=('Close', 'mean')).head ())

# print( fb.groupby("fbook").agg(mean_open=('Open', 'mean'),
#                                  mean_close=('Close', 'mean')).head ())

# print( goog.groupby("goog").agg(mean_open=('Open', 'mean'),
#                                  mean_close=('Close', 'mean')).head ())


# aapl_Data = sns.load_dataset("./aapl_Data.csv")
# sns.relplot(
#     data=aapl, kind="line",
#     x="timepoint", y="signal", col="region",
#     hue="event", style="event",
# )


