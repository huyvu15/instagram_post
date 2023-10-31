import tkinter as tk
from PIL import Image, ImageTk
from tkinter import *
from tkinter.ttk import *


def login():
    # Kiểm tra đăng nhập ở đây, bạn có thể thêm logic kiểm tra tài khoản và mật khẩu
    # Nếu đăng nhập thành công, chuyển sang cửa sổ chức năng
    main_window.destroy()
    show_function_window()

def show_function_window():
    function_window = tk.Tk()
    function_window.title("Chức năng đăng ảnh trên Instagram")
    function_window.geometry("800x600")  # Đặt kích thước cửa sổ
    
    icon = PhotoImage(file="logo.png")
    function_window.iconphoto(False, icon)  

    # Sử dụng hình ảnh làm nền
    image = Image.open("white_pink.jpg")
    photo = ImageTk.PhotoImage(image)
    background_label = tk.Label(function_window, image=photo)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    background_label.photo = photo  # Tránh bị thu hồi bởi Python's garbage collector

    # Thêm các chức năng và giao diện của cửa sổ chức năng ở đây
    label = tk.Label(function_window, text="Chức năng đăng ảnh trên Instagram")
    label.pack()

    function_window.mainloop()

# Tạo cửa sổ đăng nhập
main_window = tk.Tk()
main_window.title("Đăng nhập Instagram")
main_window.geometry("800x600") 
icon = PhotoImage(file="logo.png")
main_window.iconphoto(False, icon)


# Thêm các thành phần giao diện cho cửa sổ đăng nhập
label_username = tk.Label(main_window, text="Tài khoản:")
label_password = tk.Label(main_window, text="Mật khẩu:")
entry_username = tk.Entry(main_window)
entry_password = tk.Entry(main_window, show="*")  # Hiển thị dấu sao thay vì mật khẩu thực

button_login = tk.Button(main_window, text="Đăng nhập", command=login)
button_quit = tk.Button(main_window, text="Thoát", command=main_window.quit)

# Căn chỉnh phần tài khoản và mật khẩu ở giữa
label_username.place(relx=0.5, rely=0.4, anchor="center")
entry_username.place(relx=0.5, rely=0.45, anchor="center")
label_password.place(relx=0.5, rely=0.5, anchor="center")
entry_password.place(relx=0.5, rely=0.55, anchor="center")
button_login.place(relx=0.5, rely=0.6, anchor="center")
button_quit.place(relx=0.95, rely=0.95, anchor="se")

main_window.mainloop()
