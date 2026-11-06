from abc import ABC, abstractmethod
import pyttsx3 as pt
import random as rm
from datetime import datetime as dt
import mysql.connector
con=mysql.connector.connect(
     host="localhost",
     user="root",
     password="Password",
     database="pythonsqlproject")
cur=con.cursor()
print("MySQL connected successfully!")
def save_transaction(transaction_id,payment_method,amount,transaction_date):
     cur.execute("insert into transactions values(%s,%s,%s,%s)",(transaction_id,payment_method,amount,transaction_date))
     con.commit()
     print("Transaction saved successfully!")
e=pt.init()
class payment(ABC):
    @abstractmethod
    def pay(self,amt):
        pass    
class phonepay(payment):
    def pay(self,amt):
        self.amt=amt
        msg=str(amt)+"rupees received by phonepay thank you boss"
        e.say(msg)
        e.runAndWait()
        transaction_id=rm.randint(100000,999999)
        transaction_date=dt.today()
        print("transaction_details")
        print("t_id:=",transaction_id)
        print("t_date:=",transaction_date)
        save_transaction(transaction_id,"phonepay",amt,transaction_date)
class gpay(payment):
    def pay(self,amt):
            self.amt=amt
            msg=str(amt)+"rupees received by googlepay thank you boss"
            e.say(msg)
            e.runAndWait()
            transaction_id=rm.randint(100000,999999)
            transaction_date=dt.today()
            print("transaction_details")
            print("t_id:=",transaction_id)
            print("t_date:=",transaction_date)
            save_transaction(transaction_id,"gpay",amt,transaction_date)
class paytm(payment):
     def pay(self,amt):
             self.amt=amt
             msg=str(amt)+"rupees received by paytm thank you boss"
             e.say(msg)
             e.runAndWait()
             transaction_id=rm.randint(100000,999999)
             transaction_date=dt.today()
             print("transaction_details")
             print("t_id:=",transaction_id)
             print("t_date:=",transaction_date)
             save_transaction(transaction_id,"paytm",amt,transaction_date)
choose=int(input("enter number 1.phonepay,2.googlepay,3.paytm  "))
amount=int(input("enter the amount:="))
if choose==1:
     app=phonepay()
elif choose==2:
     app=gpay()
elif choose==3:
     app=paytm()
else:
     print("invalid input")
if app is not None:
     app.pay(amount)
con.close()

