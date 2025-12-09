from google import genai

client = genai.Client(api_key="AIzaSyAnsK6bLnIlcasPgRoUH0V_lDoA6kVzLhw")

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="Expica en pocas palabas com tabaja la IA" 
)
print(response.text)