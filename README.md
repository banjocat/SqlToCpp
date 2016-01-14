# CppSimpleORM

This was created to help bridge that gap of a legacy project that uses SQLite.

What this -WILL- accomplish
* Convert a SQLite3 schema into a C++ structure
* Takes a SQLite3 database and creates C++ structures
* Creates callbacks using the sqlite3 API to use structures
* Automatically joins tables.


To start have a schema.
example.  

```
// schema.sql

