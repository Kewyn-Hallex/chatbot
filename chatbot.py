import PySimpleGUI as sg
import google.generativeai as ai
import buttons

# Configurar API do Gemini
API_KEY = "AIzaSyCiprekWrldb64DBpfWvUTo-atHJX3XTGM"
ai.configure(api_key=API_KEY)
model = ai.GenerativeModel("gemini-pro")
chat = model.start_chat()

# Layout da interface
theme = "SystemDefault1"
sg.theme(theme)
layout = [
    [sg.Image(data=buttons.icone_chatbot),sg.Text("MDB", font=("Helvetica", 14))],
    [sg.Output(size=(70, 15), key="-OUTPUT-")],
    [sg.InputText(key="-INPUT-", size=(65, 2)), sg.Button("",image_data=buttons.button_enviar_base64)],
]

# Criar a janela
window = sg.Window("IA dos Meninos do Brega", layout, finalize=True)

# Loop principal do chatbot
while True:
    event, values = window.read()
    
    if event == sg.WINDOW_CLOSED:
        break
    
    if event == "":
        user_message = values["-INPUT-"].strip()
        if user_message:
            print(f"Você: {user_message}")
            response = chat.send_message(user_message)
            print(f"Chatbot: {response.text}\n")
            window["-INPUT-"].update("")  # Limpar o campo de entrada

# Fechar a janela
window.close()