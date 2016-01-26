// Created by sqltocpp

#ifndef SQLTOCPP_{{database_name}}_HPP
#define SQLTOCPP_{{database_name}}_HPP

namespace {{database_name}} 
{

    std::string stringtoupper(const std::string& lower)
    {
        string upper;
        for (auto c : lower)
            upper.push_back(toupper(c));

        return upper;
    };


    {% for tables in tables %}
    class {{tables.name}};
    {% endfor %}

    {% for table in tables %}
    class {{name}}
    {
        {% for column in table.columns %}
        {{column.ctype}} {{column.name}};
        {% endfor %}

        static int sqlCallback(void *pArg, int argc, char **text, char **columnName);
    };




    
};

#endif


