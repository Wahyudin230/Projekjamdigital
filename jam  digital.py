import tkinter as tk
import time
from tkinter import messagebox

def update_time():
    current_time = time.strftime('%H:%M:%S')
    clock_label.config(text=current_time)
    if current_time == alarm_time.get():
        messagebox.showinfo("Alarm", "Waktunya bangun!")
    clock_label.after(1000, update_time)

# Membuat jendela utama
root = tk.Tk()
root.title('Jam Digital dengan Alarm')

# Membuat label untuk menampilkan waktu
clock_label = tk.Label(root, font=('Helvetica', 48), bg='black', fg='white')
clock_label.pack(padx=20, pady=20)

# Membuat field untuk mengatur alarm
tk.Label(root, text='Set Alarm (HH:MM:SS)', font=('Helvetica', 14)).pack(pady=5)
alarm_time = tk.Entry(root, font=('Helvetica', 14), justify='center')
alarm_time.pack(pady=5)
alarm_time.insert(0, '00:00:00')

# Memanggil fungsi untuk memperbarui waktu secara berkala
update_time()

# Menjalankan aplikasi
root.mainloop()
