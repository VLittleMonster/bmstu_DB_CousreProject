CREATE OR REPLACE FUNCTION Reaction() RETURNS TRIGGER
AS
$$
BEGIN 
    IF TG_NAME = 'deleteuser' THEN
    RAISE EXCEPTION 'DELETE FROM users was detected! Operation is blocked!';
    END IF;
RETURN NEW;
END;
$$
LANGUAGE plpgsql;

CREATE TRIGGER DeleteUser
BEFORE DELETE
ON
users
FOR EACH ROW
EXECUTE PROCEDURE Reaction();