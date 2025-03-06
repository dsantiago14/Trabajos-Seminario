# -*- coding: utf-8 -*-
"""
Created on Thu Mar  6 11:07:31 2025

@author: SANTIAGO
"""

import requests
import tkinter as tk
from tkinter import ttk, scrolledtext

# Reemplaza 'TU_API_KEY' con tu Clave API de DeepSeek
API_KEY = 'sk-53751d5c6f344a5dbc0571de9f51313e' 
API_URL = 'https://api.deepseek.com/v1/chat/completions'

# Función para enviar mensaje
def enviar_mensaje(message, modelo="deepseek-chat"):
    headers = {
        'Authorization': f"Bearer {API_KEY}",
        'Content-Type': 'application/json'
    }

    historico = [
        {"role": "system", "content": "Eres un emprendedor experto en Colombia. Aconseja sobre posibles emprendimientos de bajo costo y que estén dirigidos a estudiantes universitarios de últimos semestres de ingeniería electrónica sin que los emprendimientos estén directamente relacionados con su profesión, exprésate con respuestas sintetizadas, buen ánimo y preguntas al usuario."},
        {"role": "user", "content": message}
    ]

    data = {'model': modelo, 'messages': historico}

    try:
        response = requests.post(API_URL, headers=headers, json=data)
        response.raise_for_status()
        return response.json()['choices'][0]['message']['content']
    except requests.exceptions.HTTPError as err:
        return f"Error de la API: {err}"
    except Exception as e:
        return f"Error inesperado: {e}"

# Función para enviar y mostrar el mensaje en la interfaz
def enviar():
    user_message = entrada_usuario.get().strip()
    if user_message:
        chat_box.insert(tk.END, f"🧑‍💼 Tú: {user_message}\n", "usuario")
        chat_box.see(tk.END)  # Auto-scroll
        entrada_usuario.delete(0, tk.END)

        respuesta = enviar_mensaje(user_message)
        chat_box.insert(tk.END, f"🤖 Emprendedor: {respuesta}\n\n", "bot")
        chat_box.see(tk.END)  # Auto-scroll

# Configuración de la ventana principal
root = tk.Tk()
root.title("💡 Chatbot Emprendedor")
root.geometry("800x600")
root.configure(bg="#f5f5f5")

# Estilos mejorados con ttk
style = ttk.Style()
style.configure("TButton",
                font=("Arial", 14, "bold"),
                padding=10,
                background="#007BFF",  
                foreground="white")
style.map("TButton",
          foreground=[("active", "white")],
          background=[("active", "#0056b3")])  # Efecto al pasar el cursor

# Etiqueta de título
titulo = tk.Label(root, text="💡 Chatbot Emprendedor", 
                  font=("Arial", 22, "bold"), bg="#f5f5f5", fg="#222")
titulo.pack(pady=10)

# Área de chat con scroll
chat_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=20, font=("Arial", 12), bg="#ffffff", fg="#333")
chat_box.pack(padx=20, pady=10)
chat_box.tag_config("usuario", foreground="#007BFF", font=("Arial", 12, "bold"))
chat_box.tag_config("bot", foreground="#28A745", font=("Arial", 12))

# Marco para entrada y botón
entrada_frame = tk.Frame(root, bg="#f5f5f5")
entrada_frame.pack(pady=10)

entrada_usuario = ttk.Entry(entrada_frame, width=60, font=("Arial", 14))
entrada_usuario.grid(row=0, column=0, padx=10)

# Botón de enviar con diseño moderno
boton_enviar = tk.Button(entrada_frame, text="🚀 Enviar", command=enviar,
                         font=("Arial", 14, "bold"), bg="#007BFF", fg="white",
                         activebackground="#0056b3", activeforeground="white",
                         relief="flat", padx=20, pady=8, cursor="hand2")
boton_enviar.grid(row=0, column=1, padx=10)

# Ejecutar la ventana
root.mainloop()
