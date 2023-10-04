import streamlit as st
import pandas as pd
import streamlit_pandas as sp

@st.cache_data
def load_data():
    df = pd.read_csv(file)
    return df

file = "./dataset/test.csv"
df = load_data()

st.sidebar.title("Filter Dataset")
all_widgets = sp.create_widgets(df)
res = sp.filter_df(df, all_widgets)

st.title("Income Dataset based on Various Factors")
st.write("This dataset, namely the Income Dataset, is obtained from Kaggle provided by MUSTAFA FATAKDAWALA. ")

tab11, tab12 = st.tabs(["Original Dataset", "Filtered Dataset"])
with tab11:
    st.write(df)

with tab12:
    st.write(res)


st.header("Charts")
tab21, tab22, tab23 = st.tabs(["Age", "Marital Status", "Gender"])

with tab21:
    st.area_chart(df['age'])    
   
with tab22:
    st.line_chart(df['marital-status'])

with tab23:
    st.bar_chart(df['gender'])
