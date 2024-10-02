import streamlit as st
import pickle
import re
import nltk

nltk.download('punkt')
nltk.download('stopwords')

#loading models
clf = pickle.load(open(r'clf.pkl', 'rb'))
tfidfd = pickle.load(open(r'tfidf.pkl', 'rb'))


st.title("Resume Screening App")