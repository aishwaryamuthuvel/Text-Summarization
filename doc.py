import nltk
import string

class Doc:

    @staticmethod
    def build(content):
        d = Doc(content)
        d.prepare()
        return d

    def __init__(self, doc_content):
        self.doc_content = doc_content

    def prepare(self):
        self._extract_sentences()
        self._tokenise_sentences()

    def _extract_sentences(self):
        content = self.doc_content.replace("\n",".\n",1)
        tokeniser = nltk.tokenize.punkt.PunktSentenceTokenizer()
        self.sentences = tokeniser.sentences_from_text(content)

    def _tokenise_sentences(self):
        self.tokenised_sentences = [nltk.word_tokenize(s.casefold()) for s in self.sentences]

    def strip_punctuation(self):
        new_sentences = []
        for ts in self.tokenised_sentences:
            new_tokens = [t for t in ts if t not in string.punctuation]
            new_sentences.append(new_tokens)
        self.tokenised_sentences = new_sentences


    def strip_common_words(self):
        new_sentences = []
        for ts in self.tokenised_sentences:
            new_tokens = [t for t in ts if t not in self._common_words()]
            new_sentences.append(new_tokens)
        self.tokenised_sentences = new_sentences

    def _common_words(self):
        return ['and', 'or', 'the', 'a', 'an']
