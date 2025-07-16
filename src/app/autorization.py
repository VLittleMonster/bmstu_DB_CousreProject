import psycopg2
from connection import connect, disconnect
from requester import exec_request, exec_active_request
from alcomarket import alcomarket
from tkinter import *
from tkinter import messagebox
from color import MAIN_COLOR, FONT_COLOR, LIST_COLOR

def login(login_entry, password_entry):
    login = login_entry.get()
    password = password_entry.get()
    
    request = "SELECT user_login, user_password, user_grant FROM users"
    result = exec_request(request)
    
    flag = 0
    usertype = 0
    
    for i in range(len(result)):
        if login == result[i][0] and password == result[i][1]:
            flag = 1
            usertype = result[i][2]
    
    if flag:
        alcomarket(login, password, usertype)
    else:
        messagebox.showerror('Ошибка входа', 'Неверный логин или пароль!')

def confirm_registration(name_entry, login_entry, password_entry, password_entry2, usertype_var):
    name = name_entry.get()
    login = login_entry.get()
    password = password_entry.get()
    password2 = password_entry2.get()
    usertype = int(usertype_var.get())
    
    if name == '' or login == '' or password == '':
        messagebox.showerror('Ошибка формы', 'Имя пользователя, логин и пароль должны быть заполнены!')
    
    if password != password2:
        messagebox.showerror('Ошибка', 'Пароли не совпадают!')
    
    request = "SELECT user_login, user_password FROM users"
    result = exec_request(request)
    
    flag = 0
    
    for i in range(len(result)):
        if login == result[i][0]:
            flag = 1
    
    if flag:
        messagebox.showerror('Ошибка регистрации', 'Пользователь с логином ' + str(login) + ' уже существует!')
    else:
        try:
            request = "INSERT INTO users(user_nick, user_login, user_password, user_grant)\
            VALUES ('" + str(name) + "', '" + str(login) + "', '" + str(password) + "', " + str(usertype) + ");"
            exec_active_request(request)
            cart = 'cart' + login
            request = "CREATE TABLE " + cart + "(id_item INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY, id_alcohol INT NOT NULL UNIQUE, qty INT NOT NULL);"
            exec_active_request(request)
            request = "ALTER TABLE " + cart + " ADD FOREIGN KEY (id_alcohol) REFERENCES alcohol(id_alcohol);"
            exec_active_request(request)
            request = "CREATE USER " + login + " WITH PASSWORD '" + password + "';"
            exec_active_request(request)
            request = "GRANT CONNECT ON DATABASE alcomarket TO " + login + ';'
            request = "GRANT SELECT, UPDATE, INSERT, DELETE ON TABLE " + cart + " TO " + '"' + login + '";'
            exec_active_request(request)
            
            if usertype == 1:
                request = 'GRANT "buyer" TO ' + login + ';'
                exec_active_request(request)
            elif usertype == 2:
                request = 'GRANT "manager" TO ' + login + ';'
                exec_active_request(request)
            elif usertype == 3:
                request = 'GRANT "general_manager" TO ' + login + ';'
                exec_active_request(request)
                
        except:
            messagebox.showerror('Ошибка регистрации', 'Что-то пошло не так!')
            return()
    
    if flag == 0:
        alcomarket(login, password, usertype)
        
    
def registration(root):
    root.iconify()
    
    reg = Toplevel()
    reg.grab_set()
    
    width = reg.winfo_screenwidth()
    height = reg.winfo_screenheight()
    x = (width - 750) / 2
    y = (height - 440) / 2

    icon = PhotoImage(file = 'icon.png')
    reg.iconphoto(False, icon)
    reg.geometry('750x440+%d+%d' % (x, y))
    reg.title('Регистрация')
    reg.resizable(False, False)
    reg.configure(background = MAIN_COLOR)

    alco_screen = PhotoImage(file = 'alco_screen.png')
    screen = Label(reg, image = alco_screen, bg = MAIN_COLOR)
    screen.image_ref = alco_screen
    screen.pack()
    screen.place(x = -5, y = -5)

    reg_label = Label(reg, text='Регистрация', 
                    anchor = 'c', 
                    bg = MAIN_COLOR, 
                    fg = FONT_COLOR, 
                    font='consolas 18 bold')
    reg_label.place(x = 485, y = 50)
    
    name_label = Label(reg, text='Имя пользователя', 
                    anchor = 'w', 
                    bg = MAIN_COLOR, 
                    fg = FONT_COLOR, 
                    font='consolas 10')
    name_label.place(x = 485, y = 100)

    name_entry = Entry(reg, width = 24) 
    name_entry.place(x = 485, y = 120)

    login_label = Label(reg, text='Логин', 
                    anchor = 'w', 
                    bg = MAIN_COLOR, 
                    fg = FONT_COLOR, 
                    font='consolas 10')
    login_label.place(x = 485, y = 140)

    login_entry = Entry(reg, width = 24) 
    login_entry.place(x = 485, y = 160)

    password_label = Label(reg, text='Пароль', 
                    anchor = 'w', 
                    bg = MAIN_COLOR, 
                    fg = FONT_COLOR, 
                    font='consolas 10')
    password_label.place(x = 485, y = 180)

    password_entry = Entry(reg, width = 24, show = '*') 
    password_entry.place(x = 485, y = 200)
    
    password_label2 = Label(reg, text='Подтвердите пароль', 
                    anchor = 'w', 
                    bg = MAIN_COLOR, 
                    fg = FONT_COLOR, 
                    font='consolas 10')
    password_label2.place(x = 485, y = 220)

    password_entry2 = Entry(reg, width = 24, show = '*')  
    password_entry2.place(x = 485, y = 240)
    
    user_label = Label(reg, text='Тип пользователя', 
                    anchor = 'w', 
                    bg = MAIN_COLOR, 
                    fg = FONT_COLOR, 
                    font='consolas 10')
    user_label.place(x = 485, y = 270)
    
    usertype_var = IntVar()
    usertype_var.set(1)
    
    buyer_rbtn_label = Radiobutton(reg, text = "Покупатель", 
                                   variable = usertype_var, 
                                   value = 1, 
                                   font=("consolas", 11), bg = MAIN_COLOR, fg =FONT_COLOR)
    buyer_rbtn_label.place(x = 485, y = 290)
    
    seller_rbtn_label = Radiobutton(reg, text = "Менеджер продаж", 
                                   variable = usertype_var, 
                                   value = 2, 
                                   font=("consolas", 11), bg = MAIN_COLOR, fg =FONT_COLOR)
    seller_rbtn_label.place(x = 485, y = 310)
    
    manager_rbtn_label = Radiobutton(reg, text = "Главный менеджер", 
                                   variable = usertype_var, 
                                   value = 3, 
                                   font=("consolas", 11), bg = MAIN_COLOR, fg =FONT_COLOR)
    manager_rbtn_label.place(x = 485, y = 330)

    reg_btn = Button(reg, text='Зарегистрироваться',
                        width=20,
                        height=1,
                        font='consolas 10',
                        bg = MAIN_COLOR,
                        fg = FONT_COLOR,
                        command=lambda:confirm_registration(name_entry, login_entry, 
                                                            password_entry, password_entry2, 
                                                            usertype_var))
    reg_btn.place(anchor = 'w', x = 485, y = 380)
    

def autorization():
    root = Tk()

    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    x = (width - 750) / 2
    y = (height - 440) / 2

    icon = PhotoImage(file = 'icon.png')
    root.iconphoto(False, icon)
    root.geometry('750x440+%d+%d' % (x, y))
    root.title('Авторизация')
    root.resizable(False, False)
    root.configure(background = MAIN_COLOR)

    alco_screen = PhotoImage(file = 'alco_screen.png')
    screen = Label(root, image = alco_screen, bg = MAIN_COLOR)
    screen.image_ref = alco_screen
    screen.pack()
    screen.place(x = -5, y = -5)

    enter_label = Label(text='Вход', 
                    anchor = 'c', 
                    bg = MAIN_COLOR, 
                    fg = FONT_COLOR, 
                    font='consolas 18 bold')
    enter_label.place(x = 530, y = 50)

    login_label = Label(text='Логин', 
                    anchor = 'w', 
                    bg = MAIN_COLOR, 
                    fg = FONT_COLOR, 
                    font='consolas 10')
    login_label.place(x = 485, y = 100)

    login_entry = Entry(root, width = 24) 
    login_entry.place(x = 485, y = 120)

    password_label = Label(text='Пароль', 
                    anchor = 'w', 
                    bg = MAIN_COLOR, 
                    fg = FONT_COLOR, 
                    font='consolas 10')
    password_label.place(x = 485, y = 140)

    password_entry = Entry(root, width = 24, show = '*') 
    password_entry.place(x = 485, y = 160)

    login_btn = Button(text='Войти',
                        width=20,
                        height=1,
                        font='consolas 10',
                        bg = MAIN_COLOR,
                        fg = FONT_COLOR,
                        command=lambda:login(login_entry, password_entry))
    login_btn.place(anchor = 'w', x = 485, y = 210)

    reg_label = Label(text='Нет аккаунта?', 
                    anchor = 'w', 
                    bg = MAIN_COLOR, 
                    fg = FONT_COLOR, 
                    font='consolas 10')
    reg_label.place(x = 485, y = 240)

    reg_btn = Button(text='Зарегистрироваться',
                        width=20,
                        height=1,
                        font='consolas 10',
                        bg = MAIN_COLOR,
                        fg = FONT_COLOR,
                        command=lambda:registration(root))
    reg_btn.place(anchor = 'w', x = 485, y = 275)

    root.mainloop()
    
autorization()