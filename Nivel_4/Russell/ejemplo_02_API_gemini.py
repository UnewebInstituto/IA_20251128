from google import genai

client = genai.Client(api_key="AIzaSyAnsK6bLnIlcasPgRoUH0V_lDoA6kVzLhw")

while True: 
    print ("Mi prmimer prompt con API Gemini".center(40,"-"))
    pregunta = input("Pregunta a Gemini  ")
    response = client.models.generate_content(
        model="gemini-2.5-flash", contents = pregunta
    )
    print(response.text)

    continuar = input("Desea efecuar otra pregunta S/N:?")
    if continuar.upper() == "S":
        continue
    else:
        print("fin del programa")
        break