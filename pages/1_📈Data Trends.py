import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# image files
logo = "gallery/logo.png"
full_logo = "gallery/fulllogo.png"

# function that uses CSS to design a style for the sidebar logo to make it bigger and generate it
def set_logo_size():
    st.markdown("""<style>
    div[data-testid="stSidebarHeader"] > img, div[data-testid="collapsedControl"] > img {
        height: 7rem;
        width: auto;
    }
    
    div[data-testid="stSidebarHeader"], div[data-testid="stSidebarHeader"] > *,
    div[data-testid="collapsedControl"], div[data-testid="collapsedControl"] > * {
        display: flex;
        align-items: center;
    }
    </style>""", unsafe_allow_html=True)

    # displays the logo in the sidebar - collapsable
    st.logo(
        full_logo,
        icon_image=logo,
    )

st.set_page_config(page_title="Data Trends")
set_logo_size()
st.title("🏠📈Housing Data Trends📈🏠")
dataf = pd.read_csv("USRealEstateTrends.csv")

st.markdown("Data shows that in the recent years, housing value has been steadily climbing while actual housing has becoming increasingly scarce. Using data provided by Zillow we find that the prices have been increasing following a quadratic curve. We can observe that Los Angeles, New York, and Blacksburg follow a similar trend line despite being urban and rural areas. To view the graph without trendlines, click on the trendline in the legend on the right of the graph.")


#reducing dataframe to just homevalue data
dataf.drop(list(dataf.filter(regex = 'DaysPending')), axis = 1, inplace = True)
dataf.drop(list(dataf.filter(regex = 'CutRaw')), axis = 1, inplace = True)
dataf.head()

#cleaning data by filling in nulls
print('Null Data in DataFrame','\n')
print(dataf.isnull().sum().sum())
dataf = dataf.fillna(method='bfill')

dataf.head()

# we want city data for NY, Blacksburg, and LA

df_ny = dataf[dataf['SizeRank'] == 1]
df_ny.drop(["SizeRank", "RegionID", "RegionName", "StateName"], axis=1, inplace=True)
df_ny.head(5)

df_bb = dataf[dataf['SizeRank'] == 265]
df_bb.drop(["SizeRank", "RegionID", "RegionName", "StateName"], axis=1, inplace=True)
df_bb.head()

df_la = dataf[dataf['SizeRank'] == 2]
df_la.drop(["SizeRank", "RegionID", "RegionName", "StateName"], axis=1, inplace=True)
df_la.head()

#averaging all the housing prices for each year

arr1 = df_ny.to_numpy()
NYarr = arr1[0]

monthCount = 0
Avg2018NY = float(0)
Avg2019NY = float(0)
Avg2020NY = float(0)
Avg2021NY = float(0)
Avg2022NY = float(0)
Avg2023NY = float(0)
Avg2024NY = float(0)

for nums in NYarr:
    if(monthCount < 12):
        Avg2018NY += nums
        monthCount += 1
    if(monthCount >= 12 and monthCount < 24):
        Avg2019NY += nums
        monthCount += 1
    if(monthCount >= 24 and monthCount < 36):
        Avg2020NY += nums
        monthCount += 1
    if(monthCount >= 36 and monthCount < 48):
        Avg2021NY += nums
        monthCount += 1
    if(monthCount >= 48 and monthCount < 60):
        Avg2022NY += nums
        monthCount += 1
    if(monthCount >= 60 and monthCount < 72):
        Avg2023NY += nums
        monthCount += 1
    if(monthCount >= 72):
        Avg2024NY += nums
        monthCount += 1

#finding Blacksburg avg
arr2 = df_bb.to_numpy() 
BBarr = arr2[0]

monthCount = 0
Avg2018BB = float(0)
Avg2019BB = float(0)
Avg2020BB = float(0)
Avg2021BB = float(0)
Avg2022BB = float(0)
Avg2023BB = float(0)
Avg2024BB = float(0)

for nums in BBarr:
    if(monthCount < 12):
        Avg2018BB += nums
        monthCount += 1
    if(monthCount >= 12 and monthCount < 24):
        Avg2019BB += nums
        monthCount += 1
    if(monthCount >= 24 and monthCount < 36):
        Avg2020BB += nums
        monthCount += 1
    if(monthCount >= 36 and monthCount < 48):
        Avg2021BB += nums
        monthCount += 1
    if(monthCount >= 48 and monthCount < 60):
        Avg2022BB += nums
        monthCount += 1
    if(monthCount >= 60 and monthCount < 72):
        Avg2023BB += nums
        monthCount += 1
    if(monthCount >= 72):
        Avg2024BB += nums
        monthCount += 1


#finding Los Angeles avg
arr3 = df_la.to_numpy() 
LAarr = arr3[0]

monthCount = 0
Avg2018LA = float(0)
Avg2019LA = float(0)
Avg2020LA = float(0)
Avg2021LA = float(0)
Avg2022LA = float(0)
Avg2023LA = float(0)
Avg2024LA = float(0)

for nums in LAarr:
    if(monthCount < 12):
        Avg2018LA += nums
        monthCount += 1
    if(monthCount >= 12 and monthCount < 24):
        Avg2019LA += nums
        monthCount += 1
    if(monthCount >= 24 and monthCount < 36):
        Avg2020LA += nums
        monthCount += 1
    if(monthCount >= 36 and monthCount < 48):
        Avg2021LA += nums
        monthCount += 1
    if(monthCount >= 48 and monthCount < 60):
        Avg2022LA += nums
        monthCount += 1
    if(monthCount >= 60 and monthCount < 72):
        Avg2023LA += nums
        monthCount += 1
    if(monthCount >= 72):
        Avg2024LA += nums
        monthCount += 1


NYdata = {
    "Avg Housing Value (USD)":[Avg2018NY/12, Avg2019NY/12,Avg2020NY/12,Avg2021NY/12,Avg2022NY/12,Avg2023NY/12],
    "Year": [2018,2019,2020,2021,2022,2023]
}

BBdata = {
    "Avg Housing Value (USD)":[Avg2018BB/12, Avg2019BB/12,Avg2020BB/12,Avg2021BB/12,Avg2022BB/12,Avg2023BB/12],
    "Year": [2018,2019,2020,2021,2022,2023]
}

LAdata = {
    "Avg Housing Value (USD)":[Avg2018LA/12, Avg2019LA/12,Avg2020LA/12,Avg2021LA/12,Avg2022LA/12,Avg2023LA/12],
    "Year": [2018,2019,2020,2021,2022,2023]
}

# graph for NYC with polynomial trendline/regression
st.header("New York City, NY", divider = "rainbow")
st.subheader("Average Housing Value (USD) in New York City, NY from 2018 to 2023")
x = [2018,2019,2020,2021,2022,2023]
y = [Avg2018NY/12, Avg2019NY/12,Avg2020NY/12,Avg2021NY/12,Avg2022NY/12,Avg2023NY/12]

coeff = np.polyfit(x, y, 2)
coeffLin = np.polyfit(x,y,1)
p = np.poly1d(coeff)
pLin = np.poly1d(coeffLin)

xpoly = np.linspace(min(x),max(x),100)
ypoly = p(xpoly)

yLin = pLin(xpoly)

figNY = px.scatter(NYdata, x='Year', y='Avg Housing Value (USD)')

figNY.add_traces(go.Scatter(x= xpoly, y= ypoly, mode='lines', name='Polynomial Trendline'))
figNY.add_traces(go.Scatter(x= xpoly, y= yLin, mode='lines', name='Linear Trendline'))

st.plotly_chart(figNY)

#graph for Blacksburg with polynomial trendline/regression
st.header("Blacksburg, VA", divider = "orange")
st.subheader("Average Housing Value (USD) in Blacksburg, VA from 2018 to 2023")
x = [2018,2019,2020,2021,2022,2023]
y = [Avg2018BB/12, Avg2019BB/12,Avg2020BB/12,Avg2021BB/12,Avg2022BB/12,Avg2023BB/12]

coeff = np.polyfit(x, y, 2)
coeffLin = np.polyfit(x,y,1)
p = np.poly1d(coeff)
pLin = np.poly1d(coeffLin)

xpoly = np.linspace(min(x),max(x),100)
ypoly = p(xpoly)

yLin = pLin(xpoly)

figBB = px.scatter(BBdata, x='Year', y='Avg Housing Value (USD)')

figBB.add_traces(go.Scatter(x= xpoly, y= ypoly, mode='lines', name='Polynomial Trendline'))
figBB.add_traces(go.Scatter(x= xpoly, y= yLin, mode='lines', name='Linear Trendline'))

st.plotly_chart(figBB)

#graph for Los Angeles with polynomial trendline/regression
st.header("Los Angeles, LA", divider = "red")
st.subheader("Average Housing Value (USD) in Los Angeles, LA from 2018 to 2023")
x = [2018,2019,2020,2021,2022,2023]
y = [Avg2018LA/12, Avg2019LA/12,Avg2020LA/12,Avg2021LA/12,Avg2022LA/12,Avg2023LA/12]

coeff = np.polyfit(x, y, 2)
p = np.poly1d(coeff)
coeffLin = np.polyfit(x,y,1)
pLin = np.poly1d(coeffLin)

xpoly = np.linspace(min(x),max(x),100)
ypoly = p(xpoly)

yLin = pLin(xpoly)

figLA = px.scatter(LAdata, x='Year', y='Avg Housing Value (USD)')

figLA.add_traces(go.Scatter(x= xpoly, y= ypoly, mode='lines', name='Polynomial Trendline'))
figLA.add_traces(go.Scatter(x= xpoly, y= yLin, mode='lines', name='Linear Trendline'))

st.plotly_chart(figLA)