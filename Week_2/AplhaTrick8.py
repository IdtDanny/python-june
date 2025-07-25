import tkinter as tk
from tkinter import messagebox

# List of uppercase alphabets
alphabets = [chr(i) for i in range(65, 91)]  # A-Z
current_index = 0
game_active = False

# Start the game
def start_game():
    global game_active, current_index
    game_active = True
    current_index = 0
    update_prompt()
    entry.config(state="normal")
    submit_btn.config(state="normal")
    resume_btn.config(state="disabled")

# Pause the game
def pause_game():
    global game_active
    game_active = False
    prompt_label.config(text="Game paused.")
    entry.config(state="disabled")
    submit_btn.config(state="disabled")
    resume_btn.config(state="normal")

# Resume the game
def resume_game():
    global game_active
    game_active = True
    update_prompt()
    entry.config(state="normal")
    submit_btn.config(state="normal")
    resume_btn.config(state="disabled")

# End the game
def end_game():
    root.destroy()

# Check user input
def check_input():
    global current_index
    if not game_active:
        return
    user_input = entry.get().upper()
    if user_input == alphabets[current_index]:
        current_index += 1
        if current_index == len(alphabets):
            messagebox.showinfo("Success", "You've completed the alphabet!")
            root.destroy()
        else:
            update_prompt()
    else:
        messagebox.showerror("Oops", "That's not the correct letter. Try again!")

# Update prompt label
def update_prompt():
    prompt_label.config(text=f"Enter: {alphabets[current_index]}")
    entry.delete(0, tk.END)

# GUI setup
root = tk.Tk()
root.title("Alphabet Learning Game")
root.geometry("400x300")
root.configure(bg="#f0f8ff")

prompt_label = tk.Label(root, text="", font=("Arial", 20, "bold"), bg="#f0f8ff", fg="#333")
prompt_label.pack(pady=20)

entry = tk.Entry(root, font=("Arial", 20), justify="center", state="disabled")
entry.pack()

submit_btn = tk.Button(root, text="Check", command=check_input, state="disabled", bg="#4CAF50", fg="white", font=("Arial", 12, "bold"))
submit_btn.pack(pady=10)

# Frame for control buttons
control_frame = tk.Frame(root, bg="#f0f8ff")
control_frame.pack(pady=20)

btn_config = {"width": 10, "height": 2, "font": ("Arial", 11, "bold")}

start_btn = tk.Button(control_frame, text="Start", command=start_game, bg="#2196F3", fg="white", **btn_config)
start_btn.grid(row=0, column=0, padx=10)

pause_btn = tk.Button(control_frame, text="Pause", command=pause_game, bg="#FFC107", fg="black", **btn_config)
pause_btn.grid(row=0, column=1, padx=10)

resume_btn = tk.Button(control_frame, text="Resume", command=resume_game, bg="#8BC34A", fg="white", state="disabled", **btn_config)
resume_btn.grid(row=0, column=2, padx=10)

end_btn = tk.Button(control_frame, text="End", command=end_game, bg="#f44336", fg="white", **btn_config)
end_btn.grid(row=0, column=3, padx=10)

root.mainloop()