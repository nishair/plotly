import pandas as pd
import plotly.graph_objs as go

mdata = pd.read_csv("OptumRx.csv")
mdata
mdata.columns
m1 = mdata[['Created','Updated','Resolved']]
fig = go.FigureWidget()

trace_start = go.Scatter(x=df.Created,y=df[‘stime’],
mode=‘markers’,
name = “start time”,
line = dict(color = ‘green’),
opacity = 0.8)


Created = pd.to_datetime(m1["Created"])

m1["Created"] = pd.to_datetime(m1["Created"])
m1["Updated"] = pd.to_datetime(m1["Updated"])
m1["Resolved"] = pd.to_datetime(m1["Resolved"])

dates = m1["Created"].dt.date
created = m1["Created"] 
updated = m1["Updated"]
resolved = m1["Resolved"]

fig = go.FigureWidget()

fig.add_bar(x=dates,
            y=created
            )

            import plotly.plotly as py
import plotly.graph_objs as go

py.plot(fig, filename = 'basic-line', auto_open=True)

m1['Difference'] = created / np.timedelta64(1, 'D')

ctime = m1["Created"].dt.time
utime = m1["Updated"].dt.time
rtime = m1["Resolved"].dt.time

test = ctime - utime

from datetime import datetime
