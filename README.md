[![Build Status](https://travis-ci.org/banjocat/SqlToCpp.svg?branch=master)](https://travis-ci.org/banjocat/SqlToCpp) -- master branch

This is in development and has not reached a stable release.

# SqlToCpp
This was created to help bridge the gap of a legacy project that uses SQLite.
Sqlite3 is commonly used in embedded products where C/C++ is the target language.
SqlToCpp is a python tools to help create structures that represent the database in C++.

Main goals that will define the first stable release
* Convert a SQlite3 schema into a C++ structure - This is currently implemented
* Create callback functions that are used with SQLite3 C API - This is being worked on next
* Create an API from the C++ structures to perform CRUD opperations
* Create an API that performs SELECT with JOINs if requested

Future goals for other releases
* Take a C++ structure header file and turn it into a SQLite schema
* Diff two SQL schemas and create update script
* Support other SQLs
