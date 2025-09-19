import customtkinter as ctk
import file
import chat

def theme_command():
    ctk.set_appearance_mode(theme_variable.get())
    file.theme_save(theme_variable.get())
    theme_switch.configure(text=theme_variable.get())

theme = file.theme_check()

ctk.set_appearance_mode(theme)
ctk.ThemeManager.theme["CTkFont"] = {"family":"Segoe UI", "size":15, "weight":"normal"}

root = ctk.CTk()
root.title("VultAI")
root.geometry("800x600")
root.resizable(True, True)

bottom_frame = ctk.CTkFrame(root)
bottom_frame.pack(side="bottom", anchor="e", padx=5, pady=5, fill="both", expand=True)

chat_box = ctk.CTkTextbox(bottom_frame, wrap="word", state="disabled")
chat_box.pack(pady=10, padx=10, fill="both", expand=True)

entry = ctk.CTkEntry(bottom_frame, width=780)
entry.bind("<Return>", chat.chat_send)
entry.pack(side="bottom", anchor="s", pady=5, padx=5)

top_frame = ctk.CTkFrame(root)
top_frame.pack(side="right", anchor="n", padx=5, pady=5, fill="both", expand=True)

theme_variable = ctk.StringVar(master=root, value=theme)
theme_switch = ctk.CTkSwitch(top_frame, command=theme_command, onvalue="Light", offvalue="Dark", variable=theme_variable, text=theme_variable.get())
theme_switch.pack(pady=10, padx=10, side="left", anchor="n")

root.mainloop()