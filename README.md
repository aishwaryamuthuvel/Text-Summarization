# Text-Summarization

This is an effort to build an extractive text summarization algorithm. The aim of the project is to create a concise and relevant summary given a long text. The challenge lies in discarding all the irrelevant information and retaining only the most important information to create the perfect gist of the given source text. 

## Data
We obtained our dataset from Kaggle - the BBC News Summary dataset found [here](https://www.kaggle.com/pariza/bbc-news-summary). This dataset contains 2225 news articles categorised into business, sports, technology, entertainment and politics. We separated this data randomly into training, validation and test sets with an 80-10-10 percentage split. We used our training data along with NLTK Brown and NLTK Reuters corpora to train the Word2Vec model we used.

## Method
Below is a flowchart outlining how to create a text summary.

![alt text](https://github.com/aishwaryamuthuvel/Text-Summarization/blob/main/Method_flowchart.png?raw=true)

### Pre-processing and Feature Extraction 
As pre-processing steps, the text was downcased and then tokenized into sentences and words. Below are the features extracted for model training.

#### Cosine Similarity
This feature is calculated for each sentence in the text. It gives a measure of how closely a sentence in the given text is associated with the text. We use a Word2Vec model to evaluate the text_vector and the sentence_vector and then we calculate the cosine similarity between both the vectors to arrive at the cosine similarity of the sentence. The Word2Vec model needs a corpus to train on. We created a corpus by combining our training corpus along with the NLTK Brown and NLTK Reuters corpora to train the Word2Vec model.




