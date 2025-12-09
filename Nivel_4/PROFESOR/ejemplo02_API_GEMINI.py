from google import genai

client = genai.Client(api_key="AIzaSyBCzRrF72hD6anUrX2XBVu8d5-YiOtNhcY")

while True:
    print("Mi primer prompt con API GEMINI".center(40,"-"))
    pregunta = input("Pregunta a Gemini:")
    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=pregunta
    )
    print(response.text)

    continuar = input("¿Desea efectuar otra pregunta a Gemini (S/N):?")
    if continuar.upper() == "S":
        continue
    else:
        print("Fin del programa. Gracias por usar nuestro prompt.")
        break