DO
$do$
BEGIN
 IF NOT EXISTS (SELECT FROM pg_catalog.pg_roles WHERE rolname = 'asterisk') THEN
 CREATE USER asterisk WITH PASSWORD 'asterisk';
 END IF;
END
$do$;

