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
        std::string CreateSql(const std::vector<std::string>& createColumns = std::vector<std::string>());
        std::string UpdateSql(
                const std::vector<std::string>& whereColumns,
                const std::vector<std::string>& updateColumns = std::vector<std::string>());
        std::string ReadSql(
                const std::vector<std::string>& whereColumns = std::vector<std::string());;
        std::string DeleteSql(
                const std::vector<std::string>& whereColumns = std::vector<std::string());;
    };



    
    std::string CreateSql()
    {
        stringstream sql;

        sql << "INSERT INTO " << {{name}};
        if (createColumns.empty())
        {
            sql << " VALUES (";
            {% for column in table.columns %}
            sql << "'" << {{column.name}} << "',"
            {% endfor %}
            string removeComma(sql.str());
            removeComma.pop_back();
            sql.str(removeComma);
            sql << ");";
        }
        else 
        {
            sql << "(";
            for (auto column : createColumns)
            {
                sql << column << ",";
            }
            string removeComma(sql.str());
            removeComma.pop_back();
            sql.str(removeComma);
            sql << ");";
            {% for column in table.columns %}
            for (auto column : createColumns)
            {
                if (stringtoupper(column) == stringtoupper("{{column}}")
                    sql << "'" << {{column}} << "',"
            }
            {% endfor %}
        }

        return sql.str();
    };

    std::string UpdateSql(const std::string& wherColumns)
    {
    }

    {% endfor %}
};

#endif


