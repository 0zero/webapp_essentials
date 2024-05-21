DO
$$
BEGIN
   IF NOT EXISTS (SELECT FROM pg_database WHERE datname = 'products') THEN
       PERFORM dblink_exec('dbname=postgres', 'CREATE DATABASE products');
   END IF;
END
$$;

DO
$$
BEGIN
   IF NOT EXISTS (SELECT FROM pg_database WHERE datname = 'products_test') THEN
       PERFORM dblink_exec('dbname=postgres', 'CREATE DATABASE products_test');
   END IF;
END
$$;