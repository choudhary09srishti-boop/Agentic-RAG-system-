import csv
from rich.console import Console
from rich.table import Table
from evaluation.metrics import evaluate
from evaluation.test_questions import test_cases
from agent.router import classify_intent
from agent.retriever import retrieve
from agent.generator import generate_answer, reject_query

console = Console()

def run_evaluation():
    table = Table(title="Evaluation Results")
    table.add_column("Query", style="cyan", max_width=30)
    table.add_column("Expected", style="white")
    table.add_column("Got", style="white")
    table.add_column("Routing", style="white")
    table.add_column("Cosine", style="white")
    table.add_column("ROUGE-L", style="white")
    table.add_column("Verdict", style="white")

    total, passed, routing_correct = 0, 0, 0
    csv_rows = []

    for case in test_cases:
        query = case["query"]
        reference = case["reference"]
        expected_intent = case["expected_intent"]

        intent, method = classify_intent(query)
        routing_ok = intent == expected_intent

        if intent == "OUT_OF_SCOPE":
            answer = reject_query()
        elif intent == "FACTUAL":
            chunks = retrieve(query, top_k=3)
            answer = generate_answer(query, chunks)
        else:
            chunks = retrieve(query, top_k=7)
            answer = generate_answer(query, chunks)

        scores = evaluate(answer, reference)
        verdict = scores["verdict"]
        routing_label = "✅" if routing_ok else "❌"
        verdict_color = "green" if verdict == "PASS" else "red"

        table.add_row(
            query[:40],
            expected_intent,
            intent,
            routing_label,
            str(scores["cosine_similarity"]),
            str(scores["rougeL"]),
            f"[{verdict_color}]{verdict}[/{verdict_color}]"
        )

        if routing_ok:
            routing_correct += 1
        if verdict == "PASS":
            passed += 1
        total += 1

        csv_rows.append({
            "query": query,
            "expected_intent": expected_intent,
            "predicted_intent": intent,
            "routing_correct": routing_ok,
            "cosine_similarity": scores["cosine_similarity"],
            "rouge1": scores["rouge1"],
            "rougeL": scores["rougeL"],
            "verdict": verdict
        })

    console.print(table)
    console.print(f"\n[bold]Total: {total} | Passed: {passed} | Failed: {total-passed}[/bold]")
    console.print(f"[bold]Routing Accuracy: {routing_correct}/{total}[/bold]")

    with open("evaluation/results.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=csv_rows[0].keys())
        writer.writeheader()
        writer.writerows(csv_rows)
    console.print("[green]Results saved to evaluation/results.csv[/green]")

if __name__ == "__main__":
    run_evaluation()
    