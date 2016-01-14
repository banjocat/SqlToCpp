# CppSimpleORM

Goals.
1. Takes a SQLite3 database and creates C++ structures
2. Creates callbacks using the sqlite3 API to use structures
3. Automatically joins tables.


To start have a schema.
example.  

```
// schema.sql

CREATE TABLE bob (
  INT primary_key;
);
