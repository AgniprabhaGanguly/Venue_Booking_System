import customtkinter
from PIL import Image
import dbms

#supporting functions

def toggle_password_visibility(entry, button):
    if entry.cget('show') == '':
        entry.configure(show='*')
        button.configure(image= customtkinter.CTkImage(light_image=Image.open('Images/pass_show.png'), size=(20, 20)))
    else:
        entry.configure(show='')
        button.configure(image= customtkinter.CTkImage(light_image=Image.open('Images/pass_hide.png'), size=(20, 20)))

def login_submit(root, username, password, type):
    status = dbms.verify_login(username, password, type)
    if(status):
        main_page(root)
    else:
        error_label.configure(text='Invalid username/password')

#pages

def login_page(root):
    #clear screen
    for widget in root.winfo_children():
        widget.destroy()

    # title

    title_frame = customtkinter.CTkFrame(
        root,
        border_color='darkblue',
        border_width=2,
    )
    title_frame.pack(fill='x')

    title_label = customtkinter.CTkLabel(
        title_frame,
        text="Venue Booking System",
        font=('Helvetica', 24),
    )

    title_label.pack(pady=20)

    # id pass entries

    id_pass_frame = customtkinter.CTkFrame(root, fg_color='#292B2E')
    id_pass_frame.pack(fill='x')

    userID_label = customtkinter.CTkLabel(
        id_pass_frame,
        text="User ID :",
        font=('Helvetica', 16)
    )

    userID_label.grid(row=1, column=1, padx=(525, 5), pady=(100, 20))

    userID_entry = customtkinter.CTkEntry(
        id_pass_frame,
        placeholder_text="Enter User ID",
    )

    userID_entry.grid(row=1, column=2, padx=(5, 0), pady=(100, 20))

    password_label = customtkinter.CTkLabel(
        id_pass_frame,
        text="Password :",
        font=('Helvetica', 16)
    )

    password_label.grid(row=2, column=1, padx=(525, 5), pady=(0, 50))

    password_entry = customtkinter.CTkEntry(
        id_pass_frame,
        placeholder_text="Enter Password",
        show='*'
    )

    password_entry.grid(row=2, column=2, padx=(5, 0), pady=(0, 50))

    toggle_visibility = customtkinter.CTkButton(
        id_pass_frame,
        fg_color='white',
        text='',
        height=20,
        width=20,
        hover_color='lightgrey',
        image= customtkinter.CTkImage(light_image=Image.open('Images/pass_hide.png'), size=(20, 20)),
        command=lambda: toggle_password_visibility(password_entry, toggle_visibility)

    )

    toggle_visibility.grid(row=2, column=3, padx=(5, 0), pady=(0, 50))

    # buttons

    button_frame = customtkinter.CTkFrame(root, fg_color='#292B2E')
    button_frame.pack(fill='both', expand=True)

    userSelectBox = customtkinter.CTkComboBox(button_frame, values=['ADMIN', 'CLUB'])
    userSelectBox.pack(pady=20)

    submit_button = customtkinter.CTkButton(button_frame, text='SUBMIT', command=lambda : login_submit(root,userID_entry.get(),password_entry.get(), userSelectBox.get()))
    submit_button.pack(pady=20)

    register_button = customtkinter.CTkButton(button_frame, text='REGISTER CLUB', command=lambda : RegisterUser(root))
    register_button.pack(pady=20)

    global error_label
    error_label = customtkinter.CTkLabel(button_frame, text='')
    error_label.pack(pady=20)

def RegisterUser(root):
    #clear screen
    for widget in root.winfo_children():
        widget.destroy()

    # title

    title_frame = customtkinter.CTkFrame(
        root,
        border_color='darkblue',
        border_width=2,
    )
    title_frame.pack(fill='x')

    title_label = customtkinter.CTkLabel(
        title_frame,
        text="Venue Booking System",
        font=('Helvetica', 24),
    )

    title_label.pack(pady=20)

    # id pass entries

    id_pass_frame = customtkinter.CTkFrame(root, fg_color='#292B2E')
    id_pass_frame.pack(fill='x')

    clubID_label = customtkinter.CTkLabel(
        id_pass_frame,
        text="Club ID :",
        font=('Helvetica', 16)
    )

    clubID_label.grid(row=1, column=1, padx=(525, 5), pady=(100, 20))

    clubID_entry = customtkinter.CTkEntry(
        id_pass_frame,
        placeholder_text="Enter Club ID",
    )

    clubID_entry.grid(row=1, column=2, padx=(5, 0), pady=(100, 20))

    clubName_label = customtkinter.CTkLabel(
        id_pass_frame,
        text="Club Name :",
        font=('Helvetica', 16)
    )

    clubName_label.grid(row=2, column=1, padx=(525, 5), pady=(0, 20))

    clubName_entry = customtkinter.CTkEntry(
        id_pass_frame,
        placeholder_text="Enter Club Name",
    )

    clubName_entry.grid(row=2, column=2, padx=(5, 0), pady=(0, 20))

    password_label = customtkinter.CTkLabel(
        id_pass_frame,
        text="Password :",
        font=('Helvetica', 16)
    )

    password_label.grid(row=3, column=1, padx=(525, 5), pady=(0, 50))

    password_entry = customtkinter.CTkEntry(
        id_pass_frame,
        placeholder_text="Enter Password",
        show='*'
    )

    password_entry.grid(row=3, column=2, padx=(5, 0), pady=(0, 50))

    toggle_visibility = customtkinter.CTkButton(
        id_pass_frame,
        fg_color='white',
        text='',
        height=20,
        width=20,
        hover_color='lightgrey',
        image= customtkinter.CTkImage(light_image=Image.open('Images/pass_hide.png'), size=(20, 20)),
        command=lambda: toggle_password_visibility(password_entry, toggle_visibility)

    )

    toggle_visibility.grid(row=3, column=3, padx=(5, 0), pady=(0, 50))

    #button

    button_frame = customtkinter.CTkFrame(root, fg_color='#292B2E')
    button_frame.pack(fill='both', expand=True)

    register_button = customtkinter.CTkButton(button_frame, text='REGISTER', command=lambda : dbms.register_user(clubID_entry.get(), clubName_entry.get(), password_entry.get()))
    register_button.pack(pady=20)

    login_button = customtkinter.CTkButton(
        button_frame,
        text='LOGIN INSTEAD',
        command=lambda: login_page(root)
    )

    login_button.pack(pady=20)

def main_page(root):
    #clear screen
    for widget in root.winfo_children():
        widget.destroy()

    # title

    title_frame = customtkinter.CTkFrame(
        root,
        border_color='darkblue',
        border_width=2,
    )
    title_frame.pack(fill='x')

    title_label = customtkinter.CTkLabel(
        title_frame,
        text="Venue Booking System",
        font=('Helvetica', 24),
    )

    title_label.pack(pady=20)