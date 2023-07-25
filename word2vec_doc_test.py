import unittest
from word2vec_doc import *
from doc import *

class Word2VecDocTest(unittest.TestCase):
    def wv_model(self):
        if not hasattr(Word2VecDocTest, 'wvm'):
            print("building model...")
            Word2VecDocTest.wvm = Word2VecModel.build_brown_model()
            print("model built.")
        return Word2VecDocTest.wvm

    def test_empty(self):
        content = Doc.build('')
        d = Word2VecDoc.build(self.wv_model(), content)

        self.assertEqual(len(d.doc_vector), 100)


    def test_one_sentence(self):
        content = Doc.build('one sentence')
        d = Word2VecDoc.build(self.wv_model(), content)

        self.assertEqual(round(d.similarity(['one','sentence']),5), 1)

    def test_multi_sentence(self):
        content = Doc.build('one sentence. two sentence. an even longer sentence.')
        d = Word2VecDoc.build(self.wv_model(), content)

        self.assertEqual(round(d.similarity(['one','sentence']),5), 0.70674)


    def test_similar_to(self):
        content1 = Doc.build('one sentence. two sentence. an even longer sentence.')
        d1 = Word2VecDoc.build(self.wv_model(), content1)

        content2 = Doc.build('one sentence. another different thing. an even longer sentence.')
        d2 = Word2VecDoc.build(self.wv_model(), content2)

        self.assertEqual(round(d1.similar_to(d2.doc_vector),5), 0.96918)
        self.assertEqual(round(d2.similar_to(d1.doc_vector),5), 0.96918)


if __name__ == '__main__':
    unittest.main()

