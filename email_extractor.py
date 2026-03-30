import re
import csv
import tkinter as tk
from tkinter import filedialog, messagebox

def extract_emails():
    file_path = filedialog.askopenfilename(title="Select a text file")
    if not file_path:
        return
    try:
        with open(file_path, "r") as file:
            content = file.read()
        emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+", content)
        unique_emails = list(set(emails))
        result_box.delete("1.0", tk.END)
        if unique_emails:
            for email in unique_emails:
                result_box.insert(tk.END, email + "\n")
            messagebox.showinfo("Success", f"Found {len(unique_emails)} emails")
        else:
            messagebox.showwarning("No Emails", "No emails found in file")
        window.emails = unique_emails
    except Exception as e:
        messagebox.showerror("Error", str(e))
def save_csv():
    if not hasattr(window, "emails") or not window.emails:
        messagebox.showwarning("No Data", "No emails to save")
        return
    save_path = filedialog.asksaveasfilename(defaultextension=".csv",
                                             filetypes=[("CSV files", "*.csv")])
    if not save_path:
        return
    try:
        with open(save_path, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Email"])  # header
            for email in window.emails:
                writer.writerow([email])
        messagebox.showinfo("Saved", "Emails saved successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))
window = tk.Tk()
window.title("📧 Email Extractor Pro")
window.geometry("400x350")
title_label = tk.Label(window, text="Email Extractor", font=("Arial", 16))
title_label.pack(pady=10)
extract_btn = tk.Button(window, text="Select File & Extract", command=extract_emails)
extract_btn.pack(pady=5)
save_btn = tk.Button(window, text="Save as CSV", command=save_csv)
save_btn.pack(pady=5)
result_box = tk.Text(window, height=12, width=45)
result_box.pack(pady=10)
window.mainloop()