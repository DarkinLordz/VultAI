import customtkinter as ctk
import file
import api

def theme_toggle():
    global theme_switch_variable
    if ctk.get_appearance_mode() == "Dark":
        ctk.set_appearance_mode("Light")
        theme_switch_variable.set("Light")
    elif ctk.get_appearance_mode() == "Light":
        ctk.set_appearance_mode("Dark")
        theme_switch_variable.set("Dark")

def filter_toggle():
    file.filter_toggle(filter_switch_variable.get())

def flush_command():
    file.history_delete()
    chat_label.configure(text="")

def interact_with_ai(prompt):
    try:
        answer = api.send_request(prompt)
        return answer
    except Exception as error:
        return error

def chat_send(event=None):
    prompt = entry.get()
    if prompt == "/flush":
        flush_command()
    elif prompt == "/theme":
        theme_toggle()
    elif prompt == "/exit":
        root.destroy()
        return
    else:
        try:
            answer = interact_with_ai(prompt)
            interaction = [{"role":"user", "content":prompt}, {"role":"assistant", "content":answer}]
            chat_label.configure(text=answer)
            file.history_save(interaction)
        except Exception as error:
            chat_label.configure(text=error)
            file.log_save(error)
    entry.delete(0, "end")

file.file_ensure()
image = file.image_return()
image_exists = bool(image)

ctk.set_appearance_mode("Dark")
ctk.ThemeManager.theme["CTkFont"] = {"family":"Segoe UI", "size":15, "weight":"normal"}

root = ctk.CTk()
root.title("VultAI")
root.geometry("800x600")
root.resizable(False, False)

bottom_frame = ctk.CTkFrame(root)
bottom_frame.pack(side="bottom", anchor="e", padx=5, pady=5, fill="both", expand=True)

chat_label = ctk.CTkLabel(bottom_frame, text="", wraplength=780)
chat_label.pack(pady=10, padx=10, anchor="nw", side="top")

entry = ctk.CTkEntry(bottom_frame, width=780)
entry.bind("<Return>", chat_send)
entry.pack(side="bottom", anchor="s", pady=5, padx=5)

top_frame = ctk.CTkFrame(root)
top_frame.pack(side="right", anchor="n", padx=5, pady=5, fill="both", expand=True)

if image_exists:
    image_label = ctk.CTkLabel(top_frame, image=image, text="")
    image_label.pack(side="left", anchor="n", pady=5, padx=5)

theme_switch_variable = ctk.StringVar(value="Dark")
theme_switch = ctk.CTkSwitch(top_frame, command=theme_toggle, onvalue="Light", offvalue="Dark", variable=theme_switch_variable, text="Theme")
theme_switch.pack(pady=10, padx=10, side="left", anchor="n")

filter_switch_variable = ctk.StringVar(value="filter_off")
filter_switch = ctk.CTkSwitch(top_frame, command=filter_toggle, variable=filter_switch_variable, onvalue="filter_on", offvalue="filter_off", text="Filter")
filter_switch.pack(pady=10, padx=10, side="left", anchor="n")

root.mainloop()