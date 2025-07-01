import tkinter as tk
import pyttsx3
import speech_recognition as sr

def speak_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        output_label.config(text="Listening...")
        try:
            audio = recognizer.listen(source)
            text = recognizer.recognize_google(audio)
            output_label.config(text=f"Blind User Said: {text}")
            text_output.insert(tk.END, f"Blind: {text}\n")
        except sr.UnknownValueError:
            output_label.config(text="Could not understand audio")
        except sr.RequestError:
            output_label.config(text="Could not request results")

def send_text():
    text = text_input.get()
    text_output.insert(tk.END, f"Deaf/Mute: {text}\n")
    speak_text(text)
    text_input.delete(0, tk.END)

def open_conversation():
    conversation_window = tk.Toplevel(root)
    conversation_window.title("Conversation Box")
    conversation_window.configure(bg="#D1C4E9")
    
    tk.Label(conversation_window, text="Deaf/Mute User: Type below and press Send", bg="#D1C4E9", fg="black").pack()
    conversation_input = tk.Entry(conversation_window, width=50)
    conversation_input.pack()
    tk.Button(conversation_window, text="Send", bg="#64B5F6", fg="white", command=lambda: send_conversation_text(conversation_input, conversation_output)).pack()
    
    global output_label
    output_label = tk.Label(conversation_window, text="Blind User: Speak into the microphone", bg="#D1C4E9", fg="black")
    output_label.pack()
    tk.Button(conversation_window, text="Listen", bg="#FF8A65", fg="white", command=lambda: recognize_conversation_speech(conversation_output)).pack()
    
    tk.Label(conversation_window, text="Conversation:", bg="#D1C4E9", fg="black").pack()
    conversation_output = tk.Text(conversation_window, height=10, width=50, bg="white", fg="black")
    conversation_output.pack()
    
    tk.Button(conversation_window, text="Reset Conversation", bg="#F06292", fg="white", command=lambda: reset_conversation(conversation_output)).pack()

def send_conversation_text(entry_widget, output_widget):
    text = entry_widget.get()
    output_widget.insert(tk.END, f"Deaf/Mute: {text}\n")
    speak_text(text)
    entry_widget.delete(0, tk.END)

def recognize_conversation_speech(output_widget):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        output_label.config(text="Listening...")
        try:
            audio = recognizer.listen(source)
            text = recognizer.recognize_google(audio)
            output_label.config(text=f"Blind User Said: {text}")
            output_widget.insert(tk.END, f"Blind: {text}\n")
        except sr.UnknownValueError:
            output_label.config(text="Could not understand audio")
        except sr.RequestError:
            output_label.config(text="Could not request results")

def reset_conversation(output_widget):
    output_widget.delete("1.0", tk.END)

root = tk.Tk()
root.title("Communication System")
root.geometry("420x420")
root.configure(bg="#B3E5FC")

tk.Button(root, text="Start Conversation", bg="#7E57C2", fg="white", command=open_conversation).pack()

root.mainloop()
