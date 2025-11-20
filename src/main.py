import os
import pandas as pd
from ai_classifier import AIClassifier
from router import Router

def main():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Please set your OPENAI_API_KEY environment variable first!")
        return

    # Load sample tickets
    df = pd.read_csv("data/tickets.csv")

    classifier = AIClassifier(api_key)
    router = Router()

    for _, row in df.iterrows():
        subject = row["subject"]
        desc = row["description"]
        category = classifier.classify_ticket(subject, desc)
        router.route_ticket(row["id"], category, subject, desc)

if __name__ == "__main__":
    main()