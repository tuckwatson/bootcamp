from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField



class AddForm(FlaskForm):
    Index = IntegerField('Index of Sale:')
    ITEM_CODE = StringField('Item Code:')
    EMP_ID = StringField('Employee ID')
    Year = IntegerField('Year of Sale:')
    Week = StringField('Week of Sale (Just Week #):')
    Amount = IntegerField('Amount of Product Sold:')
    submit = SubmitField('Add Sale')


class DelForm(FlaskForm):

    Index = IntegerField('Index # of entry to remove:')
    submit = SubmitField('Remove entry')

class AddPrice(FlaskForm):
    prod_key = IntegerField('Product-Key:')
    PROD_CODE = StringField('PROD_CODE:')
    PROD_NAME = StringField('PROD_NAME')
    Year = IntegerField('Year of Given Price:')
    Price = StringField('Price of Product for Year:')
    submit = SubmitField('Add Product')

class DelProd(FlaskForm):

    prod_key = IntegerField('Index # of entry to remove:')
    submit = SubmitField('Remove entry')