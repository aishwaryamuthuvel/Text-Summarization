import numpy as np
import gensim
from nltk.corpus import brown
from nltk.corpus import reuters
from pathlib import Path

class Word2VecModel:
    @staticmethod
    def build_brown_model():
        brown_file = Path('./brown_word2vec.model')
        if brown_file.is_file():
            model = gensim.models.Word2Vec.load('./brown_word2vec.model')
        else:
            corpus = brown.sents()
            model = gensim.models.Word2Vec(corpus)
            model.save('./brown_word2vec.model')
        return model

    def build_reuters_model():
        brown_file = Path('./reuters_word2vec.model')
        if brown_file.is_file():
            model = gensim.models.Word2Vec.load('./reuters_word2vec.model')
        else:
            corpus = brown.sents()
            model = gensim.models.Word2Vec(corpus)
            model.save('./reuters_word2vec.model')
        return model

class Word2VecDoc:

    @staticmethod
    def build(model, doc, verbose=False):
        word2vec_doc = Word2VecDoc(model, doc, verbose)
        word2vec_doc.build_doc_vector()
        return word2vec_doc

    def __init__(self, wv_model, doc_content, verbose):
        self.wv_model = wv_model
        self.doc_content = doc_content
        self.verbose = verbose

    def similarity(self, tokenised_sentence):
        s_vector, _s_count = self._build_sentence_vector(tokenised_sentence)
        s = gensim.models.KeyedVectors.cosine_similarities(self.doc_vector,[s_vector])[0]
        return s

    def similar_to(self, ref_doc_vector):
        s = gensim.models.KeyedVectors.cosine_similarities(self.doc_vector,[ref_doc_vector])[0]
        return s

    def build_doc_vector(self):
        # sum up doc vectors
        # calc doc vector - average of all words
        self.doc_vector = np.zeros(self._vector_len())
        word_count = 0
        for s in self.doc_content.tokenised_sentences:
            s_vector, s_count = self._build_sentence_vector(s)

            self.doc_vector += (s_vector * s_count)
            word_count += s_count

        self.doc_vector = self.doc_vector / word_count

    def _build_sentence_vector(self, tokenised_sentence):
        s_vector = np.zeros(self._vector_len())
        s_count = 0
        for t in tokenised_sentence:
            try:
                current_vec = self.wv_model.wv[t]
                s_vector += current_vec
                s_count += 1
            except KeyError:
                if self.verbose:
                    print("Skipping", t)

        s_vector = s_vector / s_count

        return s_vector, s_count

    def _vector_len(self):
        return len(self.wv_model.wv['and'])

