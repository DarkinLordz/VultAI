import customtkinter as ctk
import file
import api

def theme_command():
    ctk.set_appearance_mode(theme_variable.get())
    file.theme_save(theme_variable.get())
    theme_switch.configure(text=theme_variable.get())

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
theme = file.theme_check()
image = file.image_return()

ctk.set_appearance_mode(theme)
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

image_label = ctk.CTkLabel(top_frame, image=image, text="")
image_label.pack(side="left", anchor="n", pady=5, padx=5)

theme_variable = ctk.StringVar(master=root, value=theme)
theme_switch = ctk.CTkSwitch(top_frame, command=theme_command, onvalue="Light", offvalue="Dark", variable=theme_variable, text=theme_variable.get())
theme_switch.pack(pady=10, padx=10, side="left", anchor="n")

root.mainloop()