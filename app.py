import streamlit as st
import pickle
import pandas as pd
# ml=pickle.load(open('movies.pkl','rb'))
# ml=ml['title'].values
def recommend(movie):
    mi=movies[movies['title']==movie].index[0]
    d=similarity[mi]
    ml=sorted(list(enumerate(d)),reverse=True,key=lambda x:x[1])[1:6]
    rm=[]
    for i in ml:
        mid=i[0]

        rm.append(movies.iloc[i[0]].title)
    return rm
movies_dict=pickle.load(open('movie_dict.pkl', 'rb'))
movies=pd.DataFrame(movies_dict)
similarity=pickle.load(open('similar.pkl', 'rb'))
st.title('Movie Recommender System')
option=st.selectbox('selection an option',movies['title'].values)
if(st.button('Recommend')):
    rmc=recommend(option)
    for i in rmc:
        st.write(i)
