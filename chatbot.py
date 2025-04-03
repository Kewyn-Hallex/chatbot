import PySimpleGUI as sg 
import google.generativeai as ai
import buttons

# Configurar API do Gemini
API_KEY = "AIzaSyCiprekWrldb64DBpfWvUTo-atHJX3XTGM"
ai.configure(api_key=API_KEY)
model = ai.GenerativeModel("models/gemini-1.5-pro-latest")
chat = model.start_chat()

# Configuração do tema
theme = "DarkBrown1"
sg.theme(theme)

# Layout da interface
layout = [
    [sg.Image(data=buttons.icone_chatbot), sg.Text("MDB", font=("Verdana", 14))],
    
    [sg.Multiline(size=(70, 15), key="-OUTPUT-", disabled=True, autoscroll=True, font=("Verdana", 12), text_color="white", background_color="#4b4949")],
    
    [sg.InputText(key="-INPUT-", size=(65, 2), font=("Verdana", 12), background_color="#4b4949" , text_color="white"),
     sg.Button("", image_data=buttons.button_enviar_base64, border_width=0, button_color=("#4b4949", "#2C2825"))],
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
            window["-OUTPUT-"].update(f"User: {user_message}\n", append=True)
            
            response = chat.send_message(user_message).text
            window["-OUTPUT-"].update(f"MDB: {response}\n\n", append=True)
            
            window["-INPUT-"].update("")

# Fechar a janela
window.close()