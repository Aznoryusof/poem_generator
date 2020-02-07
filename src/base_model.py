from fastai import *
from fastai.text import *
#from pathlib import Path
import pandas as pd
import numpy as np
#import re

class Base_Model:
    """
    This model takes in 2 arguments:
        learning_rate (float)
        cycles (int)
    """

    def __init__(self, category='life_death', max_words=5500, data_size_base=500, learning_rate_base=1e-3, cycles_base=20,
                 data_size_cat=500, learning_rate_cat=1e-3, cycles_cat=10):
        self.category = category
        self.max_words = max_words
        self.data_size_base = data_size_base
        self.learning_rate_base = learning_rate_base
        self.cycles_base = cycles_base
        self.data_size_cat = data_size_cat
        self.learning_rate_cat = learning_rate_cat
        self.cycles_cat = cycles_cat

    def run(self): 
        """
        This is a NLP model using transfer learning from UMLFit to runm the base model.
        Output: Base model
        """
        ######################
        ## Train Base Model ##
        ######################

        #import data
        train = pd.read_csv('./data/for_training/data_others.csv')
        train = pd.DataFrame(train['Poem'])
        train = train.sample(n=self.data_size_base)
        print ("Data ready for modelling")

        #transfer learning from UMLFit
        train_size, ncols = train.shape
        data_lm = TextLMDataBunch.from_df('.', train.iloc[:train_size], train.iloc[train_size:], text_cols=['Poem'], min_freq=1, max_vocab=self.max_words)
        print ("Language model saved (base)")
        
        #run the language_model_learner class
        learn = language_model_learner(data_lm, AWD_LSTM, drop_mult=0.7)
        print ("Run one epoch with lower layers (base)")
        learn.fit_one_cycle(cyc_len=1, max_lr=self.learning_rate_base, moms=(0.8, 0.7))
        print ("Run for many epochs with all layers unfrozen (base)")
        learn.unfreeze() 
        learn.fit_one_cycle(cyc_len=self.cycles_base, max_lr=self.learning_rate_base, moms=(0.8, 0.7))
        learn.save_encoder('ft_enc_base')
        print ("Encoder saved")

        #test
        TEXT = "In the hot blazing sun"
        N_WORDS = 200
        poem_base = (learn.predict(TEXT, N_WORDS, temperature = 0.7))
        print (poem_base)
        print ("Base Model Trained!")

        ##########################  
        ## Train Category Model ##
        ##########################

        #import data
        path = './data/for_training/data_' + self.category + '.csv'
        topic = pd.read_csv(path)
        topic = pd.DataFrame(topic['Poem'])
        rows = min(self.data_size_cat, len(topic))
        topic = topic.sample(n=rows)
        print ("Data ready for modelling (cat)")

        #transfer learning/reset vocab
        topic_size, ncols = topic.shape
        data_lm = TextLMDataBunch.from_df('.', topic.iloc[:topic_size], topic.iloc[topic_size:], text_cols=['Poem'], min_freq=1, max_vocab=self.max_words)
        path = 'models/lm_databunch_' + self.category
        data_lm.save(path)
        print ("Category language model saved (cat)")

        #run the language_model_learner class for category
        learn = language_model_learner(data_lm, AWD_LSTM, drop_mult=0.7)
        learn.load_encoder('ft_enc_base')
        learn.freeze()
        print ("Run one epoch with lower layers (cat)")
        learn.fit_one_cycle(cyc_len=1, max_lr=self.learning_rate_cat, moms=(0.8, 0.7))
        learn.unfreeze()
        print ("Run for many epochs with all layers unfrozen (cat)")
        learn.fit_one_cycle(cyc_len=self.cycles_cat, max_lr=self.learning_rate_cat, moms=(0.8, 0.7))
        path = 'ft_enc_' + self.category
        learn.save_encoder(path)
        print ("Encoder saved")

        #test
        TEXT = "In the hot blazing sun"
        N_WORDS = 200
        poem_cat = (learn.predict(TEXT, N_WORDS, temperature = 0.7))
        print (poem_cat)
        print ("Cat Model Trained!")

        #return (poem_cat)


