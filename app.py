import streamlit as st
import pandas as pd
import streamlit_pandas as sp
import time

import os

from st_pages import Page, add_page_title, show_pages


show_pages(
    [
        Page("./app.py","Home","🏠"),
        Page("./pages/page1.py", "Income Dataset", "💵"),
        Page("./pages/page2.py", "Transportation Ridership", "🚄")
    ]
)

st.title("Streamlit Data Analysis")
st.write("View sample dataset analysis on the other pages or")

data_file = st.file_uploader("Upload your dataset in the form of CSV",type=["csv"])
		
if data_file is not None:

    file_details = {"filename":data_file.name, "filetype":data_file.type,
                    "filesize":data_file.size}
    
    df = pd.read_csv(data_file)

    all_widgets = sp.create_widgets(df)
    res = sp.filter_df(df, all_widgets)

    tab11, tab12 = st.tabs(["Original Dataset", "Filtered Dataset"])
    with tab11:
        st.write(df)

    with tab12:
        st.write(res)
