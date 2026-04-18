from groq import Groq
from config import GROQ_API_KEY, GROQ_MODEL

client = Groq(api_key=GROQ_API_KEY)

def classify_intent(query):
    prompt = f"""You are a query classifier for a document QA system. The documents are about policy reports, news articles, stakeholder memos, and technical briefs.

Classify the query into exactly one category:
- FACTUAL: simple question answerable from the documents
- COMPLEX: requires combining multiple pieces from the documents  
- OUT_OF_SCOPE: completely unrelated to policy, news, stakeholders, or technical topics

Query: {query}

Reply with only one word: FACTUAL, COMPLEX, or OUT_OF_SCOPE."""
    response = client.chat.completions.create(
        model=GROQ_MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )
    intent = response.choices[0].message.content.strip().upper()
    if intent not in ["FACTUAL", "COMPLEX", "OUT_OF_SCOPE"]:
        intent = "COMPLEX"
    return intent