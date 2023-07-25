# Text-Summarization

This is an effort to build an extractive text summarization algorithm.

## Data
We obtained our dataset from Kaggle - the BBC News Summary dataset found [here](https://www.kaggle.com/pariza/bbc-news-summary). This dataset contains 2225 news articles categorised into business, sports, technology, entertainment and politics. We separated this data randomly into training, validation and test sets with a 80-10-10 percentage split. We used our training data along with NLTK Brown and NLTK Reuters corpora to train the Word2Vec model we used.

