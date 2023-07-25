# Text-Summarization

This is an effort to build an extractive text summarization algorithm. The aim of the project is to create a concise and relevant summary given a long text. The challenge lies in discarding all the irrelevant information and retaining only the most important information to create the perfect gist of the given source text. 

## Data
We obtained our dataset from Kaggle - the BBC News Summary dataset found [here](https://www.kaggle.com/pariza/bbc-news-summary). This dataset contains 2225 news articles categorised into business, sports, technology, entertainment and politics. We separated this data randomly into training, validation and test sets with an 80-10-10 percentage split. We used our training data along with NLTK Brown and NLTK Reuters corpora to train the Word2Vec model we used.

## Method
Below is a flowchart outlining how to create a text summary.

![Method Flowchart](https://github.com/aishwaryamuthuvel/Text-Summarization/blob/main/Method_flowchart.png?raw=true)

### Pre-processing and Feature Extraction 
As pre-processing steps, the text was downcased and then tokenized into sentences and words. Below are the features extracted for model training.

#### Cosine Similarity
This feature is calculated for each sentence in the text. It gives a measure of how closely a sentence in the given text is associated with the text. We use a Word2Vec model to evaluate the text_vector and the sentence_vector and then we calculate the cosine similarity between both the vectors to arrive at the cosine similarity of the sentence. The Word2Vec model needs a corpus to train on. We created a corpus by combining our training corpus along with the NLTK Brown and NLTK Reuters corpora to train the Word2Vec model.

![Cosine Similarity Flowchart](https://github.com/aishwaryamuthuvel/Text-Summarization/blob/main/Cosine_similarity.png?raw=true)

#### Sentence Position
This feature gives the position of the sentence in the text. We have taken this feature into consideration under the assumption that the sentences of importance appear at earlier positions when compared to the sentences of lesser importance.

#### Length of Sentence
This feature helps choose shorter sentences into the summary instead of long sentences that carry the same measure of importance.

### Machine Learning Model to Rank Sentences
We trained a Logistic Regression model with a sigmoid activation function on our training data. This model calculates a score for each sentence in the input text based on the input features. We could create a summary of a fixed length of characters (1600 characters) using the sentences of maximum 
scores. Else the summary length could be derived from the input text length (half of the input text length). Else a threshold on the sentence score could determine whether the sentence should appear in the summary or not. Below are the results obtained on the validation data using the above-mentioned techniques. Based on the ROUGE values, we concluded that using a threshold on the scores worked best on balancing the recall and precision than the other two suggested methods.

<p align="center">
<img src="https://github.com/aishwaryamuthuvel/Text-Summarization/blob/main/Camparison_summaryCreation.png" width=70% height=70% />
</p>

## Model Performance
We used the model obtained on our test data and obtained the below performance. We used the ROUGE metric to compare the generated summary and 
the reference summary. We got an average **recall of 71%**, a **precision of 62%** and a **cosine similarity of 98%**.








