from google import genai

client = genai.Client(api_key="AIzaSyDCqn2wo9bl67e0r1kjmPL1eidczqdpLTU")

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="Explica en pocas palabras como trabaja la IA"
)
print(response.text)