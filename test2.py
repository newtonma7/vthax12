import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

x = [100, 200,300,400,800,1300]
y = [2018,2019,2020,2021,2022,2023]

coeff = np.polyfit(x, y, 2)
p = np.poly1d(coeff)

xpoly = np.linspace(min(x),max(x),100)
ypoly = p(xpoly)


figNY = px.scatter(x=x, y=y, labels={'x': 'USD', 'y': 'years'})

figNY.add_traces(go.Scatter(x= xpoly, y= ypoly, mode='lines', name='Polynomial Trendline'))


#trendline = px.scatter(x=xpoly, y= ypoly, mode='lines', name='Polynomial Trendline')

figNY.show()
#st.plotly_chart(figNY)