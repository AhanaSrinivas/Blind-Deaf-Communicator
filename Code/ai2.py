import tkinter as tk
import pyttsx3
import speech_recognition as sr
import cv2
import threading

def speak_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def detect_speech_with_opencv(output_widget):
    cap = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        if len(faces) > 0:
            recognize_speech(output_widget)
            break
    cap.release()
    cv2.destroyAllWindows()

def recognize_speech(output_widget):
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

def send_text():
    text = text_input.get()
    text_output.insert(tk.END, f"Deaf/Mute: {text}\n")
    speak_text(text)
    text_input.delete(0, tk.END)

def open_conversation():
    conversation_window = tk.Toplevel(root)
    conversation_window.title("Conversation Box")
    conversation_window.configure(bg="#D1C4E9")
    
    welcome_message = ("Breaking barriers, building connections!\n"
                       "Every voice deserves to be heard!\n"
                       "Together, we communicate!\n"
                       "Understanding starts with listening!\n"
                       "Words have power – use them wisely!\n")
    
    tk.Label(conversation_window, text=welcome_message, bg="#D1C4E9", fg="black", wraplength=400).pack()
    
    conversation_window.after(1000, lambda: speak_text(welcome_message))  # Read aloud after window opens
    
    tk.Label(conversation_window, text="Deaf/Mute User: Type below and press Send", bg="#D1C4E9", fg="black").pack()
    conversation_input = tk.Entry(conversation_window, width=50)
    conversation_input.pack()
    tk.Button(conversation_window, text="Send", bg="#64B5F6", fg="white", command=lambda: send_conversation_text(conversation_input, conversation_output)).pack()
    
    global output_label
    output_label = tk.Label(conversation_window, text="Blind User: Speak into the microphone", bg="#D1C4E9", fg="black")
    output_label.pack()
    tk.Button(conversation_window, text="Listen", bg="#FF8A65", fg="white", command=lambda: threading.Thread(target=detect_speech_with_opencv, args=(conversation_output,)).start()).pack()
    
    tk.Label(conversation_window, text="Conversation:", bg="#D1C4E9", fg="black").pack()
    conversation_output = tk.Text(conversation_window, height=10, width=50, bg="white", fg="black")
    conversation_output.pack()
    
    tk.Button(conversation_window, text="Reset Conversation", bg="#F06292", fg="white", command=lambda: reset_conversation(conversation_output)).pack()

def send_conversation_text(entry_widget, output_widget):
    text = entry_widget.get()
    output_widget.insert(tk.END, f"Deaf/Mute: {text}\n")
    speak_text(text)
    entry_widget.delete(0, tk.END)

def reset_conversation(output_widget):
    output_widget.delete("1.0", tk.END)

root = tk.Tk()
root.title("Communication System")
root.geometry("420x420")
root.configure(bg="#B3E5FC")

welcome_message = "Welcome to the communication system. Deaf or mute users can type, and blind users can speak.\nBeing different doesn’t mean being disconnected—welcome to a world where everyone is heard!"
tk.Label(root, text=welcome_message, bg="#B3E5FC", fg="black", wraplength=400).pack()

root.after(1000, lambda: speak_text(welcome_message))  # Read aloud after interface opens
tk.Button(root, text="Start Conversation", bg="#7E57C2", fg="white", command=open_conversation).pack()

root.mainloop()  