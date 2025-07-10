import typer
from pubmed_search.fetcher import fetch_pubmed
from pubmed_search.filters import is_non_academic
from pubmed_search.utils import save_to_csv

app = typer.Typer()

@app.command()
def get_papers_list(query: str, file: str = "output.csv"):
    print(f"Searching PubMed for: {query}")
    raw_data = fetch_pubmed(query)

    filtered = []
    for entry in raw_data:
        if is_non_academic(entry):
            filtered.append({"entry": entry})

    save_to_csv(filtered, file)

if __name__ == "__main__":
    app()  # ✅ run the Typer app
