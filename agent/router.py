from groq import Groq
from config import GROQ_API_KEY, GROQ_MODEL

client = Groq(api_key=GROQ_API_KEY)

# EXPLICIT RULES - inspectable, not a black box
OUT_OF_SCOPE_KEYWORDS = [
    "india", "carbon footprint", "stock market", "salary", "weather",
    "recipe", "sports", "movie", "song", "climate", "cryptocurrency"
    "companies", "financially", "stock market", "profit", "revenue", "affected financially"
]

FACTUAL_KEYWORDS = [
    "what is", "what are", "when", "who", "how many", "define",
    "name one", "what does", "maximum", "minimum", "threshold"
]

COMPLEX_KEYWORDS = [
    "compare", "difference", "similarities", "how does", "why",
    "contrast", "explain", "analyze", "across", "impact", "trade-off"
]

def rule_based_classify(query):
    query_lower = query.lower()
    
    for keyword in OUT_OF_SCOPE_KEYWORDS:
        if keyword in query_lower:
            return "OUT_OF_SCOPE"
    
    for keyword in COMPLEX_KEYWORDS:
        if keyword in query_lower:
            return "COMPLEX"
    
    for keyword in FACTUAL_KEYWORDS:
        if keyword in query_lower:
            return "FACTUAL"
    
    return None  # fallback to LLM

def llm_classify(query):
    prompt = f"""You are a query classifier for a document QA system about AI regulation (EU AI Act, US, China policies).

Classify into exactly one category:
- FACTUAL: simple question with direct answer in documents
- COMPLEX: requires combining multiple pieces of information
- OUT_OF_SCOPE: unrelated to AI regulation policy

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

def classify_intent(query):
    # Step 1: try rule-based first (explicit + inspectable)
    rule_result = rule_based_classify(query)
    if rule_result:
        return rule_result, "rule-based"
    
    # Step 2: LLM fallback
    llm_result = llm_classify(query)
    return llm_result, "llm-fallback"