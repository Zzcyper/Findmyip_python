import requests
import tkinter as tk
from tkinter import messagebox

def track_ip():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        data = response.json()
        ip_address = data['ip']
        messagebox.showinfo("IP Address", f"Your IP address is: {ip_address}")
    except requests.RequestException:
        messagebox.showerror("Error", "An error occurred while retrieving the IP address.")


window = tk.Tk()
window.title("IP Tracker")
window.configure(bg="gray")  

track_button = tk.Button(window, text="Track IP", command=track_ip)
track_button.pack(pady=10)

window.mainloop()
