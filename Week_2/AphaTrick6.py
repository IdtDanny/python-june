import tkinter as tk
from tkinter import messagebox

# List of uppercase alphabets
alphabets = [chr(i) for i in range(65, 91)]  # A-Z
print(alphabets)
current_index = 0

# Function to check user input
def check_input():
    global current_index
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

# Update the prompt label
def update_prompt():
    prompt_label.config(text=f"Enter: {alphabets[current_index]}")
    entry.delete(0, tk.END)

# GUI setup
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