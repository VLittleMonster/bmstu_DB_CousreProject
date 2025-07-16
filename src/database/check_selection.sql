SELECT alcohol_name, brand_name, alcohol.id_brand, brand.id_brand
FROM alcohol JOIN brand
ON alcohol.id_brand = brand.id_brand;

SELECT *
FROM alcohol JOIN add_grape
ON alcohol.add_data = add_grape.id_add_grape
WHERE category = 1 or category = 2;

SELECT usename, usesuper, usecreatedb FROM pg_catalog.pg_user;