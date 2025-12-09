from google import genai

client = genai.Client(api_key="AIzaSyBCzRrF72hD6anUrX2XBVu8d5-YiOtNhcY")

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="Explica en pocas palabras cómo trabaja la IA"
)
print(response.text)