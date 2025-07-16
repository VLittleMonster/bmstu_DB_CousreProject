import psycopg2
from connection import connect, disconnect, user_connect
from requester import exec_request, exec_user_request, exec_user_active_request
from card import card
from cart import cart
from tkinter import *
from tkinter import messagebox
from manager import manager_mode
from color import MAIN_COLOR, FONT_COLOR, LIST_COLOR

def transform_record(record, region_vok):
    
    result = '{:35.35s}| {:<3d}%   |{:8.02f} ₽|{:5.2f} | {:<3d} ||'.format(\
        record[1], record[6], record[7], record[8], record[9])
    
    pack = str(record[10])
    filtration = str(record[11])
    id_region = str(record[12])
    region = ''
    sort = str(record[13])
    harvest_year = str(record[14])
    sugar = str(record[15])
    
    if pack == 'None':
        pack = ''
    elif pack == '1':
        pack = 'стекло'
    elif pack == '2':
        pack = 'банка'
        
    if filtration == 'None':
        filtration = ''
    elif filtration == '1':
        filtration = 'фильтрованное'
    elif filtration == '2':
        filtration = 'нефильтрованное'
        
    if id_region == 'None':
        region = ''
    else:
        region = region_vok.get(int(id_region))
        
    if sort == 'None':
        sort = ''
    
    if harvest_year == 'None':
        harvest_year = ''
        
    if sugar == 'None':
        sugar = ''
    elif sugar == '1':
        sugar = 'полусладкое'
    elif sugar == '2':
        sugar = 'полусухое'
    elif sugar == '3':
        sugar = 'сухое'
    elif sugar == '4':
        sugar = 'брют'
        
    result = result + '{:7.7s}|{:15.15s}|{:10.10s}|{:13.13s}|{:5.5s}|{:11.11s}'.format(\
        pack, filtration, region, sort, harvest_year, sugar)
    
    return result

def alcomarket(login, password, usertype):
    alcomarket = Toplevel() #заменить на Toplevel()
    alcomarket.grab_set()
    
    width = alcomarket.winfo_screenwidth() - 15
    height = alcomarket.winfo_screenheight() - 40
    
    icon = PhotoImage(file = 'icon.png')
    alcomarket.iconphoto(True, icon)
    alcomarket.geometry('%dx%d+0+0' % (width, height))
    alcomarket.title('Alcomarket')
    alcomarket.resizable(True, True)
    alcomarket.configure(background = MAIN_COLOR)
    
    request = 'SELECT * FROM alcohol;'
    alcohol = exec_user_request(request, login, password)
    
    request = 'SELECT id_region, region_name FROM region'
    region = exec_user_request(request, login, password)
    region_vok = {}
    for i in range(len(region)):
        region_vok[region[i][0]] = region[i][1]
    
    reload_btn = Button(alcomarket, text='Найти',
                        width=20,
                        height=1,
                        font='consolas 8',
                        bg = MAIN_COLOR,
                        command=lambda:reload())
    reload_btn.place(anchor = 'ne', x = 600, y = 7)
    
    search_entry = Entry(alcomarket, width = 50) 
    search_entry.place(x = 150, y = 8)
    
    alco_label = Label(alcomarket, text='Название\
                           Крепость Цена       Объем  Кол-во '\
                               ' Тара    Фильтрация      Регион     Сорт         Урожай Сахар', 
                    anchor = 'c', 
                    bg = MAIN_COLOR,
                    font='consolas 10')
    alco_label.place(x = 150, y = 30)
    
    
    alco_scroll = Scrollbar(alcomarket)
    alco_scroll.place(x = 1115, y = 50, height = 650)
    
    alco_list = Listbox(alcomarket, 
                        yscrollcommand = alco_scroll.set,
                        bg = LIST_COLOR,
                        fg = FONT_COLOR,
                        selectbackground = MAIN_COLOR,
                        font = 'consolas 10')
    alco_list.place(x = 150, y = 50, width = 960, height = 650)
    
    for i in range(len(alcohol)):
        alco_list.insert(END, transform_record(alcohol[i], region_vok))
    
    alco_scroll.config(command = alco_list.yview)
    
    
    
    ###### ВЫБОРКА АЛКОГОЛЯ #######
    
    def main_wine_toggle():
        if wvar1.get():
            w11.select()
            w12.select()
            w13.select()
            w14.select()
            w15.select()
        else:
            w11.deselect()
            w12.deselect()
            w13.deselect()
            w14.deselect()
            w15.deselect()
    
    def child_wine_toggle():
        if wvar11.get() and wvar12.get() and wvar13.get() and wvar14.get() and wvar15.get():
            w1.select()
        else:
            w1.deselect()
    
    wvar1 = BooleanVar()
    wvar1.set(True)
    wvar11 = BooleanVar()
    wvar11.set(True)
    wvar12 = BooleanVar()
    wvar12.set(True)
    wvar13 = BooleanVar()
    wvar13.set(True)
    wvar14 = BooleanVar()
    wvar14.set(True)
    wvar15 = BooleanVar()
    wvar15.set(True)
    
    w11 = Checkbutton(alcomarket, bg = MAIN_COLOR, text = 'красное вино', var = wvar11, command = lambda:child_wine_toggle())
    w12 = Checkbutton(alcomarket, bg = MAIN_COLOR, text = 'белое вино', var = wvar12, command = lambda:child_wine_toggle())
    w13 = Checkbutton(alcomarket, bg = MAIN_COLOR, text = 'розовое вино', var = wvar13, command = lambda:child_wine_toggle())
    w14 = Checkbutton(alcomarket, bg = MAIN_COLOR, text = 'вермут', var = wvar14, command = lambda:child_wine_toggle())
    w15 = Checkbutton(alcomarket, bg = MAIN_COLOR, text = 'портвейн', var = wvar15, command = lambda:child_wine_toggle())
    
    w11.place(x=20, y=80)
    w12.place(x=20, y=100)
    w13.place(x=20, y=120)
    w14.place(x=20, y=140)
    w15.place(x=20, y=160)
    
    w1 = Checkbutton(alcomarket, bg = MAIN_COLOR, text = 'вино', var = wvar1, command = lambda:main_wine_toggle())
    w1.place(x=10, y=60)
    
    def main_champ_toggle():
        if cvar1.get():
            c11.select()
            c12.select()
            c13.select()
            c14.select()
            c15.select()
        else:
            c11.deselect()
            c12.deselect()
            c13.deselect()
            c14.deselect()
            c15.deselect()
    
    def child_champ_toggle():
        if cvar11.get() and cvar12.get() and cvar13.get() and cvar14.get() and cvar15.get():
            c1.select()
        else:
            c1.deselect()
    
    cvar1 = BooleanVar()
    cvar1.set(True)
    cvar11 = BooleanVar()
    cvar11.set(True)
    cvar12 = BooleanVar()
    cvar12.set(True)
    cvar13 = BooleanVar()
    cvar13.set(True)
    cvar14 = BooleanVar()
    cvar14.set(True)
    cvar15 = BooleanVar()
    cvar15.set(True)
    
    c11 = Checkbutton(alcomarket, bg = MAIN_COLOR, text = 'шампанское', var = cvar11, command = lambda:child_champ_toggle())
    c12 = Checkbutton(alcomarket, bg = MAIN_COLOR, text = 'игристое вино', var = cvar12, command = lambda:child_champ_toggle())
    c13 = Checkbutton(alcomarket, bg = MAIN_COLOR, text = 'просекко', var = cvar13, command = lambda:child_champ_toggle())
    c14 = Checkbutton(alcomarket, bg = MAIN_COLOR, text = 'асти', var = cvar14, command = lambda:child_champ_toggle())
    c15 = Checkbutton(alcomarket, bg = MAIN_COLOR, text = 'ламбруско', var = cvar15, command = lambda:child_champ_toggle())
    
    c11.place(x=20, y=210)
    c12.place(x=20, y=230)
    c13.place(x=20, y=250)
    c14.place(x=20, y=270)
    c15.place(x=20, y=290)
    
    c1 = Checkbutton(alcomarket, bg = MAIN_COLOR, text = 'игристое', var = cvar1, command = lambda:main_champ_toggle())
    c1.place(x=10, y=190)
    
    def main_hard_toggle():
        if hvar1.get():
            h11.select()
            h12.select()
            h13.select()
            h14.select()
            h15.select()
            h16.select()
            h17.select()
            h18.select()
            h19.select()
        else:
            h11.deselect()
            h12.deselect()
            h13.deselect()
            h14.deselect()
            h15.deselect()
            h16.deselect()
            h17.deselect()
            h18.deselect()
            h19.deselect()
    
    def child_hard_toggle():
        if hvar11.get() and hvar12.get() and hvar13.get() and hvar14.get()\
            and hvar15.get() and hvar16.get() and hvar17.get() and hvar18.get() and hvar19.get():
            h1.select()
        else:
            h1.deselect()
    
    hvar1 = BooleanVar()
    hvar1.set(True)
    hvar11 = BooleanVar()
    hvar11.set(True)
    hvar12 = BooleanVar()
    hvar12.set(True)
    hvar13 = BooleanVar()
    hvar13.set(True)
    hvar14 = BooleanVar()
    hvar14.set(True)
    hvar15 = BooleanVar()
    hvar15.set(True)
    hvar16 = BooleanVar()
    hvar16.set(True)
    hvar17 = BooleanVar()
    hvar17.set(True)
    hvar18 = BooleanVar()
    hvar18.set(True)
    hvar19 = BooleanVar()
    hvar19.set(True)
    
    h11 = Checkbutton(alcomarket, bg = MAIN_COLOR, text = 'ром', var = hvar11, command = lambda:child_hard_toggle())
    h12 = Checkbutton(alcomarket, bg = MAIN_COLOR, text = 'виски', var = hvar12, command = lambda:child_hard_toggle())
    h13 = Checkbutton(alcomarket, bg = MAIN_COLOR, text = 'коньяк', var = hvar13, command = lambda:child_hard_toggle())
    h14 = Checkbutton(alcomarket, bg = MAIN_COLOR, text = 'ликер', var = hvar14, command = lambda:child_hard_toggle())
    h15 = Checkbutton(alcomarket, bg = MAIN_COLOR, text = 'водка', var = hvar15, command = lambda:child_hard_toggle())
    h16 = Checkbutton(alcomarket, bg = MAIN_COLOR, text = 'текила', var = hvar16, command = lambda:child_hard_toggle())
    h17 = Checkbutton(alcomarket, bg = MAIN_COLOR, text = 'джин', var = hvar17, command = lambda:child_hard_toggle())
    h18 = Checkbutton(alcomarket, bg = MAIN_COLOR, text = 'абсент', var = hvar18, command = lambda:child_hard_toggle())
    h19 = Checkbutton(alcomarket, bg = MAIN_COLOR, text = 'саке', var = hvar19, command = lambda:child_hard_toggle())
    
    h11.place(x=20, y=340)
    h12.place(x=20, y=360)
    h13.place(x=20, y=380)
    h14.place(x=20, y=400)
    h15.place(x=20, y=420)
    h16.place(x=20, y=440)
    h17.place(x=20, y=460)
    h18.place(x=20, y=480)
    h19.place(x=20, y=500)
    
    h1 = Checkbutton(alcomarket, bg = MAIN_COLOR, text = 'крепкий алкоголь', var = hvar1, command = lambda:main_hard_toggle())
    h1.place(x=10, y=320)
    
    def main_beer_toggle():
        if bvar1.get():
            b11.select()
            b12.select()
            b13.select()
            b14.select()
        else:
            b11.deselect()
            b12.deselect()
            b13.deselect()
            b14.deselect()
    
    def child_beer_toggle():
        if bvar11.get() and bvar12.get() and bvar13.get() and bvar14.get():
            b1.select()
        else:
            b1.deselect()
    
    bvar1 = BooleanVar()
    bvar1.set(True)
    bvar11 = BooleanVar()
    bvar11.set(True)
    bvar12 = BooleanVar()
    bvar12.set(True)
    bvar13 = BooleanVar()
    bvar13.set(True)
    bvar14 = BooleanVar()
    bvar14.set(True)
    
    b11 = Checkbutton(alcomarket, bg = MAIN_COLOR, text = 'светлое пиво', var = bvar11, command = lambda:child_beer_toggle())
    b12 = Checkbutton(alcomarket, bg = MAIN_COLOR, text = 'темное пиво', var = bvar12, command = lambda:child_beer_toggle())
    b13 = Checkbutton(alcomarket, bg = MAIN_COLOR, text = 'сидр', var = bvar13, command = lambda:child_beer_toggle())
    b14 = Checkbutton(alcomarket, bg = MAIN_COLOR, text = 'пивной напиток', var = bvar14, command = lambda:child_beer_toggle())
    
    b11.place(x=20, y=550)
    b12.place(x=20, y=570)
    b13.place(x=20, y=590)
    b14.place(x=20, y=610)
    
    b1 = Checkbutton(alcomarket, bg = MAIN_COLOR, text = 'пиво', var = bvar1, command = lambda:main_beer_toggle())
    b1.place(x=10, y=530)
    
    ###### ВЫБОРКА АЛКОГОЛЯ КОНЕЦ ######
    
    ###### ФИЛЬТРАЦИЯ ######
    
    
    price_label = Label(alcomarket, text='Цена', 
                    anchor = 'w', 
                    bg = MAIN_COLOR, 
                    font='consolas 11')
    price_label.place(x = 1140, y = 50)
    
    price1_label = Label(alcomarket, text='от          Р', 
                    anchor = 'w', 
                    bg = MAIN_COLOR, 
                    font='consolas 10')
    price1_label.place(x = 1140, y = 80)
    
    price2_label = Label(alcomarket, text='до          Р', 
                    anchor = 'w', 
                    bg = MAIN_COLOR, 
                    font='consolas 10')
    price2_label.place(x = 1245, y = 80)
    
    price1_entry = Entry(alcomarket, width = 9) 
    price1_entry.place(x = 1165, y = 80)
    
    price2_entry = Entry(alcomarket, width = 9) 
    price2_entry.place(x = 1270, y = 80)
    
    
    request = 'SELECT MAX(price) FROM alcohol;'
    max_price = exec_user_request(request, login, password)
    price2_entry.insert(0, str(max_price[0][0]))
    
    request = 'SELECT MIN(price) FROM alcohol;'
    min_price = exec_user_request(request, login, password)
    price1_entry.insert(0, str(min_price[0][0]))
    
    
    strength_label = Label(alcomarket, text='Крепость', 
                    anchor = 'w', 
                    bg = MAIN_COLOR, 
                    font='consolas 11')
    strength_label.place(x = 1140, y = 120)
    
    strength1_label = Label(alcomarket, text='от          %', 
                    anchor = 'w', 
                    bg = MAIN_COLOR, 
                    font='consolas 10')
    strength1_label.place(x = 1140, y = 150)
    
    strength2_label = Label(alcomarket, text='до          %', 
                    anchor = 'w', 
                    bg = MAIN_COLOR, 
                    font='consolas 10')
    strength2_label.place(x = 1245, y = 150)
    
    
    strength1_entry = Entry(alcomarket, width = 9) 
    strength1_entry.place(x = 1165, y = 150)
    
    strength2_entry = Entry(alcomarket, width = 9) 
    strength2_entry.place(x = 1270, y = 150)
    
    
    request = 'SELECT MAX(strength) FROM alcohol;'
    max_strength = exec_user_request(request, login, password)
    strength2_entry.insert(0, str(max_strength[0][0]))
    
    request = 'SELECT MIN(strength) FROM alcohol;'
    min_strength = exec_user_request(request, login, password)
    strength1_entry.insert(0, str(min_strength[0][0]))
    
    
    volume_label = Label(alcomarket, text='Объем', 
                    anchor = 'w', 
                    bg = MAIN_COLOR, 
                    font='consolas 11')
    volume_label.place(x = 1140, y = 190)
    
    volume1_label = Label(alcomarket, text='от          л', 
                    anchor = 'w', 
                    bg = MAIN_COLOR, 
                    font='consolas 10')
    volume1_label.place(x = 1140, y = 220)
    
    volume2_label = Label(alcomarket, text='до          л', 
                    anchor = 'w', 
                    bg = MAIN_COLOR, 
                    font='consolas 10')
    volume2_label.place(x = 1245, y = 220)
    
    
    
    volume1_entry = Entry(alcomarket, width = 9) 
    volume1_entry.place(x = 1165, y = 220)
    
    volume2_entry = Entry(alcomarket, width = 9) 
    volume2_entry.place(x = 1270, y = 220)
    
    
    request = 'SELECT MAX(volume) FROM alcohol;'
    max_volume = exec_user_request(request, login, password)
    volume2_entry.insert(0, str(max_volume[0][0]))
    
    request = 'SELECT MIN(volume) FROM alcohol;'
    min_volume = exec_user_request(request, login, password)
    volume1_entry.insert(0, str(min_volume[0][0]))
    
    
    ###### ФИЛЬТРАЦИЯ КОНЕЦ ######
    
    ###### СОРТИРОВКА ######
    
    def sort_toggle():
        
        if svar14.get():
            s11.deselect()
            s12.deselect()
            s13.deselect()
        
        if svar13.get():
            s11.deselect()
            s12.deselect()
            s14.deselect() 
        
        if svar12.get():
            s11.deselect()
            s13.deselect()
            s14.deselect()   
            
        if svar11.get():
            s12.deselect()
            s13.deselect()
            s14.deselect()
    
    
    svar11 = BooleanVar()
    svar11.set(False)
    svar12 = BooleanVar()
    svar12.set(False)
    svar13 = BooleanVar()
    svar13.set(False)
    svar14 = BooleanVar()
    svar14.set(False)
    
    s11 = Checkbutton(alcomarket, bg = MAIN_COLOR, text = 'цене (сначала дешевые)', var = svar11, command = lambda:sort_toggle())
    s12 = Checkbutton(alcomarket, bg = MAIN_COLOR, text = 'цене (сначала дорогие)', var = svar12, command = lambda:sort_toggle())
    s13 = Checkbutton(alcomarket, bg = MAIN_COLOR, text = 'крепости (сначала некрепкие)', var = svar13, command = lambda:sort_toggle())
    s14 = Checkbutton(alcomarket, bg = MAIN_COLOR, text = 'крепости (сначала крепкие)', var = svar14, command = lambda:sort_toggle())
     
    s11.place(x=1140, y=270)
    s12.place(x=1140, y=290)
    s13.place(x=1140, y=310)
    s14.place(x=1140, y=330)
    
    sort_label = Label(text='Сортировать по:', 
                    anchor = 'w', 
                    bg = MAIN_COLOR, 
                    font='consolas 11')
    sort_label.place(x = 1140, y = 250)
    
    ###### СОРТИРОВКА КОНЕЦ ######
    
    
    ###### ОБНОВЛЕНИЕ ######
    
    def reload():
        
        nonlocal alcohol
        nonlocal region_vok
        
        request = 'SELECT id_region, region_name FROM region'
        region = exec_user_request(request, login, password)
        region_vok.clear()
        for i in range(len(region)):
            region_vok[region[i][0]] = region[i][1]
    
        
        request = 'SELECT * FROM alcohol '
        
        if wvar11.get() or wvar12.get() or wvar13.get() or wvar14.get() or wvar15.get()\
            or cvar11.get() or cvar12.get() or cvar13.get() or cvar14.get() or cvar15.get()\
                or bvar11.get() or bvar12.get() or bvar13.get() or bvar14.get()\
                    or hvar11.get() or hvar12.get() or hvar13.get() or hvar14.get() or hvar15.get()\
                        or hvar16.get() or hvar17.get() or hvar18.get() or hvar19.get():
            request = request + 'WHERE ('
            
            flag = 1
            
            if wvar11.get():
                if flag:
                    request = request + 'subcategory = 11 '
                    flag = 0
                else:
                    request = request + 'or subcategory = 11 '
            
            if wvar12.get():
                if flag:
                    request = request + 'subcategory = 12 '
                    flag = 1
                else:
                    request = request + 'or subcategory = 12 '       
                    
            if wvar13.get():
                if flag:
                    request = request + 'subcategory = 13 '
                    flag = 1
                else:
                    request = request + 'or subcategory = 13 '
            
            if wvar14.get():
                if flag:
                    request = request + 'subcategory = 14 '
                    flag = 0
                else:
                    request = request + 'or subcategory = 14 '
                    
            if wvar15.get():
                if flag:
                    request = request + 'subcategory = 15 '
                    flag = 0
                else:
                    request = request + 'or subcategory = 15 '
            
            if cvar11.get():
                if flag:
                    request = request + 'subcategory = 21 '
                    flag = 0
                else:
                    request = request + 'or subcategory = 21 '
                
            if cvar12.get():
                if flag:
                    request = request + 'subcategory = 22 '
                    flag = 0
                else:
                    request = request + 'or subcategory = 22 '
            
            if cvar13.get():
                if flag:
                    request = request + 'subcategory = 23 '
                    flag = 0
                else:
                    request = request + 'or subcategory = 23 '
                    
            if cvar14.get():
                if flag:
                    request = request + 'subcategory = 24 '
                    flag = 0
                else:
                    request = request + 'or subcategory = 24 '
                    
            if cvar15.get():
                if flag:
                    request = request + 'subcategory = 25 '
                    flag = 0
                else:
                    request = request + 'or subcategory = 25 '
                    
            if hvar11.get():
                if flag:
                    request = request + 'subcategory = 31 '
                    flag = 0
                else:
                    request = request + 'or subcategory = 31 '
            
            if hvar12.get():
                if flag:
                    request = request + 'subcategory = 32 '
                    flag = 0
                else:
                    request = request + 'or subcategory = 32 '
                    
            if hvar13.get():
                if flag:
                    request = request + 'subcategory = 33 '
                    flag = 0
                else:
                    request = request + 'or subcategory = 33 '
                    
            if hvar14.get():
                if flag:
                    request = request + 'subcategory = 34 '
                    flag = 0
                else:
                    request = request + 'or subcategory = 34 '
                    
            if hvar15.get():
                if flag:
                    request = request + 'subcategory = 35 '
                    flag = 0
                else:
                    request = request + 'or subcategory = 35 '
                    
            if hvar16.get():
                if flag:
                    request = request + 'subcategory = 36 '
                    flag = 0
                else:
                    request = request + 'or subcategory = 36 '
                    
            if hvar17.get():
                if flag:
                    request = request + 'subcategory = 37 '
                    flag = 0
                else:
                    request = request + 'or subcategory = 37 '
            
            if hvar18.get():
                if flag:
                    request = request + 'subcategory = 38 '
                    flag = 0
                else:
                    request = request + 'or subcategory = 38 '
                    
            if hvar19.get():
                if flag:
                    request = request + 'subcategory = 39 '
                    flag = 0
                else:
                    request = request + 'or subcategory = 39 '
                    
            if bvar11.get():
                if flag:
                    request = request + 'subcategory = 41 '
                    flag = 0
                else:
                    request = request + 'or subcategory = 41 '
            
            if bvar12.get():
                if flag:
                    request = request + 'subcategory = 42 '
                    flag = 0
                else:
                    request = request + 'or subcategory = 42 '
            
            if bvar13.get():
                if flag:
                    request = request + 'subcategory = 43 '
                    flag = 0
                else:
                    request = request + 'or subcategory = 43 '
            
            if bvar14.get():
                if flag:
                    request = request + 'subcategory = 44 '
                    flag = 0
                else:
                    request = request + 'or subcategory = 44 ' 
            
            if bvar14.get():
                if flag:
                    request = request + 'subcategory = 44 '
                    flag = 0
                else:
                    request = request + 'or subcategory = 44 '    
            
            flag = 1
            
            try:
                min_price = str(float(price1_entry.get()))
                max_price = str(float(price2_entry.get()))
            except:
                flag = 0
                messagebox.showerror('Ошибка', 'Неверно указаны границы цены!')
                
            try:
                min_strength = str(int(strength1_entry.get()))
                max_strength = str(int(strength2_entry.get()))
            except:
                flag = 0
                messagebox.showerror('Ошибка', 'Неверно указаны границы крепости!')
                
            try:
                min_volume = str(float(volume1_entry.get()))
                max_volume = str(float(volume2_entry.get()))
            except:
                flag = 0
                messagebox.showerror('Ошибка', 'Неверно указаны границы объема!')
            
            if flag:
                request = request + ') AND (price BETWEEN ' + min_price + ' AND ' + max_price\
                   + ') AND (strength BETWEEN ' + min_strength + ' AND ' + max_strength\
                       + ') AND (volume BETWEEN ' + min_volume + ' AND ' + max_volume + ') '
                       
    
            search = str(search_entry.get())
            if search:
                request = request + "AND alcohol_name LIKE '%" + search + "%' "
                    
            
            if svar11.get():
                request = request + 'ORDER BY price ASC ' 
            
            elif svar12.get():
                request = request + 'ORDER BY price DESC ' 
            
            elif svar13.get():
                request = request + 'ORDER BY strength ASC '
            
            elif svar14.get():
                request = request + 'ORDER BY strength DESC '    
        
            request = request + ';'
            alcohol = exec_user_request(request, login, password)
            
            alco_list.delete(0, alco_list.size())
            
            for i in range(len(alcohol)):
                alco_list.insert(END, transform_record(alcohol[i], region_vok))
            
            if not alco_list.size():
                alco_list.insert(END, '----- По вашему запросу ничего не найдено -----')
                
    if usertype == 3:
        
        manager_btn = Button(alcomarket, text='Режим менеджера',
                        width=20,
                        height=1,
                        font='consolas 10',
                        bg = MAIN_COLOR,
                        command=lambda:manager_mode(login, password))
        manager_btn.place(anchor = 'w', x = 1170, y = 590)
        
    def update_cart(login, password):
        
        if not len(alco_list.curselection()):
            return
        
        alcohol_unit = alcohol[alco_list.curselection()[0]]
        alco_id = alcohol_unit[0]
        
        request = "SELECT id_item, id_alcohol FROM cart" + login + ";"
        result = exec_user_request(request, login, password)
        
        flag = 1
        id_item = 0
        
        for i in range(len(result)):
            if alco_id == result[i][1]:
                flag = 0
                id_item = result[i][0]
                
        if flag:
            request = "INSERT INTO cart" + login + " (id_alcohol, qty) VALUES(" + str(alco_id) + ", 1);"
        else:
            request = "CALL UpdateCart('" + '"cart' + login + '"' + "', 1, " + str(id_item) + ');'
        
        exec_user_active_request(request, login, password)
            
        
                
    reload_btn = Button(alcomarket, text='Добавить в корзину',
                        width=20,
                        height=1,
                        font='consolas 10',
                        bg = MAIN_COLOR,
                        command=lambda:update_cart(login, password))
    reload_btn.place(anchor = 'w', x = 1170, y = 620)
    
    reload_btn = Button(alcomarket, text='Открыть',
                        width=20,
                        height=1,
                        font='consolas 10',
                        bg = MAIN_COLOR,
                        command=lambda:card(alco_list, alcohol, login, password, usertype))
    reload_btn.place(anchor = 'w', x = 1170, y = 650)
    
    reload_btn = Button(alcomarket, text='Обновить',
                        width=20,
                        height=1,
                        font='consolas 10',
                        bg = MAIN_COLOR,
                        command=lambda:reload())
    reload_btn.place(anchor = 'w', x = 1170, y = 680)
    
    cart_btn = Button(alcomarket, text='Корзина',
                        width=20,
                        height=1,
                        font='consolas 10',
                        bg = MAIN_COLOR,
                        command=lambda:cart(login, password))
    cart_btn.place(anchor = 'w', x = 1170, y = 30)
    
    