from tkinter import*
from PIL import ImageTk
window = Tk()
window.geometry('800x500')
window.configure(background='gray')




# show_button = Button(window, image=show_image)

password_entry = Entry(window, highlightthickness=2.4, bd=2, bg='white', fg='black', relief=FLAT, show='*', font=('', 18))
password_entry.pack(pady=200)



window.mainloop()