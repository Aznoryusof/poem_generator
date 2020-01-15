# Poem Generator
An exploration to 'Artificial Creativity', using LSTM and transfer learning to create a poem-generating machine. 

By Arvin, Aznor, Ganesh and Michelle for `Week/Assignment 8:` End-to-end Project.


## Installation
Firstly, clone the repository to a folder of your choice. 

The project has been dockerised to simplify testing and deployment on local machine. 
Simply navigate to the project folder and run the buildfile provided.

```bash
bash build.sh
```

## Usage
1. Choose the poem genre.
2. Input the number of words you want in the generated poem.
3. Input the starting line of the poem.
4. Choose how 'creative' you want the model to be. 
A number closer to 0 will create a less creative poem with more repetitions. 

## Project Objective
Use Machine Learning and Natural Language Programming techniques to generate English poems across four different topics. Users will input the starting word of phrases to the poem and the number of words desired. A poem will be generated as the output. Output will pass through a classifier to validate if the poem is topical. 

## Data Source
[Kaggle Poetry Foundation Poems](https://www.kaggle.com/tgdivy/poetry-foundation-poems/version/1)

## Methodology
- __Step 1: Data Cleaning__ `EDA.ipynb`
Data cleaning includes removing double/leading/trailing spaces and categorising the poems into four different topics.
-  __Step 2: Text Generation__ `src/base_model.py`
Apply transfer learning on fastai's pre-trained model UMLfit to generate poems. A two-layered approach was implemented. First, the text generator was first trained on 'other' poems and then on the topic-specific poems.
- __Step 3: Poem Classification__
To validate whether the text generator was able to output a topical poem, a classifier was trained on a separate set of topical poems. The classifier takes the generated text as an input.
- __Step 4: API and UI__ `src/app.py`
Create a user-friendly webpage for users to interact with the model. Usage of the UI is explained above.

## Model Architecture
![Model Architecture](http://gitlab.int.aisingapore.org/aiap/aiap4/team1-project/blob/team1_michelle/Architecture_diagram.PNG)

## Resources 
The following resources were referenced to implement this project:
- Fast ai: [A Code-First Introduction to NLP](https://www.youtube.com/watch?v=PNNHaQUQqW8&list=PLtmWHNX-gukKocXQOkQjuVxglSDYWsSh9&index=8)
- [Generating Topical Poetry](https://www.isi.edu/natural-language/mt/generating-topical-poetry.pdf)

# Further Exploration
- Generative Adversarial Networks (GANs): Integrate Discriminator and Generator into topic classification
- Poem or Not-A-Poem: word-stress, rhymes

# Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.testrun.org
