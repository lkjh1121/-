import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime
import pandas as pd

appl = pd.read_csv("./aapl_Data.csv")
# 데이터를 가져올 날짜 설정
start_date = datetime(2019,9,3)
end_date = datetime(2022,9,1)

# appl = appl.reset_index()# Date index를 Column으로 보내주기 위함
# appl['Date'] = appl['Date'].apply(lambda x : datetime.strftime(x, '%Y-%m-%d')) # Datetime to str
# plotly 캔들스틱 그래프 그리기
stock_name = '애플'

fig = go.Figure(data=[go.Candlestick(x=appl['Date'],
                                    open=appl['Open'],
                                    high=appl['High'],
                                    low=appl['Low'],
                                    close=appl['Close'])])
# x축 type을 카테고리 형으로 설정, 순서를 오름차순으로 날짜순서가 되도록 설정
fig.layout = dict(title=stock_name, 
                       xaxis = dict(type="category", 
                                    categoryorder='category ascending'))
fig.update_xaxes(nticks=5)
fig.show()
