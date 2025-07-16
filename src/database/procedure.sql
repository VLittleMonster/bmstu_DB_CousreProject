CREATE OR REPLACE PROCEDURE UpdateCart (tbl_name text, inc INT, id INT)
AS
$$
    DECLARE cur_qty INT;
BEGIN
    EXECUTE format('SELECT qty FROM %s WHERE id_item = %s', tbl_name, id) INTO cur_qty;
    IF cur_qty > 1 OR inc > 0 THEN
        EXECUTE format('UPDATE %s SET qty = qty + %s WHERE id_item = %s', tbl_name, inc, id);
    END IF;
    IF cur_qty <= inc AND inc < 0 THEN
        EXECUTE format('DELETE FROM %s WHERE id_item = %s', tbl_name, id);
    END IF;
END;
$$
LANGUAGE plpgsql;

DROP PROCEDURE UpdateCart;

CALL UpdateCart('"cartfff"', 1, 1);
SELECT * FROM cartfff;