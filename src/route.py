import os

class Router:
    def __init__(self, output_dir="output"):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def route_ticket(self, ticket_id, category, subject, description):
        """Mock routing: write ticket details to a category-specific file"""
        filename = os.path.join(self.output_dir, f"{category.lower().replace(' ', '_')}.txt")
        with open(filename, "a") as f:
            f.write(f"ID: {ticket_id}\nSubject: {subject}\nDescription: {description}\n\n")
        print(f"✅ Routed Ticket #{ticket_id} to {category}")
