import PySimpleGUI as sg #Biblioteca usada para criar interfaces gráficas.
import google.generativeai as ai # Biblioteca do Gemini (IA do Google) para gerar respostas.
import buttons #Um módulo personalizado que contém imagens de botões usados na interface.

# Configurar API do Gemini
API_KEY = "AIzaSyCiprekWrldb64DBpfWvUTo-atHJX3XTGM" #Define a chave da API
ai.configure(api_key=API_KEY) #Configura a API do Gemini.
model = ai.GenerativeModel("models/gemini-1.5-pro-latest") #Define o modelo de IA a ser usado
chat = model.start_chat() #Inicia um chat com o modelo para interações contínuas.

# Configuração do tema
theme = "DarkBrown1"
sg.theme(theme) #Define o tema da interface como SystemDefault1, que usa um estilo nativo do sistema operacional. SystemDefault1

# Layout da interface
layout = [
    [sg.Image(data=buttons.icone_chatbot), sg.Text("MDB", font=("Verdana", 14))], #Adiciona uma imagem (buttons.icone_chatbot) e um título ("MDB").
    
    # Output apenas para exibição (não editável)
    [sg.Multiline(size=(70, 15), key="-OUTPUT-", disabled=True, autoscroll=True, font=("Verdana", 12), text_color="white", background_color="#4b4949")], #Adiciona uma área de saída de texto (sg.Multiline), onde as mensagens do usuário e da IA serão exibidas.
    
    # Entrada de texto e botão de enviar
    [sg.InputText(key="-INPUT-", size=(65, 2), font=("Verdana", 12), background_color="#4b4949" , text_color="white"), #Adiciona um campo de entrada de texto (sg.InputText) para o usuário digitar a pergunta.
     sg.Button("", image_data=buttons.button_enviar_base64, border_width=0, button_color=("#4b4949", "#2C2825"))], #Adiciona um botão de envio que usa uma imagem (buttons.button_enviar_base64).
]

# Criar a janela
window = sg.Window("IA dos Meninos do Brega", layout, finalize=True) #Cria a janela com o título "IA dos Meninos do Brega" e usa o layout definido anteriormente.

# Loop principal do chatbot
#Inicia um loop que mantém a janela aberta e aguarda interações do usuário.
while True:
    event, values = window.read()
    
    if event == sg.WINDOW_CLOSED: #Se o usuário fechar a janela (sg.WINDOW_CLOSED), o loop é interrompido e a aplicação é encerrada.
        break
    
    if event == "":  #Quando o botão de envio for pressionado (if event == ""), a mensagem digitada pelo usuário (values["-INPUT-"]) é capturada.
        user_message = values["-INPUT-"].strip()
        if user_message: #Se a mensagem não estiver vazia, ela é exibida no campo de saída (-OUTPUT-).
            window["-OUTPUT-"].update(f"User: {user_message}\n", append=True) #Se a mensagem não estiver vazia, ela é exibida no campo de saída (-OUTPUT-).
            
            response = chat.send_message(user_message).text #A mensagem é enviada para a IA (chat.send_message(user_message).text), e a resposta gerada é adicionada ao campo de saída.
            window["-OUTPUT-"].update(f"MDB: {response}\n\n", append=True)
            
            window["-INPUT-"].update("")  #O campo de entrada é limpo para permitir novas mensagens.

# Fechar a janela
window.close()