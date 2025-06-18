import requests
import os
import json
from time import sleep
from tqdm import tqdm

BASE_URL = "https://discourse.onlinedegree.iitm.ac.in"
CATEGORY_ID = 34  # TDS Knowledge Base category
OUTPUT_DIR = "downloaded_threads"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def get_topics(category_id):
    topics = []
    page = 0
    while True:
        url = f"{BASE_URL}/c/courses/tds-kb/{category_id}.json?page={page}"
        headers = {"User-Agent": "Mozilla/5.0"}
        resp = requests.get(url, headers=headers)
        if resp.status_code != 200:
            break
        data = resp.json()
        topic_list = data.get("topic_list", {}).get("topics", [])
        if not topic_list:
            break
        topics.extend(topic_list)
        page += 1
        sleep(1)  # Respectful crawling
    return topics

def download_topic(topic_id, slug):
    url = f"{BASE_URL}/t/{slug}/{topic_id}.json"
    resp = requests.get(url)
    if resp.status_code == 200:
        data = resp.json()
        file_path = os.path.join(OUTPUT_DIR, f"{slug}_{topic_id}.json")
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
        return True
    return False

if __name__ == "__main__":
    topics = get_topics(CATEGORY_ID)
    print(f"Found {len(topics)} topics.")
    for topic in tqdm(topics, desc="Downloading threads"):
        topic_id = topic["id"]
        slug = topic["slug"]
        download_topic(topic_id, slug)
        sleep(0.5)
