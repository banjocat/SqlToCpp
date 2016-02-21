[![Build Status](https://travis-ci.org/banjocat/SqlToCpp.svg?branch=master)](https://travis-ci.org/banjocat/SqlToCpp) -- Travis

This is in development and has not reached a stable release.

# SqlToCpp
## The problem this solves
I am working with a legacy sqlite3 database used on a complex embedded system.
They choose to map sqlite3 data to C/C++ structures. This causes a huge problem
because we are defining the structure of the database in two locations. It requires a lot
of work to keep it in sync. 
## How it solves it
SqlToCpp parses a sqlite3 schema and creates C/C++ structures and an API that can be used.
It then can be run again when database migrations work. This allows leveraging of the compiler
to catch changes in the database schema throughout the code base. 
## Why not just use a standard ORM
The problem with C/C++ ORMs that are popular is they don't really map to C/C++. It's a mapping
to a Domain Specific Language. You then end up having to write a bridge that maps the ORM to
C/C++ class/structures. Consider SQlalchemy or Django's ORM, it maps to a class. 
## Why not use boost + maps
A valid argument. Maps alone aren't good enough because they can only represent 1 datatype.
But by using boost you can solve this problem. Why I choose not to do this is because the end
result is easier to meld into legacy systems. But I believe that one day someone will write
the above. But this is not that project.



### Required for stable release. 
[x] Convert a SQlite3 schema into a C++ structure

[x] Create callback functions that are used with SQLite3 C API

[ ] Documentation in README.md on how this tools works

[ ] Create an API from the C++ structures to perform CRUD opperations

[ ] Create an API that performs SELECT with JOINs if requested



### Future goals for other releases that probably won't ever happen. They are outside my need at this moment

[ ] Take a C++ structure header file and turn it into a SQLite schema

[ ] Diff two SQL schemas and create update script

[ ] Support other SQLs
