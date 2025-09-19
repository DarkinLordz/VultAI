from path import LOG_FILE, HISTORY_FILE, CONFIG_FILE
import time
import json

def timestamp():
    return time.strftime("%Y/%m/%d/%H/%M/%S", time.localtime())

def history_save(interaction):
    with open(HISTORY_FILE, "r", encoding="utf-8") as file:
        history = json.load(file)
    history.extend(interaction)
    with open(HISTORY_FILE, "w", encoding="utf-8") as file:
        json.dump(history, file, indent=4)

def history_delete():
    with open(HISTORY_FILE, "w", encoding="utf-8") as file:
        json.dump([], file, indent=4)

def log_save(error):
    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write(f"[{timestamp()}]: {error}\n")

def theme_check():
    with open(CONFIG_FILE, "r", encoding="utf-8") as file:
        data = json.load(file)
        theme = data["theme"]
    return theme
    
def theme_save(theme_variable):
    with open(CONFIG_FILE, "r", encoding="utf-8") as file:
        data = json.load(file)
    data["theme"] = theme_variable
    with open(CONFIG_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

def api_save(api, url, model):
    with open(CONFIG_FILE, "r", encoding="utf-8") as file:
        data = json.load(file)
    data["api"] = api
    data["url"] = url
    data["model"] = model
    with open(CONFIG_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)