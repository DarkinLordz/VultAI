import customtkinter as ctk
from PIL import Image
import time
import json
import os

def file_ensure():
    
    config = {
        "api": "",
        "url": "",
        "model": "",
        "theme": "Dark"
    }

    if not os.path.exists("assets"):
        os.mkdir("assets")
    if not os.path.exists("assets/image.png") or os.path.getsize("assets/image.png") == 0:
        (Image.new("RGB", (200, 200), color=(0, 0, 0))).save("assets/image.png")
    if not os.path.exists("config.json") or os.path.getsize("config.json") == 0:
        with open("config.json", "w", encoding="utf-8") as file:
            json.dump(config, file, indent=4)
    if not os.path.exists("history.json") or os.path.getsize("history.json") == 0:
        with open("history.json", "w", encoding="utf-8") as file:
            json.dump([], file)
    if not os.path.exists("personality.txt"):
        with open("personality.txt", "w", encoding="utf-8") as file:
            pass
    if not os.path.exists("log.txt"):
        with open("log.txt", "w", encoding="utf-8") as file:
            pass

def timestamp():
    return time.strftime("%Y/%m/%d/%H/%M/%S", time.localtime())

def history_save(interaction):
    with open("history.json", "r", encoding="utf-8") as file:
        history = json.load(file)
    history.extend(interaction)
    with open("history.json", "w", encoding="utf-8") as file:
        json.dump(history, file, indent=4)

def history_delete():
    with open("history.json", "w", encoding="utf-8") as file:
        json.dump([], file, indent=4)

def log_save(error):
    with open("log.txt", "a", encoding="utf-8") as file:
        file.write(f"[{timestamp()}]: {error}\n")

def theme_check():
    with open("config.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        theme = data["theme"]
    return theme
    
def theme_save(theme_variable):
    with open("config.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    data["theme"] = theme_variable
    with open("config.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

def api_save(api, url, model):
    with open("config.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    data["api"] = api
    data["url"] = url
    data["model"] = model
    with open("config.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

def image_return():
    if os.path.exists("assets/image.png"):
        image = Image.open("assets/image.png")
        return ctk.CTkImage(image, size=(200, 200))
    else:
        return False