import unittest
from doc import Doc

class DocTest(unittest.TestCase):
    def test_empty(self):
        content = ''
        doc = Doc.build(content)

        self.assertEqual(len(doc.sentences), 0)
        self.assertEqual(len(doc.tokenised_sentences), 0)


    def test_one_sentence(self):
        content = 'one sentence.'
        doc = Doc.build(content)

        self.assertEqual(len(doc.sentences), 1)
        self.assertEqual(len(doc.tokenised_sentences), 1)
        self.assertEqual(len(doc.tokenised_sentences[0]), 3)

    def test_multi_sentence(self):
        content = 'one sentence. two sentence. an even longer sentence.'
        doc = Doc.build(content)

        self.assertEqual(len(doc.sentences), 3)

        self.assertEqual(len(doc.tokenised_sentences), 3)
        self.assertEqual(len(doc.tokenised_sentences[2]), 5)


    def test_sentence_content(self):
        content = 'one sentence. two sentence. an even longer sentence.'
        doc = Doc.build(content)

        self.assertEqual(doc.sentences[2], 'an even longer sentence.')
        self.assertEqual(doc.tokenised_sentences[2], ['an','even','longer','sentence', '.'])

    def test_strip_punctuation(self):
        content = 'one clause, two sentence. an even longer sentence.'
        doc = Doc.build(content)
        doc.strip_punctuation()

        self.assertEqual(doc.sentences[0], 'one clause, two sentence.')
        self.assertEqual(doc.tokenised_sentences[0], ['one','clause','two','sentence'])

    def test_strip_common_words(self):
        content = 'one clause and two sentence or an even longer sentence.'
        doc = Doc.build(content)
        doc.strip_common_words()

        self.assertEqual(doc.sentences[0], 'one clause and two sentence or an even longer sentence.')
        self.assertEqual(doc.tokenised_sentences[0], ['one','clause','two','sentence','even','longer','sentence','.'])

    def test_strip(self):
        content = 'one clause, two sentences or a longer sentence.'
        doc = Doc.build(content)
        doc.strip_common_words()
        doc.strip_punctuation()

        self.assertEqual(doc.sentences[0], 'one clause, two sentences or a longer sentence.')
        self.assertEqual(doc.tokenised_sentences[0], ['one','clause','two','sentences','longer','sentence'])

if __name__ == '__main__':
    unittest.main()
