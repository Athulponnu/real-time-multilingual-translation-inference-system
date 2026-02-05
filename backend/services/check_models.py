import os
from google import genai

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

models = client.models.list()

print("\nAvailable Models:\n")

for m in models:
    print("Name:", m.name)
    print("Description:", m.description)
    print("----")
