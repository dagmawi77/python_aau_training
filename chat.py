from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    input="In One sentence, What is CS50?",
    model="gpt-4o-mini")
print(response.output_text)