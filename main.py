from rich.console import Console
from rich.panel import Panel
from agent.router import classify_intent
from agent.retriever import retrieve
from agent.generator import generate_answer, reject_query

console = Console()

def run_pipeline(query):
    console.print(Panel(f"[bold]Query:[/bold] {query}", style="blue"))
    
    intent = classify_intent(query)
    console.print(f"[yellow]Intent detected:[/yellow] {intent}")
    
    if intent == "OUT_OF_SCOPE":
        answer = reject_query()
    elif intent == "FACTUAL":
        chunks = retrieve(query, top_k=3)
        answer = generate_answer(query, chunks)
    elif intent == "COMPLEX":
        chunks = retrieve(query, top_k=7)
        answer = generate_answer(query, chunks)
    
    console.print(Panel(f"[bold]Answer:[/bold] {answer}", style="green"))
    return answer

if __name__ == "__main__":
    while True:
        query = input("\nEnter your query (or 'exit'): ")
        if query.lower() == "exit":
            break
        run_pipeline(query)