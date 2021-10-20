import streamlit as st
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns
import os
import pickle
import joblib

##############################################################################################
#untilities

def interpreter(number):

    if number == 0:
        return 'Iris-Setosa'
    elif number ==1:
        return 'Iris-Versicolour'

    else:
        return 'Iris-Virginica'



#############################################################################################


def main():
    page = st.sidebar.selectbox("Choose a page",["About App","Data Explorer","Machine Learning","Opinion pieces"])

    if page =="About App":
        st.title("The Gradient Boost Streamlit Demonstration")
        st.image("images/GB.png",width=300)
        
        st.markdown(""" The purpose of this app is to showcase some streamlit usecases. 
                This page informs the user on how to interact with the app to get the 
                best out of it.""")

        st.title("Meet the Data Scientists")



        col1,mid,col2 = st.columns([1,1,1])
        with col1:
            st.image('images/ironman2.jpg',width=300)
            st.markdown('**Name Surname**')
        with col2:
            st.image('images/ironman2.jpg',width=300)
            st.markdown('**Name Surname**')
        

    if page =="Data Explorer":
        st.title("Explore Your Dataset")
        data = st.file_uploader("Only csv files allowed",type=['csv'])

        if data:
            data = pd.read_csv(data)

            st.title("Look at the DataFrame")
            st.dataframe(data)

            with st.expander("Visualize the data?"):
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

        with st.expander("Predict Flower Class"):
            s_len = st.number_input('Sepal Length')
            s_wid = st.number_input('Sepal Width')

            p_len = st.number_input('Petal Length')
            p_wid = st.number_input('Petal Width')
            model_name = 'models/decision_tree_model.sav'
            model = pickle.load(open(model_name,'rb'))
            if st.button('Perform the classification task'):

                mylist = np.array([s_len,s_wid,p_len,p_wid]).reshape(1,-1)

                result = interpreter(model.predict(mylist))
                
                result = "The species in question is"+" " + result
                st.title(result)
                
        st.title('Regression problems')
        with st.expander("Predict movie rating"):
            movie_num = st.number_input('movie number')

            if st.button('Rate the movie'):
                result = "Movie Rating: 6.7"
                st.title(result)

    if page =="Opinion pieces":
        st.title("Opinion Pieces")
        with st.expander("Data Engineering")

if __name__=="__main__":
    main()
