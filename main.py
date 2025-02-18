import pywhatkit as kit
import tkinter as tk
from tkinter import filedialog, messagebox
import time
import random

def send_messages():
    numbers = entry_numbers.get("1.0", tk.END).strip().split("\n")
    message_template = entry_message.get("1.0", tk.END).strip()
    delay = int(entry_delay.get())

    if not numbers or not message_template:
        messagebox.showerror("Error", "Please enter numbers and a message.")
        return

    for entry in numbers:
        entry = entry.strip()
        if entry:
            try:
                parts = entry.split(" ", 1)  # Split number and name
                if len(parts) == 2:
                    number, name = parts
                else:
                    number, name = parts[0], "there"  # Default to "there" if no name provided

                # Replace <name> with actual name
                message = message_template.replace("<name>", name)

                kit.sendwhatmsg_instantly(f"+{number}", message, wait_time=delay)
                time.sleep(random.randint(delay, delay + 5))  # Adding randomness to avoid detection
            except Exception as e:
                messagebox.showwarning("Warning", f"Could not send to {entry}: {e}")

    messagebox.showinfo("Success", "Messages sent successfully!")


def load_numbers():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "r") as file:
            numbers = file.read()
            entry_numbers.delete("1.0", tk.END)
            entry_numbers.insert(tk.END, numbers)

# UI Setup
root = tk.Tk()
root.title("WhatsApp Bulk Sender")
root.geometry("500x500")

tk.Label(root, text="Enter Numbers (One per line):").pack()
entry_numbers = tk.Text(root, height=8, width=50)
entry_numbers.pack()

tk.Button(root, text="Load from File", command=load_numbers).pack()

tk.Label(root, text="Enter Message:").pack()
entry_message = tk.Text(root, height=5, width=50)
entry_message.pack()

tk.Label(root, text="Delay between messages (seconds):").pack()
entry_delay = tk.Entry(root)
entry_delay.insert(0, "5")  # Default delay
entry_delay.pack()

tk.Button(root, text="Send Messages", command=send_messages).pack()

root.mainloop()
