import mysql.connector
import pandas as pd

class MysqlIO:
    """Connect to MySQL server with python and excecute SQL commands."""
    def __init__(self, host='relational.fit.cvut.cz', database='financial', user='guest', password='relational'):
        try:
            # Change the host, user and password as needed
            connection = mysql.connector.connect(host=host,
                                                 database = database,
                                                 user=user,
                                                 password=password,
                                                 use_pure=True
                                                 )
            if connection.is_connected():
                db_info = connection.get_server_info()
                print("Connected to MySQL Server version", db_info)
                print("Your're connected to database:", database)
                self.connection = connection
        except Exception as e:
            print("Error while connecting to MySQL", e)
    
    def execute(self, query, header=False):
        """Execute SQL commands and return retrieved queries."""
        cursor = self.connection.cursor(buffered=True)
        cursor.execute(query)
        try:
            record = cursor.fetchall()
            if header:
                header = [i[0] for i in cursor.description]
                return {'header': header, 'record': record}
            else:    
                return record
        except Exception as e:
            print(e)
    
    def execute_to_df(self, query):
        """Return the retrieved SQL queries into pandas dataframe."""
        res = self.execute(query, header=True)
        df = pd.DataFrame(res['record'])
        df.columns = res['header']
        return df

if __name__ == '__main__':
    db = MysqlIO(host='relational.fit.cvut.cz', 
            database='financial', 
            user='guest', 
            password='relational')
    
    print(db.execute('SHOW TABLES'))
    
