-- Enable the dblink extension if it's not already enabled
DO
$$
BEGIN
   IF NOT EXISTS (SELECT 1 FROM pg_extension WHERE extname = 'dblink') THEN
       CREATE EXTENSION dblink;
   END IF;
END
$$;

-- Create the inventory database only if it does not already exist
DO
$$
BEGIN
   IF NOT EXISTS (SELECT 1 FROM pg_database WHERE datname = 'inventory') THEN
       PERFORM dblink_exec('dbname=postgres', 'CREATE DATABASE inventory');
   END IF;
END
$$;

-- Create the inventory_test database only if it does not already exist
DO
$$
BEGIN
   IF NOT EXISTS (SELECT 1 FROM pg_database WHERE datname = 'inventory_test') THEN
       PERFORM dblink_exec('dbname=postgres', 'CREATE DATABASE inventory_test');
   END IF;
END
$$;
