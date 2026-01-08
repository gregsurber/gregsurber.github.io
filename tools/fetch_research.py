import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
import json
import os
from datetime import datetime, timedelta

# --- Configuration ---
SEARCH_QUERY = 'all:"LLM" OR all:"Large Language Model" AND all:"ICS" OR all:"SCADA" OR all:"Industrial Control"'
MAX_RESULTS = 20

# --- FIX: ROBUST PATHING ---
# 1. Get the absolute path to the folder containing this script (e.g., /Users/greg/site/tools)
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# 2. Go up one level to the Project Root, then into _data
# Result: /Users/greg/site/_data
DATA_DIR = os.path.join(SCRIPT_DIR, "..", "_data")

OUTPUT_FILENAME = "kinetic_feed.json"

def fetch_arxiv_papers():
    """Queries arXiv and returns a list of dictionaries."""
    
    encoded_query = urllib.parse.quote(SEARCH_QUERY)
    base_url = "http://export.arxiv.org/api/query?"
    url = f"{base_url}search_query={encoded_query}&start=0&max_results={MAX_RESULTS}&sortBy=submittedDate&sortOrder=descending"

    print(f"[*] Querying arXiv...")
    
    try:
        response = urllib.request.urlopen(url)
        data = response.read().decode('utf-8')
        root = ET.fromstring(data)
        ns = {'atom': 'http://www.w3.org/2005/Atom'}
        
        extracted_papers = []

        for entry in root.findall('atom:entry', ns):
            paper_id = entry.find('atom:id', ns).text
            title = entry.find('atom:title', ns).text.replace('\n', ' ').strip()
            summary = entry.find('atom:summary', ns).text.replace('\n', ' ').strip()
            published = entry.find('atom:published', ns).text
            link = entry.find('atom:id', ns).text
            authors = [author.find('atom:name', ns).text for author in entry.findall('atom:author', ns)]
            
            paper_data = {
                "id": paper_id,
                "title": title,
                "authors": authors,
                "summary": summary,
                "link": link,
                "date": published[:10],
                "fetched_at": datetime.now().strftime("%Y-%m-%d")
            }
            extracted_papers.append(paper_data)
            
        return extracted_papers

    except Exception as e:
        print(f"[!] Error fetching data: {e}")
        return []

def update_json_feed(new_papers):
    """Updates the local JSON file, avoiding duplicates."""
    
    # Ensure root _data directory exists
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
        print(f"[*] Created directory: {DATA_DIR}")

    filepath = os.path.join(DATA_DIR, OUTPUT_FILENAME)
    print(f"[*] Target File: {filepath}") # Debug print to confirm location
    
    existing_papers = []
    if os.path.exists(filepath):
        try:
            with open(filepath, 'r') as f:
                existing_papers = json.load(f)
        except json.JSONDecodeError:
            print("[!] Warning: Could not decode existing JSON. Starting fresh.")
            existing_papers = []

    existing_ids = {p['id'] for p in existing_papers}
    added_count = 0
    
    for paper in reversed(new_papers):
        if paper['id'] not in existing_ids:
            existing_papers.insert(0, paper)
            added_count += 1
            existing_ids.add(paper['id'])

    with open(filepath, 'w') as f:
        json.dump(existing_papers, f, indent=2)
        
    print(f"[*] Success. Added {added_count} new papers.")
    print(f"[*] Total papers: {len(existing_papers)}")

if __name__ == "__main__":
    papers = fetch_arxiv_papers()
    if papers:
        update_json_feed(papers)
    else:
        print("[-] No papers found or error occurred.")
