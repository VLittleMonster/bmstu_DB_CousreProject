import psycopg2
from connection import connect, disconnect
from requester import exec_request, exec_active_request, exec_user_request, exec_user_active_request
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from alco_vok import alco_vok
from color import MAIN_COLOR, FONT_COLOR, LIST_COLOR

def manager_mode(login, password):
    manager = Toplevel()
    manager.grab_set()
    
    width = manager.winfo_screenwidth()
    height = manager.winfo_screenheight()
    x = (width - 300) / 2
    y = (height - 200) / 2
    
    icon = PhotoImage(file = 'icon.png')
    manager.iconphoto(True, icon)
    manager.geometry('250x215+%d+%d' % (x, y))
    manager.title('Режим менеджера')
    manager.resizable(True, True)
    manager.configure(background = MAIN_COLOR)
    
    def add_brand():
        brand = Toplevel()
        brand.grab_set()
        
        width = brand.winfo_screenwidth()
        height = brand.winfo_screenheight()
        x = (width - 300) / 2
        y = (height - 200) / 2
        
        icon = PhotoImage(file = 'icon.png')
        brand.iconphoto(True, icon)
        brand.geometry('300x200+%d+%d' % (x, y))
        brand.title('Добавление бренда')
        brand.resizable(True, True)
        brand.configure(background = MAIN_COLOR)
        
        def new_brand():
            request = 'SELECT brand_name FROM brand;'
            brands = exec_user_request(request, login, password)
            
            name = new_brand_entry.get()
            if not name:
                messagebox.showerror('Ошибка!', 'Поля ввода не должны быть пустыми!')
                return
            
            flag = 1
            
            for i in range(len(brands)):
                if name == brands[i][0]:
                    flag = 0
                    
            if flag:
                country = country_entry.get()
                
                if not country:
                    messagebox.showerror('Ошибка!', 'Поля ввода не должны быть пустыми!')
                    return
                
                try:
                    year = str(int(year_entry.get()))
                    
                    if int(year) <= 0:
                        messagebox.showerror('Ошибка!', 'Неверно указан год!')
                        return
                        
                    
                    request = "INSERT INTO brand (brand_name, country, product, foundation_year) VALUES ('" +\
                        name + "', '" + country + "', 11, " + year + ');'
                    exec_user_active_request(request, login, password)
                    messagebox.showinfo('Уведомление!', 'Бренд успешно добавлен!')
                    brand.destroy()
                    
                except:
                    messagebox.showerror('Ошибка!', 'Неверно указан год!')
            else:
                messagebox.showerror('Ошибка!', 'Данный бренд уже существует!')
            
        
        new_brand_label = Label(brand, text = 'Название:',
                    anchor = 'c', 
                    bg = MAIN_COLOR,
                    font='consolas 12')
        new_brand_label.place(x = 10, y = 10)
        
        new_brand_entry = Entry(brand, width = 20) 
        new_brand_entry.place(x = 150, y = 13)
        
        country_label = Label(brand, text = 'Страна:',
                    anchor = 'c', 
                    bg = MAIN_COLOR,
                    font='consolas 12')
        country_label.place(x = 10, y = 40)
        
        country_entry = Entry(brand, width = 20) 
        country_entry.place(x = 150, y = 43)
        
        year_label = Label(brand, text = 'Год основания:',
                    anchor = 'c', 
                    bg = MAIN_COLOR,
                    font='consolas 12')
        year_label.place(x = 10, y = 70)
        
        year_entry = Entry(brand, width = 20) 
        year_entry.place(x = 150, y = 73)
        
        add_btn = Button(brand, text='Подтвердить',
                            width=20,
                            height=1,
                            font='consolas 10',
                            bg = MAIN_COLOR,
                            command=lambda:new_brand())
        add_btn.place(anchor = 'w', x = 75, y = 150)
    
    def add_region():
        region = Toplevel()
        region.grab_set()
        
        width = region.winfo_screenwidth()
        height = region.winfo_screenheight()
        x = (width - 300) / 2
        y = (height - 200) / 2
        
        icon = PhotoImage(file = 'icon.png')
        region.iconphoto(True, icon)
        region.geometry('300x200+%d+%d' % (x, y))
        region.title('Добавление региона')
        region.resizable(True, True)
        region.configure(background = MAIN_COLOR)
        
        def new_region():
            request = 'SELECT region_name FROM region;'
            regions = exec_user_request(request, login, password)
            
            name = new_region_entry.get()
            if not name:
                messagebox.showerror('Ошибка!', 'Поля ввода не должны быть пустыми!')
                return
            
            flag = 1
            
            for i in range(len(regions)):
                if name == regions[i][0]:
                    flag = 0
                    
            if flag:
                country = country_entry.get()
                
                if not country:
                    messagebox.showerror('Ошибка!', 'Поля ввода не должны быть пустыми!')
                    return 
                    
                request = "INSERT INTO region (region_name, country) VALUES ('" +\
                    name + "', '" + country + "');"
                exec_user_active_request(request, login, password)
                messagebox.showinfo('Уведомление!', 'Регион успешно добавлен!')
                region.destroy()

            else:
                messagebox.showerror('Ошибка!', 'Данный регион уже существует!')
            
        
        new_region_label = Label(region, text = 'Название:',
                    anchor = 'c', 
                    bg = MAIN_COLOR,
                    font='consolas 12')
        new_region_label.place(x = 10, y = 10)
        
        new_region_entry = Entry(region, width = 20) 
        new_region_entry.place(x = 150, y = 13)
        
        country_label = Label(region, text = 'Страна:',
                    anchor = 'c', 
                    bg = MAIN_COLOR,
                    font='consolas 12')
        country_label.place(x = 10, y = 40)
        
        country_entry = Entry(region, width = 20) 
        country_entry.place(x = 150, y = 43)
        
        add_btn = Button(region, text='Подтвердить',
                            width=20,
                            height=1,
                            font='consolas 10',
                            bg = MAIN_COLOR,
                            command=lambda:new_region())
        add_btn.place(anchor = 'w', x = 75, y = 140)
    
    def add_factory():
        factory = Toplevel()
        factory.grab_set()
        
        width = factory.winfo_screenwidth()
        height = factory.winfo_screenheight()
        x = (width - 300) / 2
        y = (height - 200) / 2
        
        icon = PhotoImage(file = 'icon.png')
        factory.iconphoto(True, icon)
        factory.geometry('300x200+%d+%d' % (x, y))
        factory.title('Добавление завода')
        factory.resizable(True, True)
        factory.configure(background = MAIN_COLOR)
        
        def new_factory():
            request = 'SELECT factory_name FROM factory;'
            factorys = exec_user_request(request, login, password)
            
            name = new_factory_entry.get()
            if not name:
                messagebox.showerror('Ошибка!', 'Поля ввода не должны быть пустыми!')
                return
            
            flag = 1
            
            for i in range(len(factorys)):
                if name == factorys[i][0]:
                    flag = 0
                    
            if flag:
                country = country_entry.get()
                
                if not country:
                    messagebox.showerror('Ошибка!', 'Поля ввода не должны быть пустыми!')
                    return
                
                city  = city_entry.get()
                
                if not city:
                    messagebox.showerror('Ошибка!', 'Поля ввода не должны быть пустыми!')
                    return
                
                try:
                    year = str(int(year_entry.get()))
                    
                    if int(year) <= 0:
                        messagebox.showerror('Ошибка!', 'Неверно указан год!')
                        return
                        
                    
                    request = "INSERT INTO factory (factory_name, country, city, foundation_year) VALUES ('" +\
                        name + "', '" + country + "', '" + city + "', " + year + ');'
                    exec_user_active_request(request, login, password)
                    messagebox.showinfo('Уведомление!', 'Завод успешно добавлен!')
                    factory.destroy()
                    
                except:
                    messagebox.showerror('Ошибка!', 'Неверно указан год!')
            else:
                messagebox.showerror('Ошибка!', 'Данный завод уже существует!')
            
        
        new_factory_label = Label(factory, text = 'Название:',
                    anchor = 'c', 
                    bg = MAIN_COLOR,
                    font='consolas 12')
        new_factory_label.place(x = 10, y = 10)
        
        new_factory_entry = Entry(factory, width = 20) 
        new_factory_entry.place(x = 150, y = 13)
        
        country_label = Label(factory, text = 'Страна:',
                    anchor = 'c', 
                    bg = MAIN_COLOR,
                    font='consolas 12')
        country_label.place(x = 10, y = 40)
        
        country_entry = Entry(factory, width = 20) 
        country_entry.place(x = 150, y = 43)
        
        city_label = Label(factory, text = 'Город:',
                    anchor = 'c', 
                    bg = MAIN_COLOR,
                    font='consolas 12')
        city_label.place(x = 10, y = 70)
        
        city_entry = Entry(factory, width = 20) 
        city_entry.place(x = 150, y = 73)
        
        year_label = Label(factory, text = 'Год основания:',
                    anchor = 'c', 
                    bg = MAIN_COLOR,
                    font='consolas 12')
        year_label.place(x = 10, y = 100)
        
        year_entry = Entry(factory, width = 20) 
        year_entry.place(x = 150, y = 103)
        
        add_btn = Button(factory, text='Подтвердить',
                            width=20,
                            height=1,
                            font='consolas 10',
                            bg = MAIN_COLOR,
                            command=lambda:new_factory())
        add_btn.place(anchor = 'w', x = 75, y = 160)
    
    
    def add_alcohol():
        alcohol = Toplevel()
        alcohol.grab_set()
        
        width = alcohol.winfo_screenwidth()
        height = alcohol.winfo_screenheight()
        x = (width - 900) / 2
        y = (height - 400) / 2
        
        icon = PhotoImage(file = 'icon.png')
        alcohol.iconphoto(True, icon)
        alcohol.geometry('800x300+%d+%d' % (x, y))
        alcohol.title('Добавление алкоголя')
        alcohol.resizable(True, True)
        alcohol.configure(background = MAIN_COLOR)
        
        def new_alcohol():
             
            name = new_alcohol_entry.get()
            
            if not name:
                messagebox.showerror('Ошибка!', 'Поля ввода не должны быть пустыми!')
                return
        
            alcotype = type_box.get()
            
            if not alcotype:
                messagebox.showerror('Ошибка!', 'Поля ввода не должны быть пустыми!')
                return
            
            invert_alco_vok = {value: key for key, value in alco_vok.items()}
            
            db_subcategory = invert_alco_vok[alcotype]
            db_category = db_subcategory // 10
            
            brand = brand_box.get() 
            
            if not brand:
                messagebox.showerror('Ошибка!', 'Поля ввода не должны быть пустыми!')
                return
            
            request = "SELECT id_brand FROM brand WHERE brand_name = '" + brand + "';"
            result = exec_user_request(request, login, password)
            id_brand = str(result[0][0])
            
            factory = factory_box.get()
            
            if not factory:
                messagebox.showerror('Ошибка!', 'Поля ввода не должны быть пустыми!')
                return
            
            request = "SELECT id_factory FROM factory WHERE factory_name = '" + factory + "';"
            result = exec_user_request(request, login, password)
            id_factory = str(result[0][0])
            
            strength = 0
            
            try:
                strength = int(strength_entry.get())
            except:
                messagebox.showerror('Ошибка!', 'Поле со значением крепости заполнено неверно!')
                return
            
            price = 0
            
            try:
                price = float(price_entry.get())
            except:
                messagebox.showerror('Ошибка!', 'Поле со значением цены заполнено неверно!')
                return
            
            volume = volume_box.get()
            
            if not volume:
                messagebox.showerror('Ошибка!', 'Поля ввода не должны быть пустыми!')
                return
            
            qty = 0
            
            try:
                qty = str(int(qty_entry.get()))
            except:
                messagebox.showerror('Ошибка!', 'Поле со значением количества заполнено неверно!')
                return
            
            pack = 'NULL'
            filtration = 'NULL'
            
            if db_category == 4:
                pack = pack_box.get()
            
                if not pack:
                    messagebox.showerror('Ошибка!', 'Поля ввода не должны быть пустыми!')
                    return
                
                filtration = filtration_box.get()
                
                if not filtration:
                    messagebox.showerror('Ошибка!', 'Поля ввода не должны быть пустыми!')
                    return
                
                if pack == 'стекло':
                    pack = '1'
                elif pack == 'банка':
                    pack = '2'
                    
                if filtration == 'фильтрованное':
                    filtration = '1'
                elif filtration == 'нефильтрованное':
                    filtration = '2'
            
            id_region = 'NULL'
            sort = 'NULL'
            harvest = 'NULL'
            sugar = 'NULL'   
            
            if db_category == 1 or db_category == 2:
                
                region = region_box.get()
                
                if not region:
                    messagebox.showerror('Ошибка!', 'Поля ввода не должны быть пустыми!')
                    return
                
                request = "SELECT id_region FROM region WHERE region_name = '" + region + "';"
                result = exec_user_request(request, login, password)
                id_region = str(result[0][0])
                
                sort = sort_entry.get()
                
                if not sort:
                    messagebox.showerror('Ошибка!', 'Поля ввода не должны быть пустыми!')
                    return
                
                try:
                    harvest = int(harvest_entry.get())
                    if harvest < 1980 or harvest > 2021:
                        messagebox.showerror('Ошибка!', 'Поле ввода для года урожая заполнено неверно!')
                        return  
                except:
                    messagebox.showerror('Ошибка!', 'Поля ввода не должны быть пустыми!')
                    return
                
                sugar = sugar_box.get()
                
                if not sugar:
                    messagebox.showerror('Ошибка!', 'Поля ввода не должны быть пустыми!')
                    return
                
                if sugar == 'полусладкое':
                    sugar = '1'
                elif sugar == 'полусухое':
                    sugar = '2'
                elif sugar == 'сухое':
                    sugar = '3'
                elif sugar == 'брют':
                    sugar = '4'
                
            request = "INSERT INTO alcohol (alcohol_name, category, subcategory, id_brand, id_factory, strength, price, volume, qty, pack, filtration, id_region, sort, harvest_year, sugar) VALUES ('" +\
                str(name) + "', " + str(db_category) + ", " + str(db_subcategory) + ", " + str(id_brand)\
                    + ", " + str(id_factory) + ", " + str(strength) + ", " + str(price) + ", " + str(volume)\
                        + ", " + str(qty) + ", " + str(pack) + ", " + str(filtration) + ", " + str(id_region) + ", " + str(sort) + ", " + str(harvest) + ", '" + str(sugar) + "');"
            exec_user_active_request(request, login, password)
            messagebox.showinfo('Уведомление!', 'Алкоголь успешно добавлен!')
            alcohol.destroy()
            
        
        new_alcohol_label = Label(alcohol, text = 'Название:',
                    anchor = 'c', 
                    bg = MAIN_COLOR,
                    font='consolas 12')
        new_alcohol_label.place(x = 10, y = 10)
        
        new_alcohol_entry = Entry(alcohol, width = 38) 
        new_alcohol_entry.place(x = 150, y = 13)
        
        alco_types = []
        
        alco_types.append(alco_vok[11])
        alco_types.append(alco_vok[12])
        alco_types.append(alco_vok[13])
        alco_types.append(alco_vok[14])
        alco_types.append(alco_vok[15])
        alco_types.append(alco_vok[21])
        alco_types.append(alco_vok[22])
        alco_types.append(alco_vok[23])
        alco_types.append(alco_vok[24])
        alco_types.append(alco_vok[25])
        alco_types.append(alco_vok[31])
        alco_types.append(alco_vok[32])
        alco_types.append(alco_vok[33])
        alco_types.append(alco_vok[34])
        alco_types.append(alco_vok[35])
        alco_types.append(alco_vok[36])
        alco_types.append(alco_vok[37])
        alco_types.append(alco_vok[38])
        alco_types.append(alco_vok[39])
        alco_types.append(alco_vok[41])
        alco_types.append(alco_vok[42])
        alco_types.append(alco_vok[43])
        alco_types.append(alco_vok[44])
        alco_types.sort()
        
        type_label = Label(alcohol, text = 'Вид алкоголя:',
                    anchor = 'c', 
                    bg = MAIN_COLOR,
                    font='consolas 12')
        type_label.place(x = 10, y = 40)
        
        type_box = ttk.Combobox(alcohol, values = alco_types,
                        background = MAIN_COLOR,
                        font = 'consolas 10',
                        height = 10,
                        width = 16,
                        state="readonly")
        type_box.place(x = 150, y = 43)
        
        request = 'SELECT brand_name FROM brand;'
        brand_res = exec_user_request(request, login, password)
        brands = []
        
        for i in range(len(brand_res)):
            brands.append(brand_res[i][0])
        brands.sort()
        
        
        brand_label = Label(alcohol, text = 'Бренд:',
                    anchor = 'c', 
                    bg = MAIN_COLOR,
                    font='consolas 12')
        brand_label.place(x = 10, y = 70)
        
        
        brand_box = ttk.Combobox(alcohol, values = brands,
                        background = MAIN_COLOR,
                        font = 'consolas 10',
                        height = 10,
                        width = 30,
                        state="readonly")
        brand_box.place(x = 150, y = 73)
        
        request = 'SELECT factory_name FROM factory;'
        factory_res = exec_user_request(request, login, password)
        factorys = []
        
        for i in range(len(factory_res)):
            factorys.append(factory_res[i][0])
        factorys.sort()
        
        factory_label = Label(alcohol, text = 'Завод:',
                    anchor = 'c', 
                    bg = MAIN_COLOR,
                    font='consolas 12')
        factory_label.place(x = 10, y = 100)
    
        factory_box = ttk.Combobox(alcohol, values = factorys,
                        background = MAIN_COLOR,
                        font = 'consolas 10',
                        height = 10,
                        width = 30,
                        state="readonly")
        factory_box.place(x = 150, y = 103)
        
        strength_label = Label(alcohol, text = 'Крепость:              %',
                    anchor = 'c', 
                    bg = MAIN_COLOR,
                    font='consolas 12')
        strength_label.place(x = 10, y = 130)
        
        strength_entry = Entry(alcohol, width = 10) 
        strength_entry.place(x = 150, y = 133)
        
        price_label = Label(alcohol, text = 'Цена:                  ₽',
                    anchor = 'c', 
                    bg = MAIN_COLOR,
                    font='consolas 12')
        price_label.place(x = 10, y = 160)
        
        price_entry = Entry(alcohol, width = 10) 
        price_entry.place(x = 150, y = 163)
        
        volumes = ['0.25', '0.33', '0.45', '0.5', '1', '1.5', '2', '5']
        
        volume_label = Label(alcohol, text = 'Объем:                 л',
                    anchor = 'c', 
                    bg = MAIN_COLOR,
                    font='consolas 12')
        volume_label.place(x = 10, y = 190)
        
        volume_box = ttk.Combobox(alcohol, values = volumes,
                        background = MAIN_COLOR,
                        font = 'consolas 10',
                        height = 10,
                        width = 6,
                        state="readonly")
        volume_box.place(x = 150, y = 193)
        
        qty_label = Label(alcohol, text = 'Количество:',
                    anchor = 'c', 
                    bg = MAIN_COLOR,
                    font='consolas 12')
        qty_label.place(x = 10, y = 220)
        
        qty_entry = Entry(alcohol, width = 10) 
        qty_entry.place(x = 150, y = 223)
        
        info1_label = Label(alcohol, text = 'ДОПОЛНИТЕЛЬНАЯ ИНФОРМАЦИЯ (Игристое, Вино)',
                    anchor = 'c', 
                    bg = MAIN_COLOR,
                    font='consolas 12')
        info1_label.place(x = 400, y = 10)
        
        request = 'SELECT region_name FROM region;'
        region_res = exec_user_request(request, login, password)
        regions = []
        
        for i in range(len(region_res)):
            regions.append(region_res[i][0])
        regions.sort()
        
        region_label = Label(alcohol, text = 'Регион:',
                    anchor = 'c', 
                    bg = MAIN_COLOR,
                    font='consolas 12')
        region_label.place(x = 400, y = 40)
    
        region_box = ttk.Combobox(alcohol, values = regions,
                        background = MAIN_COLOR,
                        font = 'consolas 10',
                        height = 10,
                        width = 20,
                        state="readonly")
        region_box.place(x = 500, y = 43)
        
        sort_label = Label(alcohol, text = 'Сорт:',
                    anchor = 'c', 
                    bg = MAIN_COLOR,
                    font='consolas 12')
        sort_label.place(x = 400, y = 70)
        
        sort_entry = Entry(alcohol, width = 26) 
        sort_entry.place(x = 500, y = 73)
        
        harvest_label = Label(alcohol, text = 'Год урожая',
                    anchor = 'c', 
                    bg = MAIN_COLOR,
                    font='consolas 12')
        harvest_label.place(x = 400, y = 100)
        
        harvest_entry = Entry(alcohol, width = 26) 
        harvest_entry.place(x = 500, y = 103) 
        
        sugars = ['полусладкое', 'полусухое', 'сухое', 'брют']
        
        sugar_label = Label(alcohol, text = 'Сахар:',
                    anchor = 'c', 
                    bg = MAIN_COLOR,
                    font='consolas 12')
        sugar_label.place(x = 400, y = 130)
        
        sugar_box = ttk.Combobox(alcohol, values = sugars,
                        background = MAIN_COLOR,
                        font = 'consolas 10',
                        height = 10,
                        width = 12,
                        state="readonly")
        sugar_box.place(x = 500, y = 133)
        
        info2_label = Label(alcohol, text = 'ДОПОЛНИТЕЛЬНАЯ ИНФОРМАЦИЯ (Пиво, Сидр, ...)',
                    anchor = 'c', 
                    bg = MAIN_COLOR,
                    font='consolas 12')
        info2_label.place(x = 400, y = 160)
        
        packs = ['стекло', 'банка']
        
        pack_label = Label(alcohol, text = 'Тара:',
                    anchor = 'c', 
                    bg = MAIN_COLOR,
                    font='consolas 12')
        pack_label.place(x = 400, y = 190)
        
        pack_box = ttk.Combobox(alcohol, values = packs,
                        background = MAIN_COLOR,
                        font = 'consolas 10',
                        height = 10,
                        width = 20,
                        state="readonly")
        pack_box.place(x = 500, y = 193)
        
        filtrations = ['фильтрованное', 'нефильтрованное']
        
        filtration_label = Label(alcohol, text = 'Фильтрация',
                    anchor = 'c', 
                    bg = MAIN_COLOR,
                    font='consolas 12')
        filtration_label.place(x = 400, y = 220)
        
        filtration_box = ttk.Combobox(alcohol, values = filtrations,
                        background = MAIN_COLOR,
                        font = 'consolas 10',
                        height = 10,
                        width = 20,
                        state="readonly")
        filtration_box.place(x = 500, y = 223)
        
        add_btn = Button(alcohol, text='Добавить алкоголь',
                            width=30,
                            height=1,
                            font='consolas 10',
                            bg = MAIN_COLOR,
                            command=lambda:new_alcohol())
        add_btn.place(anchor = 'w', x = 300, y = 270)
    
    add_brand_btn = Button(manager, text='Добавить бренд',
                        width=20,
                        height=1,
                        font='consolas 12',
                        bg = MAIN_COLOR,
                        command=lambda:add_brand())
    add_brand_btn.place(anchor = 'w', x = 30, y = 30)
    
    add_factory_btn = Button(manager, text='Добавить завод',
                        width=20,
                        height=1,
                        font='consolas 12',
                        bg = MAIN_COLOR,
                        command=lambda:add_factory())
    add_factory_btn.place(anchor = 'w', x = 30, y = 80)
    
    add_region_btn = Button(manager, text='Добавить регион',
                        width=20,
                        height=1,
                        font='consolas 12',
                        bg = MAIN_COLOR,
                        command=lambda:add_region())
    add_region_btn.place(anchor = 'w', x = 30, y = 130)
    
    add_alcohol_btn = Button(manager, text='Добавить алкоголь',
                        width=20,
                        height=1,
                        font='consolas 12',
                        bg = MAIN_COLOR,
                        command=lambda:add_alcohol())
    add_alcohol_btn.place(anchor = 'w', x = 30, y = 180)