import tkinter as tk
from tkinter import messagebox
import winsound  # For simple system sounds on Windows

# Create a list of uppercase English alphabets (A-Z)
alphabets = [chr(i) for i in range(65, 91)]
current_index = 0  # Keeps track of the current letter
game_active = False  # Indicates whether the game is running

# Sound effect for correct input
def play_success():
    winsound.MessageBeep(winsound.MB_ICONASTERISK)

# Sound effect for incorrect input
def play_error():
    winsound.MessageBeep(winsound.MB_ICONHAND)

# Sound effect when the game is completed
def play_completion():
    winsound.PlaySound("SystemExit", winsound.SND_ALIAS)

# Start/restart the game
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

# End the game and close the window
def end_game():
    root.destroy()

# Check if the entered letter is correct
def check_input():
    global current_index
    if not game_active:
        return
    user_input = entry.get().upper()
    if user_input == alphabets[current_index]:
        play_success()  # Play success sound
        current_index += 1
        if current_index == len(alphabets):
            play_completion()  # Play completion sound
            messagebox.showinfo("Success", "You've completed the alphabet!")
            root.destroy()
        else:
            update_prompt()
    else:
        play_error()  # Play error sound
        messagebox.showerror("Oops", "That's not the correct letter. Try again!")

# Update the prompt to show the next letter
def update_prompt():
    prompt_label.config(text=f"Enter: {alphabets[current_index]}")
    entry.delete(0, tk.END)

# GUI Setup
root = tk.Tk()
root.title("Alphabet Learning Game")
root.geometry("600x300")
root.configure(bg="#f0f8ff")  # Light blue background

# Display current prompt letter
prompt_label = tk.Label(root, text="", font=("Arial", 15, "bold"), bg="#f0f8ff", fg="#333")
prompt_label.pack(pady=20)

# User input field
entry = tk.Entry(root, font=("Arial", 15), justify="center", state="disabled")
entry.pack()

# Submit button to check input
submit_btn = tk.Button(root, text="Check", command=check_input, state="disabled",
                       bg="#4CAF50", fg="white", font=("Arial", 12, "bold"))
submit_btn.pack(pady=10)

# Frame to hold control buttons
control_frame = tk.Frame(root, bg="#f0f8ff")
control_frame.pack(pady=20)

# Button style config
btn_config = {"width": 10, "height": 1, "font": ("Arial", 11, "bold")}

# Start button
start_btn = tk.Button(control_frame, text="Start", command=start_game,
                      bg="#2196F3", fg="white", **btn_config)
start_btn.grid(row=0, column=0, padx=10)

# Pause button
pause_btn = tk.Button(control_frame, text="Pause", command=pause_game,
                      bg="#FFC107", fg="black", **btn_config)
pause_btn.grid(row=0, column=1, padx=10)

# Resume button
resume_btn = tk.Button(control_frame, text="Resume", command=resume_game,
                       bg="#8BC34A", fg="white", state="disabled", **btn_config)
resume_btn.grid(row=0, column=2, padx=10)

# End button
end_btn = tk.Button(control_frame, text="End", command=end_game,
                    bg="#f44336", fg="white", **btn_config)
end_btn.grid(row=0, column=3, padx=10)

# Start the GUI event loop
root.mainloop()