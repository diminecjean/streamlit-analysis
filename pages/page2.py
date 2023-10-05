import streamlit as st
import pandas as pd
import streamlit_pandas as sp
import requests

st.title("Public Transportation Ridership 🚄")
st.write("This dataset is obtained from data.gov.my through their data catalogue API.")

user_input = st.text_input("Number of rows to display", "100")

try:
    limit = int(user_input)  
    url = f"https://api.data.gov.my/data-catalogue?id=ridership_headline&limit={limit}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        st.write(df)

        st.header("Ridership of Each Line")
        tab0, tab1, tab2, tab3, tab4 = st.tabs(["All","LRT Kelana Jaya Line", "LRT Ampang Line", "MRT Kajang Line", "Monorail"])
        with tab0:
            data_to_display = df[['date', 'rail_lrt_kj', 'rail_lrt_ampang','rail_mrt_kajang','rail_monorail']]
            st.line_chart(data_to_display.set_index('date'))
        
        with tab1:
            st.line_chart(df.set_index('date')['rail_lrt_kj'])

        with tab2:
            st.line_chart(df.set_index('date')['rail_lrt_ampang'])
        
        with tab3:
            st.line_chart(df.set_index('date')['rail_mrt_kajang'])

        with tab4:
            st.line_chart(df.set_index('date')['rail_monorail'])
            
    else:
        st.write("Error fetching data from the API")
except ValueError:
    st.write("Please enter a valid number.")
