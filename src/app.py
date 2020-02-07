# https://towardsdatascience.com/how-to-write-web-apps-using-simple-python-for-data-scientists-a227a1a01582

from gtts import gTTS
from fastai.text import *
import streamlit as st
import pandas as pd
import os

abs_path = os.path.abspath(os.path.dirname(__file__))
parent_path = os.path.dirname(abs_path)

"""
# THE GHOST WRITER
### Poet Companion Bot
Enter any text and let me compose something for you!
"""

Genre_option = pd.DataFrame({
    'Genre': ['Life', 'Love', 'Nature', 'Social']})

chosen = st.sidebar.selectbox(
    'Which genre do you want to compose?',
    Genre_option['Genre'])


data_path = os.path.join(os.path.dirname(abs_path), "data/")

chosen_databunch = 'lm_databunch_{}'.format(chosen)

data_lm = load_data(data_path, chosen_databunch, bs=192)

learn = language_model_learner(data_lm, AWD_LSTM, drop_mult=0.5)

model_path = os.path.join(parent_path, "model/",
                          "ft_enc_{}".format(chosen))

learn.load_encoder(model_path)

N_WORDS = st.slider('Number of Words', 1, 200, 100)
slider_input = st.slider('Bot Creativity Level', 1, 10, 4)
temperature = slider_input/10*1
text_input = st.text_input('Enter text...', ('a new song I sing'))

poem = learn.predict(text_input, int(N_WORDS), temperature=temperature)

"""
# Here's your poem!
"""
poem
"""
## This section loads the learner classifier, and classifies the generated poem
"""
if st.button('Classify!'):
    learn_clf_load = load_learner(parent_path, file = 'export_clf.pkl')
    result = learn_clf_load.predict(poem)[0]
    result
