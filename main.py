from tkinter import *
from tkinter import messagebox
import pickle

root = Tk()
root.title("Password")
root.geometry("600x550")

root.option_add('*Font', 'Calibri')
root.option_add('*Background', 'white')

label_error = None

frame = Frame(root, bd=10)
frame.place(relx=0.15, rely=0.2, relwidth=0.7, relheight=0.6)
label = Label(frame, text='Sing Up', font='16')
label.place(relwidth=1, relheight=0.1)
label_login = Label(frame, text="Login:")
label_login.place(rely=0.2, relwidth=0.35, relheight=0.1)
login_entry = Entry(frame)
login_entry.place(rely=0.2, relx=0.4, relwidth=0.55, relheight=0.1)

label_password1 = Label(frame, text='Password: ')
label_password1.place(rely=0.35, relwidth=0.35, relheight=0.2)
password1_entry = Entry(frame, show='*')
password1_entry.place(rely=0.4, relx=0.4, relwidth=0.55)

def password():
    global label_error
    error = ''
    if label_error:
        label_error.destroy()
    if len(login_entry.get()) == 0:
        error = 'Login Error'
        print(False)
    elif len(password1_entry.get()) < 6:
        error = 'Password Error'
        print(False)
    else:
        password = str(password1_entry.get())
        for i in range(10):
            if password.find(str(i)) != -1:
                print(True)
                return True

        print(False)
        error = 'Password Error'
        return False


    label_error = Label(frame, text=error, fg='red')
    label_error.place(rely=0.9)

button = Button(frame, text='Sing up', command=password)
button.place(relx=0.36, rely=0.8, relwidth=0.3)

root.mainloop()