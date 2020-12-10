#importing the modules
import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

#intialising the Falsk , App get created
app = Flask(__name__)

# here it incdicate which datatbase you are using , what is username and passwword and localhost
# syntax                                           
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/name'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/contact1'

db = SQLAlchemy(app)

#note here in class you should write in capital ,example here Contactform
class Contactform(db.Model):
    #SNO , name , password , date , address ,gmail , contact
    #here unique means everthing solud be unique or not and nullable = it means not compulsory if it is true , write false
    SNO = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(50), nullable=False )
    date= db.Column(db.String(50)) #it will take automatically database
    address = db.Column(db.String(120),nullable=False )
    gmail = db.Column(db.String(120),nullable=False )
    contact= db.Column(db.String(50),nullable=False)
    


#here first homepage will get display in website

@app.route('/')
def home():
    return render_template ('index.html')

@app.route('/contact12',methods=['GET','POST'])
def contact12():
    if (request.method=='POST'):
        #fetching the data from contact form
       
       
       name =request.form.get('name')
       password =request.form.get('password')
       date =request.form.get('date')
       address =request.form.get('address')
       gmail =request.form.get('gmail')
       contact =request.form.get('contact')
        # syntax of adding     database variable name= fetching varable name
       entry= Contactform(name=name , password =password , date=date ,address = address ,gmail  =gmail ,contact=contact)
        # by using add and commit function date get stored in datatbase
       db.session.add(entry)
       db.session.commit()

       return render_template('index.html',result='Thank You For filling the form')


if __name__ == "__main__":
    app.run(debug=True)