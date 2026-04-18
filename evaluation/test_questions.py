test_cases = [
    # FACTUAL (5)
    {
        "query": "What are the four risk categories defined in the EU AI Act?",
        "reference": "The EU AI Act defines four risk categories: unacceptable risk, high risk, limited risk, and minimal risk.",
        "expected_intent": "FACTUAL"
    },
    {
        "query": "What is the maximum penalty under the EU AI Act?",
        "reference": "The maximum penalty under the EU AI Act is 35 million euros or 7% of global annual turnover.",
        "expected_intent": "FACTUAL"
    },
    {
        "query": "What FLOPs threshold defines a frontier AI model in the US?",
        "reference": "The US Executive Order defines frontier AI models as those trained using more than 10^26 floating point operations.",
        "expected_intent": "FACTUAL"
    },
    {
        "query": "Name one prohibited AI system under the EU AI Act.",
        "reference": "Social scoring systems by governments are prohibited under the EU AI Act.",
        "expected_intent": "FACTUAL"
    },
    {
        "query": "When will the EU AI Act be fully enforced?",
        "reference": "The EU AI Act will be fully enforced by 2026.",
        "expected_intent": "FACTUAL"
    },
    # COMPLEX (5)
    {
        "query": "How does the EU AI Act differ from the US approach to AI regulation?",
        "reference": "The EU AI Act takes a risk-based legislative approach with strict penalties while the US favors voluntary guidelines and sector-specific oversight without a unified federal law.",
        "expected_intent": "COMPLEX"
    },
    {
        "query": "Compare penalty structures across the EU and US AI regulations.",
        "reference": "The EU has defined maximum penalties up to 35 million euros while the US does not have a unified federal penalty structure for AI violations.",
        "expected_intent": "COMPLEX"
    },
    {
        "query": "How does China's approach to generative AI differ from the EU's approach?",
        "reference": "China mandates government approval and security assessments before deployment of generative AI, whereas the EU classifies AI by risk level and requires conformity assessments for high-risk systems.",
        "expected_intent": "COMPLEX"
    },
    {
        "query": "What trade-offs exist between innovation and regulation in AI governance?",
        "reference": "Stricter regulation improves safety and accountability but may slow innovation, increase compliance costs, and disadvantage smaller developers compared to large corporations.",
        "expected_intent": "COMPLEX"
    },
    {
        "query": "What are the key similarities across global AI regulatory frameworks?",
        "reference": "All major frameworks emphasize transparency, accountability, risk assessment, and human oversight as core principles of AI governance.",
        "expected_intent": "COMPLEX"
    },
    # OUT OF SCOPE (5)
    {
        "query": "What is India's AI regulation policy?",
        "reference": "This query is outside the scope of the provided documents.",
        "expected_intent": "OUT_OF_SCOPE"
    },
    {
        "query": "What is the carbon footprint of AI systems?",
        "reference": "This query is outside the scope of the provided documents.",
        "expected_intent": "OUT_OF_SCOPE"
    },
    {
        "query": "Which companies are most affected financially by the EU AI Act?",
        "reference": "This query is outside the scope of the provided documents.",
        "expected_intent": "OUT_OF_SCOPE"
    },
    {
        "query": "What is the recipe for pasta?",
        "reference": "This query is outside the scope of the provided documents.",
        "expected_intent": "OUT_OF_SCOPE"
    },
    {
        "query": "How does AI regulation impact stock market performance?",
        "reference": "This query is outside the scope of the provided documents.",
        "expected_intent": "OUT_OF_SCOPE"
    },
]