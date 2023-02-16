import mysql.connector as conn
import csv
import logging
class database:

    def __init__(self):
        pass

    def get_connection(self):
        mydb = conn.connect(host="localhost",username="root",password="hasnain@@1",database="testdb")
        return mydb
    
    def create_table(self):
        try:
            mydb = self.get_connection()
            cursor = mydb.cursor()
            cursor.execute("create table if not exists video_details(video_Id int AUTO_INCREMENT PRIMARY KEY,Sr_No int, video_Title varchar(500),video_description varchar(500),likes varchar(50),video_url varchar(100))")
            mydb.commit()
        except Exception as e:
            logging.info(e)

    #cursor.execute("show tables")
    #_tables = cursor.fetchall()
    #print(_tables)

    def import_data_FromCSV(self,filename):
        val = ""
        query = ""
        try:
            mydb = self.get_connection()
            cursor = mydb.cursor()
            with open(filename,'r') as f:
                _data = csv.reader(f,delimiter='\n')
                for row in _data:
                    val = '\'' +str(row[0]).replace(',','\',\'')+'\''
                    query = "insert into video_details(Sr_No,video_Title,video_description,likes,video_url) values("+ val + ")"
                    cursor.execute(query)
                mydb.commit()
            f.close() 
        except Exception as e:
            logging.info(e)

    def insert_data(self,val):
        query = ""
        try:
            mydb = self.get_connection()
            cursor = mydb.cursor()
            
            query = "insert into video_details(Sr_No,video_Title,video_description,likes,video_url) values("+ val + ")"
            #print(query)
            cursor.execute(query)
            mydb.commit()
        except Exception as e:
            logging.info(e)