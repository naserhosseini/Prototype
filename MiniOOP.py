import csv
import pandas as pd
import mysql.connector
from mysql.connector import errorcode

class Update:
    def __init__(self,file_path):
        '''

        :param file_path: the CSV file

        '''
        with open(file_path, 'r') as csv_feed:
            data = csv.reader(csv_feed)
        self.data=data

    def add_order(self,customer_id,date,product,type,quantities,delivery,status=False):
        '''
        add placed order to the SQL data base
        :customer_id:
        :param date: order date
        :param product: either cookies, or cupcakes or cakes
        :param type: [{'cookies':['Large','Small']},{cupcakes:['chocolate','vanilla','strawberry','coconut','lemon','carrot','red velvet','pineapple','rainbow']},{cakes:['8X6','10X8','6X4','6','8','10']}]
        :param quantities:[{'cookies':dozen},{cupcakes:dozen},{cakes:initger]
        :param delivery: delivery date
        :param status: boolean, if the order is done (true) or not (false)
        '''
        self.customer_id=customer_id
        self.date=date
        self.product=product
        self.type=type
        self.quantities=quantities
        self.delivery=delivery
        self.status=status
        _col='customer_id,date,product,type,quantities,delivery,status'
        _val='{},"{}","{}","{}",{},"{}",{}'.format(customer_id,date,product,type,quantities,delivery,status)
        _sql = 'INSERT orders ({}) VALUES ({});'.format(_col, _val)
        mycrs.execute(_sql)
        cnx.commit()
        return

    def add_purchase(self,reciept_id,date,product,type,quantities,delivery,status=False):
        '''
        add purchase to the SQL data base
        :customer_id:
        :param date: order date
        :param product: either cookies, or cupcakes or cakes
        :param type: [{'cookies':['Large','Small']},{cupcakes:['chocolate','vanilla','strawberry','coconut','lemon','carrot','red velvet','pineapple','rainbow']},{cakes:['8X6','10X8','6X4','6','8','10']}]
        :param quantities:[{'cookies':dozen},{cupcakes:dozen},{cakes:initger]
        :param delivery: delivery date
        :param status: boolean, if the order is done (true) or not (false)
        '''
        self.reciept_id=reciept_id
        self.date=date
        self.product=product
        self.type=type
        self.quantities=quantities
        self.delivery=delivery
        self.status=status
        _col='customer_id,date,product,type,quantities,delivery,status'
        _val='{},"{}","{}","{}",{},"{}",{}'.format(reciept_id,date,product,type,quantities,delivery,status)
        _sql = 'INSERT inventory ({}) VALUES ({});'.format(_col, _val)
        mycrs.execute(_sql)
        cnx.commit()
        return

MySqldf=pd.read_csv('MySql.cfg')
user=MySqldf['Value'][0]
password=MySqldf['Value'][1]
host=MySqldf['Value'][2]

try:
    config = {
        'user': user,
        'password': password,
        'host': host,
        'database': 'minioop',
        'raise_on_warnings': True}
    cnx = mysql.connector.connect(**config)
    mycrs=cnx.cursor()
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
    quit()

cnx.close()