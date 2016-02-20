
#include <string>
#include <sstream>

namespace SqlToCpp 
{

    class Table
    {
        public:
        virtual std::string CreateSql();
        virtual std::string UpdateSql(const std::string& where);
        virtual std::string SelectSql(const std::string& where);
        virtual std::string DeleteSql(const std::string& where);

        static virtual int sql_callback(void *pAarg, int argc, char **text, char **columnName);

        const std::string d_tableName;
        const std::string d_defaultWhere; // Usually the ID
    };

}


