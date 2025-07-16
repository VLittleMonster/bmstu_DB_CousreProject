ALTER TABLE brand
	ADD CHECK (foundation_year > 0);

ALTER TABLE factory
	ADD CHECK (foundation_year > 0);

ALTER TABLE alcohol
	ADD CHECK (category > 0),
    ADD CHECK (subcategory > 0),
    ADD CHECK (strength > 0),
    ADD CHECK (price > 0),
    ADD CHECK (volume > 0),
    ADD CHECK (qty >= 0),
    ADD CHECK (harvest_year > 1900),
	ADD FOREIGN KEY (id_region) REFERENCES region(id_region),
    ADD FOREIGN KEY (id_brand) REFERENCES brand(id_brand),
    ADD FOREIGN KEY (id_factory) REFERENCES factory(id_factory);

ALTER TABLE users
	ADD CHECK (user_grant BETWEEN 1 AND 3);