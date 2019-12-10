import mysql.connector
import json
from datetime import datetime

class DBOperation():

    def __init__(self):
        file=open("./config.json","r")
        datadic=json.loads(file.read())
        file.close()
        self.mydb=mysql.connector.connect(host="localhost",user=datadic['username'],passwd=datadic['password'],database=datadic['database'])

    def CreateTables(self):
        cursor=self.mydb.cursor()
        cursor.execute("DROP TABLE if exists admin")
        cursor.execute("DROP TABLE if exists slots")
        cursor.execute("DROP TABLE if exists vehicles")
        cursor.execute("CREATE TABLE admin (id int(255) AUTO_INCREMENT PRIMARY KEY,username varchar(30),password varchar(30),created_at varchar(30))")
        cursor.execute("CREATE TABLE slots (id int(255) AUTO_INCREMENT PRIMARY KEY,vehicle_id varchar(30),space_for int(25),is_empty int(25))")
        cursor.execute("CREATE TABLE vehicles (id int(255) AUTO_INCREMENT PRIMARY KEY,name varchar(30),mobile varchar(30),entry_time varchar(30),exit_time varchar(30),is_exit varchar(30),vehicle_no varchar(30),vehicle_type varchar(30),created_at varchar(30),updated_at varchar(30))")
        cursor.close()

    def InsertOneTimeData(self,space_for_two,space_for_four):
        cursor=self.mydb.cursor()
        for x in range(space_for_two):
            cursor.execute("INSERT into slots (space_for,is_empty) values ('2','1')")
            self.mydb.commit()

        for x in range(space_for_four):
            cursor.execute("INSERT into slots (space_for,is_empty) values ('4','1')")
            self.mydb.commit()
        cursor.close()

    def InsertAdmin(self,username,password):
        cursor=self.mydb.cursor()
        val=(username,password)
        cursor.execute("INSERT into admin (username,password) values (%s,%s)",val)
        self.mydb.commit()
        cursor.close()

    def doAdminLogin(self,username,pasword):
        cursor=self.mydb.cursor()
        cursor.execute("select * from admin where username='"+username+"' and password='"+pasword+"'")
        data=cursor.fetchall()
        cursor.close()
        if len(data)>0:
            return True
        else:
            return False

    def getSlotSpace(self):
        cursor=self.mydb.cursor()
        cursor.execute("select * from slots")
        data=cursor.fetchall()
        cursor.close()
        return data

    def getCurrentVehicle(self):
        cursor=self.mydb.cursor()
        cursor.execute("select * from vehicles where is_exit='0'")
        data=cursor.fetchall()
        cursor.close()
        return data

    def getAllVehicle(self):
        cursor=self.mydb.cursor()
        cursor.execute("select * from vehicles where is_exit='1'")
        data=cursor.fetchall()
        cursor.close()
        return data

    def AddVehicles(self,name,vehicleno,mobile,vehicle_type):
        spacid=self.spaceAvailable(vehicle_type)
        if spacid:
            currentdata=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            data=(name,mobile,str(currentdata),'','0',vehicleno,str(currentdata),str(currentdata),vehicle_type)
            cursor=self.mydb.cursor()
            cursor.execute("INSERT into vehicles (name,mobile,entry_time,exit_time,is_exit,vehicle_no,created_at,updated_at,vehicle_type) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)",data)
            self.mydb.commit()
            lastid=cursor.lastrowid
            cursor.execute("UPDATE slots set vehicle_id='"+str(lastid)+"',is_empty='0' where id='"+str(spacid)+"'")
            self.mydb.commit()
            cursor.close()
            return True
        else:
            return "No Space Available for Parking"


    def spaceAvailable(self,v_type):
        cursor=self.mydb.cursor()
        cursor.execute("select * from slots where is_empty='1' and space_for='"+str(v_type)+"'")
        data=cursor.fetchall()
        cursor.close()

        if len(data)>0:
            return data[0][0]
        else:
            return False

    def exitVehicle(self,id):
        cursor=self.mydb.cursor()
        currentdata = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute("UPDATE slots set is_empty='1',vehicle_id='' where vehicle_id='"+id+"'")
        self.mydb.commit()
        cursor.execute("UPDATE vehicles set is_exit='1',exit_time='"+currentdata+"' where id='" + id + "'")
        self.mydb.commit()

