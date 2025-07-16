import psycopg2
from connection import connect, disconnect
from requester import exec_request, exec_active_request, exec_user_request, exec_user_active_request
from tkinter import *
from tkinter import messagebox
from alco_vok import alco_vok
from color import MAIN_COLOR, FONT_COLOR, LIST_COLOR

def card(alco_list, alcohol, login, password, usertype):
    
    if not len(alco_list.curselection()):
        return
    
    card = Toplevel()
    card.grab_set()
    
    width = card.winfo_screenwidth()
    height = card.winfo_screenheight()
    x = (width - 700) / 2
    y = (height - 400) / 2
    
    icon = PhotoImage(file = 'icon.png')
    card.iconphoto(True, icon)
    card.geometry('700x400+%d+%d' % (x, y))
    card.title('Карточка алкоголя')
    card.resizable(True, True)
    card.configure(background = MAIN_COLOR)
    
    alcohol_unit = alcohol[alco_list.curselection()[0]]
    name = alcohol_unit[1]
    category = alco_vok[alcohol_unit[2]]
    subcategory = alco_vok[alcohol_unit[3]]
    brand = str(alcohol_unit[4])
    factory = str(alcohol_unit[5])
    strength = str(alcohol_unit[6])
    price = str(alcohol_unit[7])
    volume = str(alcohol_unit[8])
    qty = str(alcohol_unit[9])
    pack = str(alcohol_unit[10])
    filtration = str(alcohol_unit[11])
    region = str(alcohol_unit[12])
    sort = str(alcohol_unit[13])
    harvest_year = str(alcohol_unit[14])
    sugar = str(alcohol_unit[15])
    
    request = 'SELECT brand_name, country FROM brand WHERE id_brand = ' + brand
    brand_res = exec_user_request(request, login, password)
    
    request = 'SELECT factory_name, country FROM factory WHERE id_factory = ' + factory
    factory_res = exec_user_request(request, login, password)
    
    name_label = Label(card, text = 'Название: ' + name,
                    anchor = 'c', 
                    bg = MAIN_COLOR,
                    font='consolas 12')
    name_label.place(x = 10, y = 10)
    
    category_label = Label(card, text = 'Категория: ' + category,
                    anchor = 'c', 
                    bg = MAIN_COLOR,
                    font='consolas 12')
    category_label.place(x = 10, y = 30)
    
    subcategory_label = Label(card, text = 'Подкатегория: ' + subcategory,
                    anchor = 'c', 
                    bg = MAIN_COLOR,
                    font='consolas 12')
    subcategory_label.place(x = 10, y = 50)
    
    brand_label = Label(card, text = 'Бренд: ' + brand_res[0][0] + '(' + brand_res[0][1] + ')',
                    anchor = 'c', 
                    bg = MAIN_COLOR,
                    font='consolas 12')
    brand_label.place(x = 10, y = 70)
    
    factory_label = Label(card, text = 'Производитель: ' + factory_res[0][0],
                    anchor = 'c', 
                    bg = MAIN_COLOR,
                    font='consolas 12')
    factory_label.place(x = 10, y = 90)
    
    strength_label = Label(card, text = 'Крепость: ' + strength + '%',
                    anchor = 'c', 
                    bg = MAIN_COLOR,
                    font='consolas 12')
    strength_label.place(x = 10, y = 110)
    
    volume_label = Label(card, text = 'Объем: ' + volume + ' л',
                    anchor = 'c', 
                    bg = MAIN_COLOR,
                    font='consolas 12')
    volume_label.place(x = 10, y = 130)
    
    
    price_label = Label(card, text = 'Цена:               ₽',
                    anchor = 'c', 
                    bg = MAIN_COLOR,
                    font='consolas 12')
    price_label.place(x = 10, y = 150)
    
    price_entry = Entry(card, width = 10) 
    price_entry.place(x = 123, y = 152)
    price_entry.insert(0, price)
    price_entry.config(state="readonly")
    
    qty_label = Label(card, text = 'Количество:',
                    anchor = 'c', 
                    bg = MAIN_COLOR,
                    font='consolas 12')
    qty_label.place(x = 10, y = 170)
    
    qty_entry = Entry(card, width = 10) 
    qty_entry.place(x = 123, y = 174)
    qty_entry.insert(0, qty)
    qty_entry.config(state="readonly")
    
    
    info_label = Label(card, text = 'ДОПОЛНИТЕЛЬНАЯ ИНФОРМАЦИЯ',
                    anchor = 'c', 
                    bg = MAIN_COLOR,
                    font='consolas 12')
    info_label.place(x = 430, y = 10)
    
    if category == 'Пиво':
        if pack == '1':
            pack = 'стекло'
        elif pack == '2':
            pack = 'банка'
        
        if filtration == '1':
            filtration = 'фильтрованное'
        elif filtration == '2':
            filtration = 'нефильтрованное'
            
        pack_label = Label(card, text = 'Тара: ' + pack,
                    anchor = 'c', 
                    bg = MAIN_COLOR,
                    font='consolas 12')
        pack_label.place(x = 430, y = 30)
        
        filtration_label = Label(card, text = 'Фильтрация: ' + filtration,
                    anchor = 'c', 
                    bg = MAIN_COLOR,
                    font='consolas 12')
        filtration_label.place(x = 430, y = 50)
    
    if category == 'Вино' or category == 'Игристое':
        
        request = 'SELECT region_name FROM region WHERE id_region = ' + region + ';'
        result = exec_user_request(request, login, password)
        region = result[0][0]
        
        region_label = Label(card, text = 'Регион: ' + region,
                    anchor = 'c', 
                    bg = MAIN_COLOR,
                    font='consolas 12')
        region_label.place(x = 430, y = 30)
        
        sort_label = Label(card, text = 'Сорт: ' + sort,
                    anchor = 'c', 
                    bg = MAIN_COLOR,
                    font='consolas 12')
        sort_label.place(x = 430, y = 50)
        
        harvest_label = Label(card, text = 'Год урожая: ' + harvest_year,
                    anchor = 'c', 
                    bg = MAIN_COLOR,
                    font='consolas 12')
        harvest_label.place(x = 430, y = 70)
    
        if sugar == '1':
            sugar = 'полусладкое'
        elif sugar == '2':
            sugar = 'полусухое'
        elif sugar == '3':
            sugar = 'сухое'
        elif sugar == '4':
            sugar = 'брют'
        
        sugar_label = Label(card, text = 'Сахар: ' + sugar,
                    anchor = 'c', 
                    bg = MAIN_COLOR,
                    font='consolas 12')
        sugar_label.place(x = 430, y = 90)    
    
    def change_price():
        try:
            new_price = str(float(price_entry.get()))
            answer = messagebox.askyesno(title="Изменение", 
            message="Вы уверены что хотите изменить цену на " + new_price + "?")
            
            if answer:
                request = 'UPDATE alcohol SET price = ' + new_price + ' WHERE id_alcohol = ' + str(alcohol_unit[0]) + ';'
                exec_user_active_request(request, login, password)
            
        except:
            messagebox.showerror('Ошибка!', 'Неверно указана цена!')
            
    def change_qty():
        try:
            new_qty = str(int(qty_entry.get()))
            answer = messagebox.askyesno(title="Изменение", 
            message="Вы уверены что хотите изменить количество на " + new_qty + "?")
            
            if answer:
                request = 'UPDATE alcohol SET qty = ' + new_qty + ' WHERE id_alcohol = ' + str(alcohol_unit[0]) + ';'
                exec_user_active_request(request, login, password)
        except:
            messagebox.showerror('Ошибка!', 'Неверно указано количество!')
            
    def delete_alcohol():
        
        answer = messagebox.askyesno(title="Удаление", 
                                     message="Вы уверены что хотите удалить выбранный алкоголь?")
        if answer:
            request = 'DELETE FROM alcohol WHERE id_alcohol = ' + str(alcohol_unit[0]) + ';'
            exec_user_active_request(request, login, password)
            card.destroy()
    
    if usertype != 1:
        
        price_entry.config(state='normal')
        qty_entry.config(state='normal')
        
        price_btn = Button(card, text='Изменить',
                            width=20,
                            height=1,
                            font='consolas 8',
                            bg = MAIN_COLOR,
                            command=lambda:change_price())
        price_btn.place(anchor = 'w', x = 220, y = 162)
        
        qty_btn = Button(card, text='Изменить',
                            width=20,
                            height=1,
                            font='consolas 8',
                            bg = MAIN_COLOR,
                            command=lambda:change_qty())
        qty_btn.place(anchor = 'w', x = 220, y = 184)
    
    if usertype == 3:
        
        del_btn = Button(card, text='Удалить алкоголь',
                            width=20,
                            height=1,
                            font='consolas 10',
                            bg = MAIN_COLOR,
                            command=lambda:delete_alcohol())
        del_btn.place(anchor = 'w', x = 10, y = 215)