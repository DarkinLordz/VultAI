import api
import file
import gui

def flush_command():
    file.history_delete()
    gui.chat_box.delete("1.0", "end")

def api_command(prompt):
    prompt = prompt.split()

    if len(prompt) != 4:
        file.log_save("Invalid API command format.")
        return
    
    api = prompt[1]
    url = prompt[2]
    model = prompt[3]

    file.api_save(api, url, model)

def interact_with_ai(prompt):
    try:
        answer = api.send_request(prompt)
        return answer
    except Exception as error:
        return error

def chat_send(event=None):
    prompt = gui.entry.get().strip()
    if not prompt:
        return
    gui.chat_box.configure(state="normal")
    if prompt == "/flush":
        flush_command()
    elif "/api" in prompt:
        api_command(prompt)
    elif prompt == "/exit":
        gui.root.destroy()
        return
    else:
        try:
            answer = interact_with_ai(prompt)
            if not answer:
                file.log_save("API not configured correctly.")
                return
            interaction = [{"role":"user", "content":prompt}, {"role":"assistant", "content":answer}]
            gui.chat_box.insert("end", f"You: {prompt}\n\nAI: {answer}\n\n")
            file.history_save(interaction)
        except Exception as error:
            gui.chat_box.insert("end", f"You: {prompt}\n\nAI: {error}\n\n")
            file.log_save(error)
    gui.chat_box.see("end")
    gui.chat_box.configure(state="disabled")
    gui.entry.delete(0, "end")