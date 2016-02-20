// Created by sqltocpp

#ifndef SQLTOCPP_fun_db_HPP
#define SQLTOCPP_fun_db_HPP

namespace fun_db 
{
    class people;
    class cats;
    class home;
    class state;

    class people
    {
        int id;
        std::string first_name;
        std::string last_name;
        int age;
        int home;

        static int sqlCallback(void *pArg, int argc, char **text, char **columnName);
    };
    class cats
    {
        int id;
        std::string first_name;
        int owner;
        std::string color;

        static int sqlCallback(void *pArg, int argc, char **text, char **columnName);
    };
    class home
    {
        int id;
        std::string address;
        int zip_code;
        int state;

        static int sqlCallback(void *pArg, int argc, char **text, char **columnName);
    };
    class state
    {
        int id;
        std::string name;

        static int sqlCallback(void *pArg, int argc, char **text, char **columnName);
    };


    static int people::sqlCallback(void *pAarg, int argc, char **text, char **columnName)
    {
        auto *list = (std::vector<people>*) pArg;
        people rowToAdd;
        stringstream value;
    
        for (int i = 0; i < argc; i++)
        {
            if (!str_cmp(columnName[i], "id"))
                rowToAdd.id << value.str(text[i]);
            if (!str_cmp(columnName[i], "first_name"))
                rowToAdd.first_name << value.str(text[i]);
            if (!str_cmp(columnName[i], "last_name"))
                rowToAdd.last_name << value.str(text[i]);
            if (!str_cmp(columnName[i], "age"))
                rowToAdd.age << value.str(text[i]);
            if (!str_cmp(columnName[i], "home"))
                rowToAdd.home << value.str(text[i]);
    
        }
    }
    
    static int cats::sqlCallback(void *pAarg, int argc, char **text, char **columnName)
    {
        auto *list = (std::vector<cats>*) pArg;
        cats rowToAdd;
        stringstream value;
    
        for (int i = 0; i < argc; i++)
        {
            if (!str_cmp(columnName[i], "id"))
                rowToAdd.id << value.str(text[i]);
            if (!str_cmp(columnName[i], "first_name"))
                rowToAdd.first_name << value.str(text[i]);
            if (!str_cmp(columnName[i], "owner"))
                rowToAdd.owner << value.str(text[i]);
            if (!str_cmp(columnName[i], "color"))
                rowToAdd.color << value.str(text[i]);
    
        }
    }
    
    static int home::sqlCallback(void *pAarg, int argc, char **text, char **columnName)
    {
        auto *list = (std::vector<home>*) pArg;
        home rowToAdd;
        stringstream value;
    
        for (int i = 0; i < argc; i++)
        {
            if (!str_cmp(columnName[i], "id"))
                rowToAdd.id << value.str(text[i]);
            if (!str_cmp(columnName[i], "address"))
                rowToAdd.address << value.str(text[i]);
            if (!str_cmp(columnName[i], "zip_code"))
                rowToAdd.zip_code << value.str(text[i]);
            if (!str_cmp(columnName[i], "state"))
                rowToAdd.state << value.str(text[i]);
    
        }
    }
    
    static int state::sqlCallback(void *pAarg, int argc, char **text, char **columnName)
    {
        auto *list = (std::vector<state>*) pArg;
        state rowToAdd;
        stringstream value;
    
        for (int i = 0; i < argc; i++)
        {
            if (!str_cmp(columnName[i], "id"))
                rowToAdd.id << value.str(text[i]);
            if (!str_cmp(columnName[i], "name"))
                rowToAdd.name << value.str(text[i]);
    
        }
    }
    


};


#endif

