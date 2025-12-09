from google import genai

client = genai.Client(api_key="AIzaSyDCqn2wo9bl67e0r1kjmPL1eidczqdpLTU")

while True: 
    print("Mi primer promt con API GEMINI".center(40,"-"))
    pregunta = input("pregunta a Gemini:")
    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=pregunta
    )
    print(response.text)


    continuar = input("¿Desea efectuar otra pregunta a Gemini (S/N):?")
    if continuar.upper()=="S":
        continue
    else:
        print("Fin del programa. Gracias por usar nuestro promt")
        break