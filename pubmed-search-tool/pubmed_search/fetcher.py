import requests
from Bio import Entrez

Entrez.email = "test@example.com"  # Replace with your real email

def fetch_pubmed(query, max_results=10):
    handle = Entrez.esearch(db="pubmed", term=query, retmax=max_results)
    record = Entrez.read(handle)
    id_list = record["IdList"]

    papers = []
    for pubmed_id in id_list:
        fetch = Entrez.efetch(db="pubmed", id=pubmed_id, rettype="medline", retmode="text")
        papers.append(fetch.read())

    return papers
