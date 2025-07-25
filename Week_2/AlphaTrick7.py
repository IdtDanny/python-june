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

# Pause the game
def pause_game():
    global game_active
    game_active = False
    prompt_label.config(text="Game paused.")
    entry.config(state="disabled")
    submit_btn.config(state="disabled")

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
root.geometry("350x250")

prompt_label = tk.Label(root, text="", font=("Arial", 18))
prompt_label.pack(pady=15)

entry = tk.Entry(root, font=("Arial", 18), state="disabled")
entry.pack()

submit_btn = tk.Button(root, text="Check", command=check_input, state="disabled")
submit_btn.pack(pady=5)

# Control buttons
start_btn = tk.Button(root, text="Start", command=start_game)
start_btn.pack(side="left", padx=15, pady=20)

pause_btn = tk.Button(root, text="Pause", command=pause_game)
pause_btn.pack(side="left", padx=15)

end_btn = tk.Button(root, text="End", command=end_game)
end_btn.pack(side="right", padx=15)

root.mainloop()