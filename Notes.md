**Connect to db command line in container**

`>docker exec -it moneyhelper_db_1 psql -U postgres`

**Create dump of database**


`>docker exec moneyhelper_db_1 pg_dump -U postgres -O postgres > postgres_dump.sql`


**Import dump**


>docker exec moneyhelper_db_1 psql -U postgres postgres < postgres_dump.sql