COPY brand(brand_name, country, product, foundation_year)
FROM 'C:\Users\Vlad\Desktop\DB\course\data\db_brand.txt' DELIMITER ',' CSV;

COPY factory(factory_name, country, city, foundation_year)
FROM 'C:\Users\Vlad\Desktop\DB\course\data\db_factory.txt' DELIMITER ',' CSV;

COPY region(region_name, country)
FROM 'C:\Users\Vlad\Desktop\DB\course\data\db_region.txt' DELIMITER ',' CSV;

COPY alcohol(alcohol_name, category, subcategory, id_brand, id_factory, strength, price, volume, qty, pack, filtration, id_region, sort, harvest_year, sugar)
FROM 'C:\Users\Vlad\Desktop\DB\course\data\db_alcohol.txt' DELIMITER ',' CSV;