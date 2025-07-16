CREATE TABLE brand(
	id_brand INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    brand_name TEXT NOT NULL UNIQUE,
    country TEXT NOT NULL,
	product INT NOT NULL,
    foundation_year INT NOT NULL
);

CREATE TABLE factory(
	id_factory INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
	factory_name TEXT NOT NULL UNIQUE,
	country TEXT NOT NULL,
	city TEXT NOT NULL,
	foundation_year INT NOT NULL
);

CREATE TABLE region(
	id_region INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
	region_name TEXT NOT NULL UNIQUE,
	country TEXT NOT NULL
);

CREATE TABLE alcohol(
    id_alcohol INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
	alcohol_name TEXT NOT NULL,
	category INT NOT NULL,
	subcategory INT NOT NULL,
	id_brand INT NOT NULL,
    id_factory INT NOT NULL,
	strength INT NOT NULL,
	price FLOAT NOT NULL,
	volume FLOAT NOT NULL,
	qty INT NOT NULL,
	pack INT,
	filtration INT,
	id_region INT,
	sort TEXT,
	harvest_year INT,
	sugar INT
);

CREATE TABLE users(
	id_user INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
	user_nick TEXT NOT NULL,
	user_login TEXT NOT NULL UNIQUE,
	user_password TEXT NOT NULL,
	user_grant INT NOT NULL
);