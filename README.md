# 🧠 Blind-Deaf Communicator

A Python-based desktop application that enables communication between deaf/mute and blind users using speech recognition, text-to-speech, and a graphical interface. This tool bridges communication gaps and promotes inclusive conversations between individuals with sensory impairments.

---

## 💡 Features

- 🎙️ **Speech Recognition** for blind users using `speech_recognition`
- 🗣️ **Text-to-Speech** responses for deaf/mute users using `pyttsx3`
- 📷 **OpenCV Face Detection** to activate speech input when a face is detected
- 🖼️ Clean **Tkinter GUI** interface
- ✨ Inspirational welcome messages
- 🔁 Resettable conversation box for continued use

---

## 📷 How It Works

1. **Blind user** speaks into the microphone.
   - System detects face via webcam.
   - Captures speech and converts to text.
   - Displays message in conversation box.
2. **Deaf/Mute user** types a response.
   - Text is converted to speech.
   - Played back for the blind user.

---

## 🛠️ Built With

- [`Tkinter`](https://docs.python.org/3/library/tkinter.html) – GUI library for Python
- [`speech_recognition`](https://pypi.org/project/SpeechRecognition/) – For converting speech to text
- [`pyttsx3`](https://pypi.org/project/pyttsx3/) – For converting text to speech
- [`OpenCV`](https://opencv.org/) – For face detection and camera access
- [`Pillow`](https://pypi.org/project/Pillow/) – For displaying images in the GUI

---

## 🚀 Getting Started

### Prerequisites

Make sure you have Python installed along with the following libraries:

```bash
pip install opencv-python pillow pyttsx3 SpeechRecognition
