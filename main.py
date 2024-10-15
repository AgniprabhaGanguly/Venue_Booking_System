import customtkinter
import pages

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.title('Venue Booking System')
root.geometry('1280x720')

#initial page
pages.login_page(root)

root.mainloop()