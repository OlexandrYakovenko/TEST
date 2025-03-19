from gtts import gTTS
import os
import sys

def speak_text(text):
    # Створення об’єкту gTTS з українською мовою (lang='uk')
    tts = gTTS(text=text, lang='uk')
    
    # Збереження озвученого тексту у файл output.mp3
    filename = "output.mp3"
    tts.save(filename)
    
    # Відтворення аудіофайлу (залежно від операційної системи)
    if sys.platform == "win32":
        os.system(f"start {filename}")
    elif sys.platform == "darwin":
        os.system(f"afplay {filename}")
    else:
        # Для Linux можна скористатися mpg123 або іншим плеєром
        os.system(f"mpg123 {filename}")

if __name__ == '__main__':
    # Зчитування тексту від користувача
    text = input("Введіть текст для озвучення: ")
    speak_text(text)
