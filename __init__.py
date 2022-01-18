import time
import json
import yaml
import os
from flask import Flask,redirect,url_for,render_template,request
from datetime import date
from flask_mysqldb import MySQL


"""
    invoke the flask object here.
"""
app = Flask(__name__,template_folder='templates',static_folder='static')

"""
    created the date object and format it to month and year only
    for the top part of the calendar event
"""
__date = date.today().strftime("%B %Y")


""" 
    get the database info in the yaml file
"""
filename = os.path.join(app.static_folder,'database','database.yaml')
with open(filename,'r') as file:
    __db_info = yaml.load(file,Loader=yaml.FullLoader)     

"""
    give the database info in the flask 
"""
app.config['MYSQL_HOST'] = __db_info['host']
app.config['MYSQL_USER'] = __db_info['user']
app.config['MYSQL_PASSWORD'] = __db_info['password']
app.config['MYSQL_DB'] = __db_info['database']

mysql = MySQL(app)

"""
    created the single route here
"""
@app.route('/')
@app.route('/home',methods=['POST'])
def home():
    
    """
        to put the html in the browser
        you need to render it.

        also the date object that i created before is included in the parameter
    """

    """ 
        this variable will store the event details that will
        store in the database
    """
    title:str = request.form.get('event')
    toDate:str = request.form.get('toDate')
    fromDate:str = request.form.get('fromDate')

    """ 
        check if the data is not empty so cant 
        send empty data
    """
    if not title == None and not toDate == None and not fromDate == None:
        """ 
            get data in the database
        """
        cursor = mysql.connection.cursor()
        """ 
            using procedure to prevent dynamic query in the application
        """
        cursor.execute(''' call CalendarEvent2.addevent_proc3(%s,%s,%s);''',(title,toDate,fromDate))
        mysql.connection.commit()
        cursor.close()
        return render_template('calendar.html',year=__date,status='SAVED')

    return render_template('calendar.html',year=__date,status='')

    




""" 
    to run the flask you need to invoke the method needed
    also i included the debug mode because in default 
    it's running on production mode.
"""
if __name__ == '__main__':
    app.run(debug=True)



