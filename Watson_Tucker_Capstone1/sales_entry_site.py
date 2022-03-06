import os
# from forms import  AddForm , DelForm, AddOwnerForm
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import sqlalchemy as sq
import pandas as pd
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

# class Employee(db.Model):

#     __tablename__ = 'employee_info'
#     EMP_ID = db.Column(db.String(9),primary_key = True)
#     Sales_Team_Lead = db.Column(db.Text, nullable=False)
#     region = db.Column(db.Text, nullable=False)


#     def __init__(self,emp_id, Sales_Team_Lead, region):
#         self.emp_id = emp_id
#         self.Sales_Team_Lead = Sales_Team_Lead
#         self.region = region


# db.create_all()

con=sq.create_engine('mysql+pymysql://root:password123@localhost/sales_data')

rawdata = pd.read_csv(r'C:\Users\tuckw\Documents\Projects\Watson_Tucker_Capstone1\rawdata_csv.csv')

rawdata.to_sql("raw_sales",con,if_exists="replace", index=False)

employee_table = pd.read_csv(r'C:\Users\tuckw\Documents\Projects\Watson_Tucker_Capstone1\employee_table.csv')
employee_table.to_sql("employee_info",con,if_exists="replace", index=False)

date_table = pd.read_csv(r'C:\Users\tuckw\Documents\Projects\Watson_Tucker_Capstone1\date_table.csv')
date_table.to_sql("date_table",con,if_exists="replace", index=False)


prices_table = pd.read_csv(r'C:\Users\tuckw\Documents\Projects\Watson_Tucker_Capstone1\Prices_table.csv')
prices_table.to_sql("prices_table",con,if_exists="replace", index=False)

# ############################################

#         # VIEWS WITH FORMS

# ##########################################
# @app.route('/')
# def index():
#     return render_template('home.html')

# @app.route('/add', methods=['GET', 'POST'])
# def add_pup():
#     form = AddForm()

#     if form.validate_on_submit():
#         name = form.name.data
#         color = form.color.data

#         # Add new Puppy to database
#         new_pup = Puppy(name,color)
#         db.session.add(new_pup)
#         db.session.commit()

#         return redirect(url_for('list_pup'))

#     return render_template('add.html',form=form)
# @app.route('/add_owner', methods=['GET', 'POST'])
# def add_owner():

#     form = AddOwnerForm()

#     if form.validate_on_submit():
#         name = form.name.data
#         pup_id = form.pup_id.data
#         # Add new owner to database
#         new_owner = Owner(name,pup_id)
#         db.session.add(new_owner)
#         db.session.commit()

#         return redirect(url_for('list_pup'))

#     return render_template('add_owner.html',form=form)

# @app.route('/list')
# def list_pup():
#     # Grab a list of puppies from database.
#     puppies = Puppy.query.all()
#     return render_template('list.html', puppies=puppies)

# @app.route('/delete', methods=['GET', 'POST'])
# def del_pup():

#     form = DelForm()

#     if form.validate_on_submit():
#         id = form.id.data
#         pup = Puppy.query.get(id)
#         db.session.delete(pup)
#         db.session.commit()

#         return redirect(url_for('list_pup'))
#     return render_template('delete.html',form=form)


# if __name__ == '__main__':
#     app.run(debug=True)

