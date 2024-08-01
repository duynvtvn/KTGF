# data_class.py
class SpanPrediction:
    def __init__(self, predicted_answer, score, relevance_score, passage_idx, span_text):
        self.predicted_answer = predicted_answer
        self.score = score
        self.relevance_score = relevance_score
        self.passage_idx = passage_idx
        self.span_text = span_text

    def __repr__(self):
        return f"SpanPrediction(answer={self.predicted_answer}, score={self.score}, relevance={self.relevance_score}, passage_idx={self.passage_idx}, span_text={self.span_text})"
