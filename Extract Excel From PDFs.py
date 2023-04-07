import streamlit as st
import pandas as pd
import numpy as np
import tabula 
from io import StringIO
import time



st.header("Extract Tables from PDFs")

st.subheader("This application uses Tabula-Py to extract PDFs")

#upload a PDF

uploaded_file = st.file_uploader("Choose a file")

##change the upload file to Data Frame

if uploaded_file is not None:
	df_uploaded=tabula.read_pdf(uploaded_file)
else :st.write('No file Uploaded')

##enter the page number

Text_input = st.text_input("Enter Page number 👇")
if Text_input is not None:
	st.write("You entered: ", Text_input)

else: Text_input='all'

##Function Calls  

def convert_pdf_csv(data1,data2):
	converted_pdf=tabula.convert_into(uploaded_file, "output_Streamlit", output_format="csv", pages=Text_input)
	return converted_pdf

def read_pdf(filename):
	read_pdf_file=tabula.read_pdf(uploaded_file, stream=True)
	return read_pdf_file

Final_result=read_pdf(df_uploaded)

df=pd.DataFrame()

csv=df.reset_index(drop=True, inplace=True)
csv=st.dataframe(Final_result[0])


def convert_df(df):

    # IMPORTANT: Cache the conversion to prevent computation on every rerun

    return df.to_csv().encode('utf-8')


csv = convert_df(Final_result[0])

st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name=uploaded_file.name,
    mime='text/csv',
)


st.text('Copyright: MIT Common | Developed by Binay Siddharth')
