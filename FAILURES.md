# Failure Analysis

## Failure 1: Low Cosine Score on FLOPs Threshold Query
**Query:** What FLOPs threshold defines a frontier AI model in the US?
**Root Cause:** The documents mention FLOPs indirectly. The chunk retrieved does not contain the exact numeric value, causing a weak semantic match with the reference answer.
**Fix:** Smaller chunk size (100-150 words) would keep numeric facts together and improve retrieval precision.

## Failure 2: China vs EU Comparison — Partial Answer
**Query:** How does China's approach to generative AI differ from the EU's approach?
**Root Cause:** Information about China and EU exists in separate documents. The retriever fetches chunks from one document more than the other, causing an incomplete synthesis.
**Fix:** Implement MMR (Maximal Marginal Relevance) retrieval to enforce diversity across source documents.

## Failure 3: Routing Edge Case — Financial Impact Query
**Query:** Which companies are most affected financially by the EU AI Act?
**Root Cause:** The rule-based router initially missed this as OUT_OF_SCOPE because it lacked financial keywords. Pure keyword matching has coverage gaps for paraphrased out-of-scope queries.
**Fix:** Add a semantic similarity check against a set of known in-scope topics before falling back to LLM classification.

## What Would Be Done Differently
- Smaller, overlapping chunks for fact-dense documents
- MMR retrieval for synthesis queries
- Hybrid router: keyword rules + embedding similarity + LLM fallback