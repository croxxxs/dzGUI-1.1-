from tkinter import *


root = Tk()
root.title("Форма регистрации")
root.geometry("400x300")
root.resizable(False,False)

header = Label(root, text="Регистрация", font=("Arial", 16))
header.pack(pady=10)


form_frame = Frame(root)
form_frame.pack(padx=20, pady=10,side='top')


label_name = Label(form_frame, text="Имя:")
entry_name = Entry(form_frame)
label_name.grid(row=0,column=0)
entry_name.grid(row=0,column=1)

label_surname = Label(form_frame, text="Фамилия:")
entry_surname = Entry(form_frame)
label_surname.grid(row=1,column=0)
entry_surname.grid(row=1,column=1)

label_email = Label(form_frame, text="Электронная почта:")
entry_email = Entry(form_frame)
label_email.grid(row=2,column=0)
entry_email.grid(row=2,column=1)


label_password = Label(form_frame, text="Пароль:")
entry_password = Entry(form_frame, show='*')
label_password.grid(row=3,column=0)
entry_password.grid(row=3,column=1)



button_frame = Frame(root)
button_frame.pack(pady=10,side="bottom")

register_button = Button(button_frame, text="Зарегистрироваться")

register_button.pack(anchor='center')


root.mainloop()