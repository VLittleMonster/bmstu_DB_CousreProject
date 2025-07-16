import psycopg2
from connection import connect, disconnect
from requester import exec_request, exec_active_request, exec_user_request, exec_user_active_request
from tkinter import *
from tkinter import messagebox
from alco_vok import alco_vok
from color import MAIN_COLOR, FONT_COLOR, LIST_COLOR

def transform_record(record):
    
    result = '{:35.35s}| {:<3d}|'.format(\
        record[0], record[1])
    
    return result

def cart(login, password):
    cart = Toplevel()
    cart.grab_set()
    
    width = cart.winfo_screenwidth()
    height = cart.winfo_screenheight()
    x = (width - 600) / 2
    y = (height - 250) / 2
    
    icon = PhotoImage(file = 'icon.png')
    cart.iconphoto(True, icon)
    cart.geometry('600x250+%d+%d' % (x, y))
    cart.title('Корзина')
    cart.resizable(True, True)
    cart.configure(background = MAIN_COLOR)
    
    def reload():
        cart_list.delete(0, cart_list.size())
        
        request = "SELECT alcohol_name, cart" + login + ".qty FROM alcohol JOIN cart" + login + " ON alcohol.id_alcohol = cart" + login + ".id_alcohol ORDER BY alcohol_name;"
        result = exec_user_request(request, login, password)
    
        for i in range(len(result)):
            cart_list.insert(END, transform_record(result[i]))
            
    def update_cart(mode):
        
        if not len(cart_list.curselection()):
            return
        
        request = "SELECT id_item, cart" + login + ".qty FROM alcohol JOIN cart" + login + " ON alcohol.id_alcohol = cart" + login + ".id_alcohol ORDER BY alcohol_name;"
        result = exec_user_request(request, login, password)
        
         
        item_id = str(result[cart_list.curselection()[0]][0])
        
        if mode == 1:
            request = "CALL UpdateCart('" + '"cart' + login + '"' + "', 1, " + item_id + ');'
        if mode == -1:
            request = "CALL UpdateCart('" + '"cart' + login + '"' + "', -1, " + item_id + ');'
        
        exec_user_active_request(request, login, password)
        
        reload()
            
        
            
    request = "SELECT user_nick FROM users WHERE user_login = '" + login + "';"
    result = exec_request(request) 
            
    user_label = Label(cart, text= 'Приветсвуем в корзине, ' + result[0][0] + '!', 
                    anchor = 'c', 
                    bg = MAIN_COLOR,
                    font='consolas 11')
    user_label.place(x = 30, y = 9)
    
    alco_label = Label(cart, text= 'Наименование алкоголя              Количество', 
                    anchor = 'c', 
                    bg = MAIN_COLOR,
                    font='consolas 10')
    alco_label.place(x = 15, y = 30)
    
    cart_scroll = Scrollbar(cart)
    cart_scroll.place(x = 480, y = 50, height = 150)
    
    cart_list = Listbox(cart, 
                        yscrollcommand = cart_scroll.set,
                        bg = LIST_COLOR,
                        fg = FONT_COLOR,
                        selectbackground = MAIN_COLOR,
                        font = 'consolas 10')
    cart_list.place(x = 15, y = 50, width = 460, height = 150)
    
    cart_scroll.config(command = cart_list.yview)
    
    plus_btn = Button(cart, text='+',
                        width=4,
                        height=1,
                        font='consolas 16',
                        bg = MAIN_COLOR,
                        command=lambda:update_cart(1))
    plus_btn.place(anchor = 'c', x = 550, y = 100)
    
    minus_btn = Button(cart, text='-',
                        width=4,
                        height=1,
                        font='consolas 16',
                        bg = MAIN_COLOR,
                        command=lambda:update_cart(-1))
    minus_btn.place(anchor = 'c', x = 550, y = 150)
    
    reload()