import customtkinter
from tkinter import ttk
from tktimepicker import AnalogPicker, AnalogThemes, constants
from tkcalendar import Calendar
from PIL import Image
import dbms

#for toggling password visibility
def toggle_password_visibility(password_entry, toggle_visibility):
    if password_entry.cget('show') == '':
        password_entry.configure(show='*')
        toggle_visibility.configure(
            image=customtkinter.CTkImage(light_image=Image.open('Images/pass_show.png'), size=(20, 20)))
    else:
        password_entry.configure(show='')
        toggle_visibility.configure(
            image=customtkinter.CTkImage(light_image=Image.open('Images/pass_hide.png'), size=(20, 20)))

#pages

def login_page(root):
    #supporting functions
    def login_submit(username, password, type, error_label):
        status = dbms.verify_login(username, password, type)
        if (status):
            main_page(root, dbms.get_clubname(username))
        else:
            error_label.configure(text='Invalid username/password')

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

    submit_button = customtkinter.CTkButton(button_frame, text='SUBMIT', command=lambda : login_submit(userID_entry.get(),password_entry.get(), userSelectBox.get(), error_label))
    submit_button.pack(pady=20)

    register_button = customtkinter.CTkButton(button_frame, text='REGISTER CLUB', command=lambda : RegisterUser(root))
    register_button.pack(pady=20)

    error_label = customtkinter.CTkLabel(button_frame, text='')
    error_label.pack(pady=20)

def RegisterUser(root):
    #supporting function
    def register_submit(ID, name, password):
        status = dbms.register_user(ID, name, password)
        if (status == True):
            login_page(root)

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

    register_button = customtkinter.CTkButton(button_frame, text='REGISTER', command=lambda : register_submit(clubID_entry.get(), clubName_entry.get(), password_entry.get()))
    register_button.pack(pady=20)

    login_button = customtkinter.CTkButton(
        button_frame,
        text='LOGIN INSTEAD',
        command=lambda: login_page(root)
    )

    login_button.pack(pady=20)

def main_page(root, clubname):
    #supporting database functions
    def fetch_data(from_date = None, to_date = None):
        data = dbms.fetch_data(from_date, to_date)
        return data

    def add_record(entries, win):
        entries = [entry.get() if isinstance(entry, customtkinter.CTkEntry) else entry for entry in entries]
        status = dbms.add_data(tuple(entries))
        if status == False:
            error_label.configure(text='Booking not possible due to conflicting bookings or fields are not given properly')
        if status == True:
            error_label.configure(text='')
            refresh_table()
        win.destroy()

    #supporting functions
    def refresh_table():
        lst = fetch_data()
        for item in table.get_children():
            table.delete(item)
        for i in range(1, len(lst) + 1):
            if i % 2 == 0:
                tag = 'evenrow'
            else:
                tag = 'oddrow'
            table.insert(parent='', index='end', values=lst[i - 1], iid=i, tags=tag)

    # calender

    def get_date(selected_date_label, booking_win):
        top = customtkinter.CTkToplevel(root)
        top.title("Select Date")
        top.transient(booking_win)
        top.wm_attributes('-topmost', True)

        cal = Calendar(top, selectmode='day', date_pattern='dd-mm-yyyy')
        cal.pack()

        def updateDate():
            selected_date_label.configure(state='normal')
            selected_date_label.delete(0, 'end')
            selected_date_label.insert(0, cal.get_date())
            selected_date_label.configure(state='disabled')
            top.destroy()

        select_button = customtkinter.CTkButton(top, text='Select', command=updateDate)
        select_button.pack(pady=10)

    # time
    def get_time(selected_time_label, booking_win):
        top = customtkinter.CTkToplevel(root)
        top.title("Select Time")
        top.transient(booking_win)
        top.wm_attributes('-topmost', True)

        time_picker = AnalogPicker(top, type=constants.HOURS12)
        time_picker.pack(expand=True, fill="both")

        theme = AnalogThemes(time_picker)
        theme.setDracula()

        def update_time(time):
            selected_time_label.configure(state='normal')
            selected_time_label.delete(0, 'end')
            selected_time_label.insert(0, "{}:{} {}".format(*time))
            selected_time_label.configure(state='disabled')
            top.destroy()

        ok_btn = customtkinter.CTkButton(top, text="ok", command=lambda: update_time(time_picker.time()))
        ok_btn.pack(pady=10)

    # create new booking window
    def booking_window():
        booking_win = customtkinter.CTkToplevel(root)
        booking_win.title('Add booking')
        booking_win.geometry('500x400')
        booking_win.wm_attributes('-topmost', True)

        # labels
        labels = ['Venue', 'Booked By', 'From Date', 'To Date', 'From Time', 'To Time']
        entries = []

        entries.append(dbms.last_booking_id() + 1)

        # Venue
        label = customtkinter.CTkLabel(booking_win, text='Venue')
        label.grid(row=1, column=0, padx=(80, 5), pady=5)

        entry = customtkinter.CTkEntry(booking_win)
        entry.grid(row=1, column=1, padx=(5, 0), pady=5)

        entries.append(entry)

        # Booked By
        entries.append(clubname)

        # From Date
        label = customtkinter.CTkLabel(booking_win, text='From Date')
        label.grid(row=3, column=0, padx=(80, 5), pady=5)

        selected_from_date = customtkinter.CTkEntry(booking_win)
        selected_from_date.configure(state='disabled')
        selected_from_date.grid(row=3, column=1, padx=(5, 0), pady=5)

        button = customtkinter.CTkButton(booking_win, text='Select Date',
                                         command=lambda: get_date(selected_from_date, booking_win))
        button.grid(row=3, column=2, padx=(5, 0), pady=5)

        entries.append(selected_from_date)

        # To Date
        label = customtkinter.CTkLabel(booking_win, text='To Date')
        label.grid(row=4, column=0, padx=(80, 5), pady=5)

        selected_to_date = customtkinter.CTkEntry(booking_win)
        selected_to_date.configure(state='disabled')
        selected_to_date.grid(row=4, column=1, padx=(5, 0), pady=5)

        button = customtkinter.CTkButton(booking_win, text='Select Date',
                                         command=lambda: get_date(selected_to_date, booking_win))
        button.grid(row=4, column=2, padx=(5, 0), pady=5)

        entries.append(selected_to_date)

        # From Time
        label = customtkinter.CTkLabel(booking_win, text='From Time')
        label.grid(row=5, column=0, padx=(80, 5), pady=5)

        selected_from_time = customtkinter.CTkEntry(booking_win)
        selected_from_time.configure(state='disabled')
        selected_from_time.grid(row=5, column=1, padx=(5, 0), pady=5)

        button = customtkinter.CTkButton(booking_win, text='Select Time',
                                         command=lambda: get_time(selected_from_time, booking_win))
        button.grid(row=5, column=2, padx=(5, 0), pady=5)

        entries.append(selected_from_time)

        # To Time
        label = customtkinter.CTkLabel(booking_win, text='To Time')
        label.grid(row=6, column=0, padx=(80, 5), pady=5)

        selected_to_time = customtkinter.CTkEntry(booking_win)
        selected_to_time.configure(state='disabled')
        selected_to_time.grid(row=6, column=1, padx=(5, 0), pady=5)

        button = customtkinter.CTkButton(booking_win, text='Select Time',
                                         command=lambda: get_time(selected_to_time, booking_win))
        button.grid(row=6, column=2, padx=(5, 0), pady=5)

        entries.append(selected_to_time)

        # Status
        entries.append('Pending')

        # submit button
        submit = customtkinter.CTkButton(booking_win, text='Submit', command=lambda: add_record(entries, booking_win))
        submit.grid(row=7, column=0, columnspan=2, padx=(100, 0), pady=5)

    def filter_table():
        pass

    def reset_filters():
        pass

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

    # button frame
    buttons_frame = customtkinter.CTkFrame(root)
    buttons_frame.pack(pady=20)

    # filter
    filter_btn = customtkinter.CTkButton(buttons_frame, text='Apply Date filter', command=lambda: filter_table())
    filter_btn.grid(row=1, column=1, padx=10)

    # reset filter
    reset_filter_btn = customtkinter.CTkButton(buttons_frame, text='Reset filter', command=lambda: reset_filters())
    reset_filter_btn.grid(row=1, column=2, padx=10)

    # add record
    add_record_btn = customtkinter.CTkButton(buttons_frame, text='Add Booking', command=lambda: booking_window())
    add_record_btn.grid(row=1, column=3, padx=10)

    # settings
    settings_btn = customtkinter.CTkButton(buttons_frame, text='Settings', command=lambda: settings_page(root))
    settings_btn.grid(row=1, column=5, padx=10)

    #logout
    logout_btn = customtkinter.CTkButton(buttons_frame, text='Logout', command=lambda : login_page(root))
    logout_btn.grid(row=1, column=6, padx=10)

    # Table Frame with border color
    table_frame = customtkinter.CTkFrame(root, border_color='darkblue', border_width=5)
    table_frame.pack(padx=20, pady=20, fill='both')

    # table style
    style = ttk.Style()
    style.theme_use('clam')
    style.configure('Treeview', fieldbackground='grey', rowheight='20')
    style.configure('Treeview.Heading',
                    background='#1f538d',  # Set the background color to dark blue
                    foreground='white',  # Set the text color to white
                    font=('Helvetica', 10)  # Set the font
                    )

    # table
    table = ttk.Treeview(table_frame, show='headings', style='Treeview')

    # style tags
    table.tag_configure('oddrow', background='grey16', foreground='white')
    table.tag_configure('evenrow', background='grey10', foreground='white')

    # table column
    table['columns'] = ('Booking ID', 'Venue', 'Booked By', 'From Date', 'To Date', 'From Time', 'To Time', 'Status')

    # format column
    table.column('Booking ID', anchor='center', width=20)
    table.column('Venue', anchor='center', width=80)
    table.column('Booked By', anchor='center', width=80)
    table.column('From Date', anchor='e', width=80)
    table.column('To Date', anchor='e', width=80)
    table.column('From Time', anchor='e', width=80)
    table.column('To Time', anchor='e', width=80)
    table.column('Status', anchor='center', width=80)

    # table heading
    table.heading('Booking ID', text='Booking ID', anchor='center')
    table.heading('Venue', text='Venue', anchor='center')
    table.heading('Booked By', text='Booked By', anchor='center')
    table.heading('From Date', text='From Date', anchor='center')
    table.heading('To Date', text='To Date', anchor='center')
    table.heading('From Time', text='Time', anchor='center')
    table.heading('To Time', text='Time', anchor='center')
    table.heading('Status', text='Status', anchor='center')

    # Vertical scrollbar
    vsb = customtkinter.CTkScrollbar(table_frame, orientation="vertical", command=table.yview)
    vsb.pack(side='right', fill='y', pady=10)

    # Horizontal scrollbar
    hsb = customtkinter.CTkScrollbar(table_frame, orientation="horizontal", command=table.xview)
    hsb.pack(side='bottom', fill='x', padx=10)

    # Configure the table to use the scrollbars
    table.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    table.pack(padx=5, pady=5, expand=True, fill='both')

    #adding error label incase booking is not possible
    error_label = customtkinter.CTkLabel(root, text='')
    error_label.pack(pady=20)

    # run refresh table
    refresh_table()

def settings_page(root):
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