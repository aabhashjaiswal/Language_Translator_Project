
import tkinter as tk
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES
from gtts import gTTS
import playsound
import os
import uuid

translator = Translator()
app = tk.Tk()
app.title("Language Translation Tool")
app.geometry("600x400")
app.resizable(False, False)

language_choices = list(LANGUAGES.values())
lang_code_map = {v: k for k, v in LANGUAGES.items()}

def translate_text():
    input_text = input_textbox.get("1.0", tk.END).strip()
    source_lang = lang_code_map[source_lang_var.get()]
    target_lang = lang_code_map[target_lang_var.get()]
    
    if not input_text:
        messagebox.showwarning("Input Required", "Please enter some text to translate.")
        return
    
    try:
        translated = translator.translate(input_text, src=source_lang, dest=target_lang)
        output_textbox.delete("1.0", tk.END)
        output_textbox.insert(tk.END, translated.text)
    except Exception as e:
        messagebox.showerror("Translation Error", f"An error occurred:\n{e}")

def copy_to_clipboard():
    output = output_textbox.get("1.0", tk.END).strip()
    if output:
        app.clipboard_clear()
        app.clipboard_append(output)
        messagebox.showinfo("Copied", "Translated text copied to clipboard!")

def text_to_speech():
    output = output_textbox.get("1.0", tk.END).strip()
    target_lang = lang_code_map[target_lang_var.get()]
    if output:
        try:
            tts = gTTS(text=output, lang=target_lang)
            filename = f"{uuid.uuid4()}.mp3"
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)
        except Exception as e:
            messagebox.showerror("TTS Error", f"Error in text-to-speech:\n{e}")

tk.Label(app, text="Enter Text:", font=('Arial', 12)).pack(pady=5)
input_textbox = tk.Text(app, height=5, width=70)
input_textbox.pack()

frame = tk.Frame(app)
frame.pack(pady=10)

source_lang_var = tk.StringVar()
target_lang_var = tk.StringVar()
source_lang_var.set("english")
target_lang_var.set("hindi")

ttk.Label(frame, text="From:").grid(row=0, column=0, padx=5)
source_lang_menu = ttk.Combobox(frame, textvariable=source_lang_var, values=language_choices, state="readonly", width=20)
source_lang_menu.grid(row=0, column=1, padx=5)

ttk.Label(frame, text="To:").grid(row=0, column=2, padx=5)
target_lang_menu = ttk.Combobox(frame, textvariable=target_lang_var, values=language_choices, state="readonly", width=20)
target_lang_menu.grid(row=0, column=3, padx=5)

tk.Button(app, text="Translate", command=translate_text, bg='skyblue', width=20).pack(pady=10)

tk.Label(app, text="Translated Text:", font=('Arial', 12)).pack()
output_textbox = tk.Text(app, height=5, width=70)
output_textbox.pack()

button_frame = tk.Frame(app)
button_frame.pack(pady=10)

tk.Button(button_frame, text="Copy", command=copy_to_clipboard, width=15).grid(row=0, column=0, padx=10)
tk.Button(button_frame, text="Text-to-Speech", command=text_to_speech, width=15).grid(row=0, column=1, padx=10)

app.mainloop()
