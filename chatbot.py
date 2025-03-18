import PySimpleGUI as sg
import google.generativeai as ai
import buttons

# Configurar API do Gemini
API_KEY = "AIzaSyCiprekWrldb64DBpfWvUTo-atHJX3XTGM"
ai.configure(api_key=API_KEY)
model = ai.GenerativeModel("models/gemini-1.5-pro-latest")
chat = model.start_chat()

# Configuração do tema
theme = "SystemDefault1"
sg.theme(theme)

# Layout da interface
layout = [
    [sg.Image(data=buttons.icone_chatbot), sg.Text("MDB", font=("Verdana", 14))],
    
    # Output apenas para exibição (não editável)
    [sg.Multiline(size=(70, 15), key="-OUTPUT-", disabled=True, autoscroll=True, font=("Verdana", 12), text_color="black", background_color="white")],
    
    # Entrada de texto e botão de enviar
    [sg.InputText(key="-INPUT-", size=(65, 2), font=("Verdana", 12)), 
     sg.Button("", image_data=buttons.button_enviar_base64, border_width=0)],
]

# Criar a janela
window = sg.Window("IA dos Meninos do Brega", layout, finalize=True)

# Loop principal do chatbot
while True:
    event, values = window.read()
    
    if event == sg.WINDOW_CLOSED:
        break
    
    if event == "":  # Quando o botão de enviar for pressionado
        user_message = values["-INPUT-"].strip()
        if user_message:
            window["-OUTPUT-"].update(f"User: {user_message}\n", append=True)
            
            response = chat.send_message(user_message).text
            window["-OUTPUT-"].update(f"MDB: {response}\n\n", append=True)
            
            window["-INPUT-"].update("")  # Limpar o campo de entrada

# Fechar a janela
window.close()
