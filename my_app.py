import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import os
import joblib

##############################################################################################
#untilities




#############################################################################################


def main():
    page = st.sidebar.selectbox("Choose a page",["About App","Problem Statement","Data Explorer","Machine Learning"])

    if page =="About App":
        st.title("The Gradient Boost Streamlit Demonstration")
        st.image("images/GB.png",width=300)
        
        st.markdown(""" The purpose of this app is to showcase some streamlit usecases. 
                This page informs the user on how to interact with the app to get the 
                best out of it.""")

        st.title("Meet the Data Scientists")



        col1,mid,col2 = st.beta_columns([2,2,3])
        with col1:
            st.image('images/GB.png',width=300)
            st.markdown('**Name Surname**')
        with col2:
            st.image('images/GB.png',width=300)
            st.markdown('**Name Surname**')
        

    if page =="Data Explorer":
        st.title("Explore the dataset")
        st.markdown(""" This page is buggy.... still to figure out why""")
        
        data = st.file_uploader("Only csv files allowed",type=['csv'])

        if data:
            data = pd.read_csv(data)

            st.title("Look at the DataFrame")
            st.dataframe(data)

            if st.checkbox("Visualize the data?"):
                dim=(15.0,10.0)
                fig = plt.figure(figsize=dim)

                viz_page = st.sidebar.selectbox('choose visual',['Count Plot','Bar Chart', 'Pie chart'])

                if viz_page == "Count Plot":
                    columns = data.columns
                    x = st.selectbox('choose column',columns)
                    
                    
                    sns.countplot(x=x,data=data)


                    st.pyplot(fig)


    if page =="Machine Learning":
        st.title("Machine Learning")



if __name__=="__main__":
    main()
