import streamlit as st
import pandas as pd
import numpy as np
import plotly.figure_factory as ff


st.write("#WELCOME TO MY APP#")

st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

#styler example


dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(dataframe.style.highlight_max(axis=1).highlight_min(axis=0))

#create a line graph

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

#plot a map 
#sanfran latitude 

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)

#widget

x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)


#checkbox with Show and Hide Data 

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

chart_data


#selectbox 

st.header('Selectbox example :blue')

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

option = st.selectbox(
    'Which number do you like best?',
     df['second column'])

'You selected: ', option


#select box in Sidebar


st.sidebar.header('Selectbox example in Sidebar :blue')

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

option = st.sidebar.selectbox(
    'Which number do you like best?',
     df['second column'], key=2)

st.sidebar.write('You selected: ', option)


#Grid Example


columns = st.columns(3)

with columns[0]:
    st.metric("Temparature", "70F", "1.2F", help='Temparature of the Day') #tooltip functionality
    chart_data_metrics = pd.DataFrame(
     np.random.randn(10, 2),
     columns=['a', 'b'])

    st.area_chart(chart_data_metrics,use_container_width=True)

with columns[1]:
    st.metric("Car Prices", "$60,000","$5000", delta_color = 'inverse', help='Prices of Car as per Car Sales' )
    st.line_chart(chart_data_metrics,use_container_width=True)

with columns[2]:
    st.metric("House Prices", "1,000,000", "$80000",help='House Prices as per Realestate Data')
    st.bar_chart(chart_data_metrics,use_container_width=True)


#Concept of Tabs

tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

with tab1:
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

with tab2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)




