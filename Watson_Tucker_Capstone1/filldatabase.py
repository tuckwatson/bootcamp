from enum import unique
import os
from forms import  AddForm , DelForm
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import sqlalchemy as sq
import pandas as pd
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import mysql.connector
from Database import Sales, Employees

con=sq.create_engine('mysql+pymysql://root:password123@localhost/sales_data')

employee_table = pd.read_csv(r'C:\Users\tuckw\Documents\Projects\Watson_Tucker_Capstone1\employee_table.csv')
employee_table.to_sql("employee_info",con,if_exists="append", index=False) 


df = pd.read_csv(r'C:\Users\tuckw\Documents\Projects\Watson_Tucker_Capstone1\rawdata_csv.csv')
df.to_sql("sales_raw_data",con,if_exists="append", index=False)


prices_table = pd.read_csv(r'C:\Users\tuckw\Documents\Projects\Watson_Tucker_Capstone1\Prices_table.csv')
prices_table.to_sql("prices_table",con,if_exists="append", index=False)


date_table = pd.read_csv(r'C:\Users\tuckw\Documents\Projects\Watson_Tucker_Capstone1\Date_table.csv')
date_table.to_sql("date_table",con,if_exists="append", index=False)



