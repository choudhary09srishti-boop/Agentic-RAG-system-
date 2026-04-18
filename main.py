from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from agent.router import classify_intent
from agent.retriever import retrieve
from agent.generator import generate_answer, reject_query
from evaluation.metrics import evaluate

console = Console()

def run_pipeline(query, reference=None):
    console.print(Panel(f"[bold cyan]Query:[/bold cyan] {query}", style="cyan"))

    # AGENT DECISION
    intent, method = classify_intent(query)
    console.print(f"[yellow]⚡ Agent Decision:[/yellow] {intent} [dim]({method})[/dim]")

    # AGENT ACTION
    if intent == "OUT_OF_SCOPE":
        answer = reject_query()
    elif intent == "FACTUAL":
        chunks = retrieve(query, top_k=3)
        console.print(f"[blue]📄 Chunks retrieved:[/blue] {len(chunks)}")
        answer = generate_answer(query, chunks)
    elif intent == "COMPLEX":
        chunks = retrieve(query, top_k=7)
        console.print(f"[blue]📄 Chunks retrieved:[/blue] {len(chunks)}")
        answer = generate_answer(query, chunks)

    console.print(Panel(f"[bold green]Answer:[/bold green] {answer}", style="green"))

    # AGENT SELF-EVALUATION
    if reference:
        scores = evaluate(answer, reference)
        table = Table(title="Self-Evaluation")
        table.add_column("Metric")
        table.add_column("Score")
        table.add_row("Cosine Similarity", str(scores["cosine_similarity"]))
        table.add_row("ROUGE-1", str(scores["rouge1"]))
        table.add_row("ROUGE-L", str(scores["rougeL"]))
        verdict = scores["verdict"]
        color = "green" if verdict == "PASS" else "red"
        table.add_row("Verdict", f"[{color}]{verdict}[/{color}]")
        console.print(table)

    return answer

if __name__ == "__main__":
    while True:
        query = input("\nEnter your query (or 'exit'): ")
        if query.lower() == "exit":
            break
        reference = input("Enter reference answer (or press Enter to skip): ")
        run_pipeline(query, reference if reference else None)