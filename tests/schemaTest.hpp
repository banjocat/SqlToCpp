// Generated by SqlToCpp

#include <string>

struct people
{
    int id;
    std::string first_name;
    std::string last_name;
    int age;
    int home;
};

struct cats
{
    int id;
    std::string first_name;
    int owner;
    std::string color;
};

struct home
{
    int id;
    std::string address;
    int zip_code;
    int state;
};

struct state
{
    int id;
    std::string name;
};
