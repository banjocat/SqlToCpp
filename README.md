[![Build Status](https://travis-ci.org/banjocat/SqlToCpp.svg?branch=master)](https://travis-ci.org/banjocat/SqlToCpp)

This is in developemnt and has not reached a stable release.

# SqlToCpp
This was created to help bridge the gap of a legacy project that uses SQLite.
Sqlite3 is commonly used in embedded products where C/C++ is the target language.
SqlToCpp is a python tools to help create structures that represent the database in C++.

Main goals
* Convert a SQlite3 schema into a C++ structure
* Create an API from the C++ structures to perform CRUD opperations
* Create an API that performs SELECT with JOINs if requested

Future goals still being decided
* Take a C++ structure header file and turn it into a SQLite schema
* Diff two SQL schemas and create update script
