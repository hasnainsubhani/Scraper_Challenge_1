import mysql.connector as conn
import csv
class database:

    def __init__(self):
        pass

    def get_connection(self):
        mydb = conn.connect(host="localhost",username="root",password="hasnain@@1",database="testdb")
        return mydb
    
    def create_table(self):
        mydb = self.get_connection()
        cursor = mydb.cursor()
        cursor.execute("create table if not exists video_details(video_Id int AUTO_INCREMENT PRIMARY KEY,Sr_No int, video_Title varchar(50),video_description varchar(500),likes int,video_url varchar(100))")
        mydb.commit()

    #cursor.execute("show tables")
    #_tables = cursor.fetchall()
    #print(_tables)

    def import_data_FromCSV(self,filename):
        val = ""
        query = ""
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


    def insert_data(self,val):
        query = ""
        mydb = self.get_connection()
        cursor = mydb.cursor()
        
        query = "insert into video_details(Sr_No,video_Title,video_description,likes,video_url) values("+ val + ")"
        #print(query)
        cursor.execute(query)
        mydb.commit()