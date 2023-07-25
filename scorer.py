# needs "pip install rouge"
from rouge import Rouge

class Scorer:
    def __init__(self):
        self.scores = []
        self.total = self._blank_score()

    def add(self, generated, reference, cosine):
        rouge = Rouge()
        score = rouge.get_scores(generated, reference, avg=True)
        score['cosine'] = cosine

        self.scores.append(score)
        self._update_total(score)

    def averages(self):
        avg = self.total
        count = len(self.scores)

        avg['rouge-1']['f'] /= count
        avg['rouge-1']['r'] /= count
        avg['rouge-1']['p'] /= count
        avg['rouge-2']['f'] /= count
        avg['rouge-2']['r'] /= count
        avg['rouge-2']['p'] /= count
        avg['rouge-l']['f'] /= count
        avg['rouge-l']['r'] /= count
        avg['rouge-l']['p'] /= count
        avg['cosine'] /= count

        return avg

    def _blank_score(self):
        return {
            'rouge-1': {'f': 0, 'p': 0, 'r': 0},
            'rouge-2': {'f': 0, 'p': 0, 'r': 0},
            'rouge-l': {'f': 0, 'p': 0, 'r': 0},
            'cosine': 0
        }

    def _update_total(self, score):
        self.total['rouge-1']['f'] += score['rouge-1']['f']
        self.total['rouge-1']['r'] += score['rouge-1']['r']
        self.total['rouge-1']['p'] += score['rouge-1']['p']
        self.total['rouge-2']['f'] += score['rouge-2']['f']
        self.total['rouge-2']['r'] += score['rouge-2']['r']
        self.total['rouge-2']['p'] += score['rouge-2']['p']
        self.total['rouge-l']['f'] += score['rouge-l']['f']
        self.total['rouge-l']['r'] += score['rouge-l']['r']
        self.total['rouge-l']['p'] += score['rouge-l']['p']
        self.total['cosine'] += score['cosine']
