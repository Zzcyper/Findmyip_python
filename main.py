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

# Create a tkinter window
window = tk.Tk()
window.title("IP Tracker")
window.configure(bg="gray")  # Set the background color to gray

# Create track button
track_button = tk.Button(window, text="Track IP", command=track_ip)
track_button.pack(pady=10)

# Run the tkinter event loop
window.mainloop()