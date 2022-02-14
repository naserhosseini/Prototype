import csv
import pandas as pd
import mysql.connector
from datetime import datetime,timedelta
from mysql.connector import errorcode

class Update:
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

    def add_purchase(self,reciept_id,date,product,type,quantities,delivery,status=False):
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
        self.reciept_id=reciept_id
        self.date=date
        self.product=product
        self.type=type
        self.quantities=quantities
        self.delivery=delivery
        self.status=status
        _col='customer_id,date,product,type,quantities,delivery,status'
        _val='{},"{}","{}","{}",{},"{}",{}'.format(reciept_id,date,product,type,quantities,delivery,status)
        _sql = 'INSERT orders ({}) VALUES ({});'.format(_col, _val)
        mycrs.execute(_sql)
        cnx.commit()


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

'''Naser=Employee()
Naser.add(name='Naser',DOB='4/28/1980')
Nafise=Employee()
Nafise.add('Nafiseh','3/24/1985')
Nafise.UpdateEmployee('2020/01/20',new_salary=3400,new_email='nafiseh@info.com')
Naser.UpdateEmployee('2020/5/12',new_salary=2000,new_phone='888-777-6655')
Nafise.UpdateEmployee('2020/10/15',new_salary='5500')
bdCake=Order()
bdCake.add(customer_id=12,date='2021/12/21',product='cake',type='8X6',quantities=1,delivery='2021/12/25')
bdCake.add(customer_id=30,date='2020/12/21',product='cake',type='8',quantities=1,delivery='2020/12/25')
for item in bdCake.ongoing_orders():
    print(item)'''
cnx.close()