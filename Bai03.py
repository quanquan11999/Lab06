# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 13:35:47 2024

@author: SinhVien
"""

import tkinter as tk
from tkinter import messagebox

def submit_form():
    # Lấy dữ liệu từ các trường nhập
    name = name_entry.get()
    last_name = last_name_entry.get()
    title = title_entry.get()
    age = age_entry.get()
    nationality = nationality_entry.get()

    # Lấy dữ liệu từ khung đăng ký
    is_registered = registered_checkbox.get()
    courses_completed = courses_completed_spinbox.get()
    semester = semester_combobox.get()

    # Kiểm tra xem người dùng đã đồng ý với Điều khoản và Điều kiện hay chưa
    if not terms_checkbox.get():
        messagebox.showerror("Lỗi", "Bạn cần đồng ý với Điều khoản và Điều kiện")
        return

    # In thông báo ra bảng điều khiển
    print(f"""
        Thông tin người dùng:
            - Tên: {name} {last_name}
            - Chức danh: {title}
            - Tuổi: {age}
            - Quốc tịch: {nationality}

        Thông tin đăng ký:
            - Trạng thái đăng ký: {"Đã đăng ký" if is_registered else "Chưa đăng ký"}
            - Số khóa học đã hoàn thành: {courses_completed}
            - Học kỳ: {semester}
    """)

root = tk.Tk()
root.title("Đăng ký khóa học")
root.geometry("500x400")

# Khung thông tin người dùng
user_info_frame = tk.Frame(root)
user_info_frame.pack(pady=20)

name_label = tk.Label(user_info_frame, text="Tên:")
name_label.pack(side=tk.LEFT)

name_entry = tk.Entry(user_info_frame)
name_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)

last_name_label = tk.Label(user_info_frame, text="Họ:")
last_name_label.pack(side=tk.LEFT)

last_name_entry = tk.Entry(user_info_frame)
last_name_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)

title_label = tk.Label(user_info_frame, text="Chức danh:")
title_label.pack(side=tk.LEFT)

title_entry = tk.Entry(user_info_frame)
title_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)

age_label = tk.Label(user_info_frame, text="Tuổi:")
age_label.pack(side=tk.LEFT)

age_entry = tk.Entry(user_info_frame)
age_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)

nationality_label = tk.Label(user_info_frame, text="Quốc tịch:")
nationality_label.pack(side=tk.LEFT)

nationality_entry = tk.Entry(user_info_frame)
nationality_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)

# Khung đăng ký
registration_frame = tk.Frame(root)
registration_frame.pack(pady=20)

registered_label = tk.Label(registration_frame, text="Đã đăng ký:")
registered_label.pack(side=tk.LEFT)

registered_checkbox = tk.BooleanVar()
registered_checkbox.set(False)  # Default value
registered_checkbox_entry = tk.Checkbutton(registration_frame, variable=registered_checkbox)
registered_checkbox_entry.pack(side=tk.LEFT)

courses_completed_label = tk.Label(registration_frame, text="Số khóa học đã hoàn thành:")
courses_completed_label.pack(side=tk.LEFT)

courses_completed_spinbox = tk.Spinbox(registration_frame, from_=0, to=10)
courses_completed_spinbox.pack(side=tk.LEFT)

semester_label = tk.Label(registration_frame, text="Học kỳ:")
semester_label.pack(side=tk.LEFT)

semester_combobox = tk.StringVar()
semester_combobox.set("Học kỳ 1")
semester_combobox_entry = tk.OptionMenu(registration_frame, semester_combobox, "Học kỳ 1", "Học kỳ 2", "Học kỳ 3")
semester_combobox_entry.pack(side=tk.LEFT)

terms_checkbox = tk.BooleanVar()
terms_checkbox_entry = tk.Checkbutton(root, text="Tôi đồng ý với Điều khoản và Điều kiện", variable=terms_checkbox)
terms_checkbox_entry.pack()

submit_button = tk.Button(root, text="Đăng ký", command=submit_form)
submit_button.pack(pady=10)

root.mainloop()
