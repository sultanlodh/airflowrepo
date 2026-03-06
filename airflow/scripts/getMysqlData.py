import pandas as pd
import mysql.connector as mysql
import os
import sys
import logging
import json

logging.basicConfig(level=logging.INFO)

class MySQLDataExtractor:

    def __init__(self, db_config):
        self.db_config = db_config
        self.connection = None
        self.cursor = None

    def get_connection(self):
        try:
            self.connection = mysql.connect(**self.db_config)
            self.cursor = self.connection.cursor()

            if self.connection:
                logging.info("MySQL connection established")
                return self.connection, self.cursor

        except Exception as e:
            logging.exception("MySQL connection failed: %s", e)
            return None
        
    def get_data(self):

        try:

            sql = """SELECT order_id, order_date, ship_date, region, country 
                 FROM ecommerce_db.ecommerce_sales limit 3;
              """    
            self.cursor.execute(sql)
            rows = self.cursor.fetchall()

            if rows:
                logging.info("table have some data")

                #columns = [col[0] for col in self.cursor.description]
                #df0 = pd.DataFrame(rows, columns=columns)

                df0 = pd.read_sql(sql, self.connection)

                if not df0.empty:
                    logging.info("Dataframe created successfull")
                    return df0

        except Exception as e:
            logging.exception("Data error:", e)

    def run(self):
        result = self.get_connection()

        if result:
            connection, cursor = result
            logging.info("Extractor running")
        else:
            logging.error("Could not start extractor")

        df0 = self.get_data()
        print("Data \n", df0)  

        self.cursor.close()
        self.connection.close()  


# if __name__ == "__main__":

#     db_config = {
#         "host": "127.0.0.1",
#         "user": "root",
#         "password": "MySecretPassword123",
#         "database": "ecommerce_db",
#         "port": 14306
#     }

#     extractor = MySQLDataExtractor(db_config)
#     extractor.run()