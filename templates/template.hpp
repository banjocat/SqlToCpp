// Created by sqltocpp

#ifndef SQLTOCPP_{{database_name}}_HPP
#define SQLTOCPP_{{database_name}}_HPP

namespace {{database_name}} 
{
    {% for tables in tables %}
    class {{tables.name}};
    {% endfor %}

    {% for table in tables %}
    class {{table.name}}
    {
        {% for column in table.members %}
        {{column.c_type}} {{column.name}};
        {% endfor %}

        static int sqlCallback(void *pArg, int argc, char **text, char **columnName);
    };
    {% endfor %}


    {% for table in tables %}
    static int {{table.name}}::sqlCallback(void *pAarg, int argc, char **text, char **columnName)
    {
        auto *list = (std::vector<{{ table.name }}>*) pArg;
        {{ table.name }} rowToAdd;
        stringstream value;
    
        for (int i = 0; i < argc; i++)
        {
            {% for column in table.members %}
            if (!str_cmp(columnName[i], "{{ column.name }}"))
                rowToAdd.{{column.name}} << value.str(text[i]);
            {% endfor %}
    
        }
    }
    
    {% endfor %}


};


#endif


