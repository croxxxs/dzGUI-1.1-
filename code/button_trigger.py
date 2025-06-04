from tkinter import *

root = Tk()
root.geometry('400x300')
root.title('тест кнопок')
root.resizable(False,False)


buttons_frame = Frame(root,width=350,height=150)

def hello_config():
    word_label.configure(text='Привет!')
    return

def bye_config():
    word_label.configure(text='До свидания!')
    return

hello_button = Button(buttons_frame,width=25,text='Привет',command=hello_config)
bye_button = Button(buttons_frame,width=25,text='До свидания',command=bye_config)



hello_button.pack(side=LEFT)
bye_button.pack(side=RIGHT)




buttons_frame.pack(side='top')
buttons_frame.pack_propagate(False)


label_frame = Frame(root,width=350,height=150)

word_label = Label(label_frame,text=None,font=('Arial',32))
word_label.pack(anchor='c')


label_frame.pack(side='bottom')
label_frame.pack_propagate(False)

root.mainloop()