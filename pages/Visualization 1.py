import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px

#TITLE
st.title('CUACA v CUSTOMER')

#LOAD DATAFRAME
viz_tempscale = pd.read_csv('viz/temp_scale.csv')
viz_seasonscale = pd.read_csv('viz/season_scale.csv')
viz_lineplot = pd.read_csv('viz/lineplot.csv')

#VISUALIZATION
#VIZ 1
fig1 = px.bar(viz_tempscale, x="scale", y=["casual", "registered"], 
              color_discrete_map={"casual": "#FF0000", "registered": "#87CEEB"}, 
              title="Total Users by Temperature Scale ")
fig1.update_layout(
    xaxis_title="Temperature Level",
    yaxis_title="Total",
    legend_title="User"
)
st.plotly_chart(fig1, use_container_width=True, sharing="streamlit", theme="streamlit")

#VIZ 2
fig2 = px.bar(viz_seasonscale, x="xseason", y=["casual", "registered"],
              color_discrete_map={"casual": "#FF0000", "registered": "#87CEEB"},
              title="Total Users by Season Scale ")
fig2.update_layout(
    xaxis_title="Season & Temperature",
    yaxis_title="Total",
    legend_title="User"
)
st.plotly_chart(fig2, use_container_width=True, sharing="streamlit", theme="streamlit")

#LINECHART VIZ 3
fig3 = px.line(viz_lineplot, x='month_yr', y=["casual","registered"],
               color_discrete_map={"casual": "#0a437a", "registered": "#3c4d03"},
               markers=True, title="Total User for Medium-High Temperature")
fig3.update_layout(
    xaxis_title="Date",
    yaxis_title="Total Customer",
    legend_title="User"
)
fig3.update_xaxes(
    tickangle = 45    
)

st.plotly_chart(fig3, use_container_width=True, sharing="streamlit", theme="streamlit")

#SIDEBAR
with st.sidebar:
    with st.expander("About The Dataset"):
        st.write("""
        Bike-sharing rental process is highly correlated to the environmental and seasonal settings. For instance, weather conditions,
precipitation, day of week, season, hour of the day, etc. can affect the rental behaviors. The core data set is related to  
the two-year historical log corresponding to years 2011 and 2012 from Capital Bikeshare system, Washington D.C., USA which is 
publicly available in http://capitalbikeshare.com/system-data. We aggregated the data on two hourly and daily basis and then 
extracted and added the corresponding weather and seasonal information. Weather information are extracted from http://www.freemeteo.com. 
    """)
    with st.expander("Dataset License"):
        st.write("""
        License
=========================================
Use of this dataset in publications must be cited to the following publication:""")
        st.write("""[1] Fanaee-T, Hadi, and Gama, Joao, "Event labeling combining ensemble detectors and background knowledge", Progress in Artificial Intelligence (2013): pp. 1-15, Springer Berlin Heidelberg, doi:10.1007/s13748-013-0040-3.""")
        st.write("""@article{
	year={2013},
	issn={2192-6352},
	journal={Progress in Artificial Intelligence},
	doi={10.1007/s13748-013-0040-3},
	title={Event labeling combining ensemble detectors and background knowledge},
	url={http://dx.doi.org/10.1007/s13748-013-0040-3},
	publisher={Springer Berlin Heidelberg},
	keywords={Event labeling; Event detection; Ensemble learning; Background knowledge},
	author={Fanaee-T, Hadi and Gama, Joao},
	pages={1-15}
}""")
    with st.expander("Dataset Files"):
        st.write("""
            Files
=========================================

	- Readme.txt
	- hour.csv : bike sharing counts aggregated on hourly basis. Records: 17379 hours
	- day.csv - bike sharing counts aggregated on daily basis. Records: 731 days
 """)
    with st.expander("Dataset Characteristics"):
        st.write("""
                Dataset characteristics
=========================================	
Both hour.csv and day.csv have the following fields, except hr which is not available in day.csv
	
	- instant: record index
	- dteday : date
	- season : season (1:springer, 2:summer, 3:fall, 4:winter)
	- yr : year (0: 2011, 1:2012)
	- mnth : month ( 1 to 12)
	- hr : hour (0 to 23)
	- holiday : weather day is holiday or not (extracted from http://dchr.dc.gov/page/holiday-schedule)
	- weekday : day of the week
	- workingday : if day is neither weekend nor holiday is 1, otherwise is 0.
	+ weathersit : 
		- 1: Clear, Few clouds, Partly cloudy, Partly cloudy
		- 2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist
		- 3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds
		- 4: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog
	- temp : Normalized temperature in Celsius. The values are divided to 41 (max)
	- atemp: Normalized feeling temperature in Celsius. The values are divided to 50 (max)
	- hum: Normalized humidity. The values are divided to 100 (max)
	- windspeed: Normalized wind speed. The values are divided to 67 (max)
	- casual: count of casual users
	- registered: count of registered users
	- cnt: count of total rental bikes including both casual and registered
""")
