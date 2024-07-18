import customtkinter as ctk
import requests
from tkinter import messagebox

def track_ip():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        data = response.json()
        ip_address = data['ip']
        messagebox.showinfo("IP Address", f"Your IP address is: {ip_address}")
    except requests.RequestException:
        messagebox.showerror("Error", "An error occurred while retrieving the IP address.")

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

window = ctk.CTk()
window.title("IP Tracker")
window.geometry("300x200")
window.configure(bg="black")

track_button = ctk.CTkButton(window, text="Track IP", command=track_ip)
track_button.pack(pady=10, padx=10)

window.mainloop()

