from enum import unique
import os
from forms import  AddForm, AddPrice, DelForm, DelProd
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import sqlalchemy as sq
import pandas as pd
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base




app = Flask(__name__)
# Key for Forms
app.config['SECRET_KEY'] = 'mysecretkey'

############################################

        # SQL DATABASE AND MODELS

##########################################
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password123@localhost/sales_data'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)


#Creating each individual table in the sales_data database.

class Sales(db.Model):

    __tablename__ = 'sales_raw_data'
    Index = db.Column(db.Integer, primary_key = True)
    ITEM_CODE = db.Column(db.String(255), nullable=False)
    EMP_ID = db.Column(db.String(6))
    Year = db.Column(db.Integer)
    Week = db.Column(db.Integer)
    Amount = db.Column(db.Integer)
    def __init__(self,Index, ITEM_CODE, EMP_ID, Year, Week, Amount):
        self.Index = Index
        self.ITEM_CODE = ITEM_CODE
        self.EMP_ID = EMP_ID
        self.Year = Year
        self.Week = Week
        self.Amount = Amount


class Employees(db.Model):

    __tablename__ = 'employee_info'

    EMPID = db.Column(db.String(6), primary_key= True)
    Region = db.Column(db.Text)
    PayGrade = db.Column(db.Text)
    Sales_Team_Lead = db.Column(db.String(255))

    def __init__(self,EMPID,Region, PayGrade, Sales_Team_Lead):
        self.EMPID = EMPID
        self.Region = Region
        self.PayGrade = PayGrade
        self.Sales_Team_lead = Sales_Team_Lead

class Date(db.Model):
    __tablename__ = 'date_table'

    date_key = db.Column(db.Integer, primary_key= True)
    Week = db.Column(db.Integer)
    Date = db.Column(db.String(255))
    Sales_Period = db.Column(db.String(255))
    Sales_Year = db.Column(db.Integer)
    Quarter = db.Column(db.Integer)

    def __init__(self,date_key,Week, Date, Sales_Period, Sales_Year, Quarter):
        self.date_key = date_key
        self.Week = Week
        self.Date = Date
        self.Sales_Period = Sales_Period
        self.Sales_Year = Sales_Year
        self.Quarter = Quarter

class Prod(db.Model):
    __tablename__ = 'prices_table'
    prod_key = db.Column(db.Integer, primary_key=True)
    PROD_CODE = db.Column(db.String(255))
    PROD_NAME = db.Column(db.String(255))
    Year = db.Column(db.Integer)
    Price = db.Column(db.Integer)

    def __init__(self,prod_key, PROD_CODE, PROD_NAME, Year, Price):
        self.prod_key = prod_key
        self.PROD_CODE = PROD_CODE
        self.PROD_NAME = PROD_NAME
        self.Year = Year
        self.Price = Price




db.create_all()



# ###########################################

#         # VIEWS WITH FORMS

# #########################################
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/add', methods=['GET', 'POST'])
def add_sale():
    form = AddForm()

    if form.validate_on_submit():
        Index = form.Index.data
        EMP_ID = form.EMP_ID.data
        Year = form.Year.data
        ITEM_CODE = form.ITEM_CODE.data
        Week = form.Week.data
        Amount = form.Amount.data

        # Add new Sale to database
        new_sale = Sales(Index, ITEM_CODE, EMP_ID,Year, Week, Amount)
        db.session.add(new_sale)
        db.session.commit()
    
        return redirect(url_for('add_sale'))
    return render_template('add.html',form=form)

@app.route('/add_prod', methods=['GET', 'POST'])
def add_prod():
    form = AddPrice()

    if form.validate_on_submit():
        prod_key = form.prod_key.data
        PROD_CODE = form.PROD_CODE.data
        PROD_NAME = form.PROD_NAME.data
        Year = form.Year.data
        Price = form.Price.data

        # Add new Product Price to the database
        new_prod = Prod(prod_key, PROD_CODE, PROD_NAME, Year, Price)
        db.session.add(new_prod)
        db.session.commit()
    
        return redirect(url_for('add_sale'))
    return render_template('add_prod.html',form=form)

@app.route('/delete', methods=['GET', 'POST'])
def del_sale():

    form = DelForm()

    if form.validate_on_submit():
        Index = form.Index.data
        sale = Sales.query.get(Index)
        db.session.delete(sale)
        db.session.commit()

        #Delete Sale from the Database.

        return redirect(url_for('add_sale'))
    return render_template('delete.html',form=form)

@app.route('/del_prod', methods=['GET', 'POST'])
def del_prod():

    form = DelProd()

    if form.validate_on_submit():
        prod_key = form.prod_key.data
        product = Prod.query.get(prod_key)
        db.session.delete(product)
        db.session.commit()

        #Delete Sale from the Database.

        return redirect(url_for('add_sale'))
    return render_template('del_prod.html',form=form)



if __name__ == '__main__':
    app.run(debug=True)



