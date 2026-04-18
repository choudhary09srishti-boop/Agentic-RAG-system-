import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from rouge_score import rouge_scorer

nltk.download('punkt', quiet=True)

def cosine_sim(generated, reference):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([generated, reference])
    score = cosine_similarity(vectors[0], vectors[1])[0][0]
    return round(float(score), 4)

def rouge_scores(generated, reference):
    scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)
    scores = scorer.score(reference, generated)
    return {
        "rouge1": round(scores['rouge1'].fmeasure, 4),
        "rouge2": round(scores['rouge2'].fmeasure, 4),
        "rougeL": round(scores['rougeL'].fmeasure, 4)
    }

def evaluate(generated, reference):
    cosine = cosine_sim(generated, reference)
    rouge = rouge_scores(generated, reference)
    verdict = "PASS" if cosine >= 0.3 else "FAIL"
    return {
        "cosine_similarity": cosine,
        **rouge,
        "verdict": verdict
    }