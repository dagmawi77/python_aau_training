import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import plotly.subplots as sp
s['week_start'] = pd.to_datetime(
s['week_start'])
weekly = s.groupby('week_start')[
'reported_cases'].sum().reset_index()
fig = px.line(weekly, x='week_start',
y='reported_cases', markers=True)
fig.show()