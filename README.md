# Language Translation Tool

## Objective:
The main objective of this project is to develop a **Language Translation Tool** that translates text between different languages and can also convert translated text to speech.

## Language:
- **Python 3.x**  
  Libraries used: `googletrans`, `gTTS`, `playsound`, `tkinter`.

## Features:
- Translate text from one language to another using Google Translate API.
- Text-to-speech conversion for translated text.
- Graphical User Interface (GUI) built with `tkinter`.
- Easy selection of source and target languages.
- Lightweight and user-friendly application.

## Folder Structure:
```
project_extracted/
│
├── language_translator.py   # Main application script
├── requirements.txt         # Python dependencies
└── User_Guide.pdf           # User manual
```

## How to Run:
1. **Install Python 3.x** (if not installed).
2. **Install required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the application**:
   ```bash
   python language_translator.py
   ```

## Sample Output:
- A GUI window will appear with:
  - Text input box for the source text.
  - Dropdown menus to select source and target languages.
  - A "Translate" button to get the translation.
  - A "Speak" button to listen to the translated text.

**Example:**  
Input: `Hello`  
Target Language: `Spanish`  
Output: `Hola` (audio playback available).


