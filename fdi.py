import pandas as pd
import plotly.express as px
import streamlit as st

# Load the dataset
fdi_data = pd.read_csv('FDI data.csv')

# Sidebar
st.sidebar.title('Filters')
selected_sector = st.sidebar.selectbox('Select Sector', fdi_data['Sector'].unique())
selected_years = st.sidebar.multiselect('Select Years', fdi_data.columns[1:])  # Assuming the years are columns from 1st index onwards

# Total FDI by Sector
total_fdi_by_sector = fdi_data.groupby('Sector')[selected_years].sum()

# Year-wise FDI Trends
yearly_fdi_trends = fdi_data[selected_years].sum()

# Sector-wise FDI Distribution
sector_fdi_distribution = fdi_data.groupby('Sector')[selected_years].sum()

# Calculating the Growth rate of FDI 
selected_yearly_fdi = fdi_data[['Sector'] + selected_years]
fdi_growth_rate = selected_yearly_fdi.set_index('Sector').pct_change(axis='columns')

# Correlation Analysis
correlation_matrix = fdi_data[selected_years].corr()

# Displaying the results
st.title(':chart_with_upwards_trend: Foreign Direct Investment')

# Total FDI by Sector
st.subheader('Total FDI by Sector')
st.write(total_fdi_by_sector.loc[selected_sector])

# Year-wise FDI Trends
st.subheader('Year-wise FDI Trends')
st.line_chart(yearly_fdi_trends)

# Sector-wise FDI Distribution
st.subheader('Sector-wise FDI Distribution')
st.bar_chart(sector_fdi_distribution.loc[selected_sector])

# Growth Rate of FDI
st.subheader('Growth Rate of FDI')
st.write('Growth rate is the percentage change in a variable over a specific period, calculated as the difference between final and initial values divided by the initial value, expressed as a percentage.')
if selected_sector in fdi_growth_rate.index:
    st.line_chart(fdi_growth_rate.loc[selected_sector])
else:
    st.write(f"No data available for the selected sector: {selected_sector}")

# Correlation Analysis
st.subheader('Correlation Analysis')
st.write("Measures the degree of association between two or more variables. A positive value indicates variables move in the same direction, a negative value indicates variables move in opposite directions, and a value close to zero suggests a weak or no correlation")
st.write(correlation_matrix)
