from random import randint

wine_brand_f = open('wine_brand.txt', 'r', encoding='utf-8')
champ_brand_f = open('champ_brand.txt', 'r', encoding='utf-8')
hard_brand_f = open('hard_brand.txt', 'r', encoding='utf-8')
beer_brand_f = open('beer_brand.txt', 'r', encoding='utf-8')
sort_f = open('sort.txt', 'r', encoding='utf-8')
# factory_f = open('factory.txt', 'r')
sort_f = open('sort.txt', 'r', encoding='utf-8')
# alcohol_f = open('alcohol.txt', 'r')

wine_brand = []
champ_brand = []
hard_brand = []
beer_brand = []
sort = []

sugar = ['сухое', 'полусухое', 'полусладкое', 'сладкое']



db_brand_f = open('db_brand.txt', 'w', encoding='utf-8')

for line in wine_brand_f:
    n_line = line.replace('\n', '')
    n_line = n_line + ',' + str(randint(1800,2000))
    wine_brand.append(n_line)
    db_brand_f.write(n_line + '\n')
    
    
for line in champ_brand_f:
    n_line = line.replace('\n', '')
    n_line = n_line + ',' + str(randint(1800,2000))
    champ_brand.append(n_line)
    db_brand_f.write(n_line + '\n')
    
    
for line in hard_brand_f:
    n_line = line.replace('\n', '')
    n_line = n_line + ',' + str(randint(1800,2000))
    hard_brand.append(n_line)
    db_brand_f.write(n_line + '\n')
    
    
for line in beer_brand_f:
    n_line = line.replace('\n', '')
    n_line = n_line + ',' + str(randint(1800,2000))
    beer_brand.append(n_line)
    db_brand_f.write(n_line + '\n')
    
db_brand_f.close()


db_brand_f = open('db_brand.txt', 'r', encoding='utf-8')
db_factory_f = open('db_factory.txt', 'w', encoding='utf-8')

for line in db_brand_f:
    n_line = line.replace('\n', '')
    n_line = line.replace(',', ' Corp. Ltd.,', 1)
    db_factory_f.write(n_line)

for line in sort_f:
    n_line = line.replace('\n', '')
    sort.append(n_line)


wine_brand_f.close()
champ_brand_f.close()
hard_brand_f.close()
beer_brand_f.close()
sort_f.close()

db_factory_f = open('db_factory.txt', 'w')
db_region_f = open('db_region.txt', 'w')
db_grape_f = open('db_grape.txt', 'w')
db_alcohol_f = open('db_alcohol.txt', 'w')

brand = tuple()
factory = tuple()
region = tuple()

import psycopg2

def connect():
    connection = psycopg2.connect(dbname='alcomarket', user='postgres', 
                        password='75863302', host='localhost')
    cursor = connection.cursor()
    
    return connection, cursor

def disconnect(cursor, connection):
    cursor.close()
    connection.close()
    

def show_result(result):
    print()
    for i in range(len(result)):
        print();
        for j in range(len(result[0])):
            print(str(result[i][j]) + ' ', end = '');
    print('');

def exec_request(request, type):
    result = tuple()
    
    connection, cursor = connect()
    cursor.execute(request)
    result = cursor.fetchall()
    
    global brand, factory, region
    
    if type == 1:
        brand = result
    
    if type == 2:
        factory = result
        
    if type == 4:
        region = result
                
    disconnect(cursor, connection)
    

def r_1():
    request = "\
    SELECT * \
    FROM brand"
    exec_request(request,1)

def r_2():
    request = "\
    SELECT * \
    FROM factory"
    exec_request(request,2)
    
def r_4():
    request = "\
    SELECT * \
    FROM region"
    exec_request(request,4)
    
    

r_1()
r_2()
r_4()

db_alcohol_f = open('db_alcohol.txt', 'w', encoding='utf-8')


for i in range(1000):
    
    category = randint(1,4)
    
    if category == 3:
        subcategory = randint(31,39)
    elif category == 4:
        subcategory = randint(41,44)
    else:
        subcategory = category * 10 + randint(1,5)
    
    names = {11: 'Red wine', 12: 'White wine', 13: 'Rose wine', 14: 'Vermouth', 15: 'Portwine', 
             21: 'Champagne', 22: 'Sparkling wine', 23: 'Average', 24: 'Asti', 25: 'Lambrusko', 
             31: 'Rum', 32: 'Whiskey', 33: 'Cognac', 34: 'Liquor', 
             35: 'Vodka', 36: 'Tequila', 37: 'Gin', 38: 'Absinthe', 39: 'Sake', 
             41: 'Liht beer', 42: 'Dark beer', 43: 'Cider', 44: 'Beer drink'}
    
    need_id = 0
    name = ''
    name = name + names[subcategory] + ' de '
    
    key = 1
    
    if category != 3:
        while key:
            id = randint(1, len(brand) - 1)
            if category == brand[id-1][3]:
                name = name + brand[id-1][1]
                need_id = id
                key = 0
                
    else:
        while key:
            id = randint(1, len(brand) - 1)
            if subcategory == brand[id-1][3]:
                name = name + brand[id-1][1]
                need_id = id
                key = 0
    
    strength = 0
    
    if category == 1 or category == 2:
        strength = randint(12, 18)
    elif category == 4:
        strength = randint(4, 8)
    else:
        if subcategory == 8:
            strength = randint(60, 70)
        else:
            strength = randint(40, 45)
    
    price = 0
    
    if category == 1 or category == 2:
        price = randint(200, 2500)
    elif category == 3:
        price = randint(400, 4000)
    else:
        price = randint(100, 300)
    
    volumes_12 = [0.33, 0.75, 1.5]
    volumes_3 = [0.25, 0.5, 0.7, 1]
    volumes_4 = [0.33, 0.45, 0.5, 1.5]
    
    volume = 0
    
    if category == 1 or category == 2:
        volume = volumes_12[randint(0, len(volumes_12) - 1)]
    elif category == 3:
        volume = volumes_3[randint(0, len(volumes_3) - 1)]
    else:
        volume = volumes_4[randint(0, len(volumes_4) - 1)]
    
    price = price * volume
    price = round(price, 2)
    
    qty = randint(1, 100)
    
    # pack INT,
	# filtration INT,
	# id_region INT,
	# sort TEXT,
	# harvest_year INT,
	# sugar INT
    
    add_inf  = ''
    if category == 4:
        add_inf = add_inf + str(randint(1,2)) + ',' + str(randint(1,2)) + ',,,,'
    if category == 1 or category == 2:
        add_inf = add_inf + ',,' + str(randint(1,27)) + ',' + sort[randint(0, len(sort)-1)] + ',' + str(randint(1980, 2021)) + ',' + str(randint(1,4))
    if category == 3:
        add_inf = add_inf + ",,,,,"

        
    db_alcohol_f.write(name + ',' + str(category) + ',' + str(subcategory) + ',' + 
                       str(need_id) + ',' + str(need_id) + ',' +
                       str(strength) + ',' +
                       str(price) + ',' + str(volume) + ',' + str(qty) + ',' + add_inf + '\n')
        
    
db_alcohol_f.close()