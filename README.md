# Text-Summarization

This is an effort to build an extractive text summarization algorithm. The aim of the project is to create a concise and relevant summary given a long text. The challenge lies in discarding all the irrelevant information and retaining only the most important information to create the perfect gist of the given source text. 

## Data
We obtained our dataset from Kaggle - the BBC News Summary dataset found [here](https://www.kaggle.com/pariza/bbc-news-summary). This dataset contains 2225 news articles categorised into business, sports, technology, entertainment and politics. We separated this data randomly into training, validation and test sets with an 80-10-10 percentage split. We used our training data along with NLTK Brown and NLTK Reuters corpora to train the Word2Vec model we used.

## Method
Below is a flowchart outlining how to create a text summary.

![alt text](https://github.com/aishwaryamuthuvel/Text-Summarization/blob/main/Method_flowchart.jpg?raw=true)




###


