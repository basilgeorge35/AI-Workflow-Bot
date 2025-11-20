import openai

# Simple helper class for AI classification
class AIClassifier:
    def __init__(self, api_key):
        openai.api_key = api_key

    def classify_ticket(self, subject, description):
        """Ask GPT model to categorise a support ticket into a simple label"""
        try:
            prompt = f"""
            Categorise this ticket into one of the following:
            [Billing, Technical Issue, Product Feedback, Account, Other]

            Subject: {subject}
            Description: {description}

            Reply with only the category name.
            """
            response = openai.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.2,
                max_tokens=10
            )
            category = response.choices[0].message.content.strip()
            return category
        except Exception as e:
            print(f"[Error] Failed to classify ticket: {e}")
            return "Other"
