import tkinter as tk
from tkinter import messagebox
from playsound import playsound

# Alphabet list
alphabets = [chr(i) for i in range(65, 91)]  # 'A' to 'Z'
current_index = 0

# Sound playback (replace with your actual paths or logic)
def play_sound(letter):
    try:
        playsound(f'sounds/{letter}.mp3')  # Assumes sounds are stored like A.mp3, B.mp3...
    except:
        print(f'Sound for {letter} not found.')

# Check user input
def check_input():
    global current_index
    user_input = entry.get().upper()
    if user_input == alphabets[current_index]:
        current_index += 1
        if current_index == len(alphabets):
            messagebox.showinfo("Success", "You've mastered the alphabet!")
            root.destroy()
        else:
            update_prompt()
    else:
        messagebox.showerror("Oops", "Try again!")

# Update GUI prompt
def update_prompt():
    prompt_label.config(text=f"Enter: {alphabets[current_index]}")
    play_sound(alphabets[current_index])
    entry.delete(0, tk.END)

# GUI Setup
root = tk.Tk()
root.title("Alphabet Learning Game")
root.geometry("300x200")

prompt_label = tk.Label(root, text="", font=("Arial", 18))
prompt_label.pack(pady=20)

entry = tk.Entry(root, font=("Arial", 18))
entry.pack()

submit_btn = tk.Button(root, text="Check", command=check_input)
submit_btn.pack(pady=10)

update_prompt()
root.mainloop()