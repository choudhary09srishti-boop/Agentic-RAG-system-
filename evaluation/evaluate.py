from rich.console import Console
from rich.table import Table
from evaluation.metrics import evaluate
from evaluation.test_questions import test_cases
from main import run_pipeline

console = Console()

def run_evaluation():
    table = Table(title="Evaluation Results")
    table.add_column("Query", style="cyan", max_width=30)
    table.add_column("Cosine", style="white")
    table.add_column("ROUGE-1", style="white")
    table.add_column("ROUGE-L", style="white")
    table.add_column("Verdict", style="white")

    total, passed = 0, 0

    for case in test_cases:
        generated = run_pipeline(case["query"])
        scores = evaluate(generated, case["reference"])
        verdict_color = "green" if scores["verdict"] == "PASS" else "red"
        table.add_row(
            case["query"][:50],
            str(scores["cosine_similarity"]),
            str(scores["rouge1"]),
            str(scores["rougeL"]),
            f"[{verdict_color}]{scores['verdict']}[/{verdict_color}]"
        )
        total += 1
        if scores["verdict"] == "PASS":
            passed += 1

    console.print(table)
    console.print(f"\n[bold]Total: {total} | Passed: {passed} | Failed: {total - passed}[/bold]")

if __name__ == "__main__":
    run_evaluation()