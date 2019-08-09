from flask import Flask,render_template
import pymysql
import urllib.request
import json
import datetime 



'''connection = pymysql.connect(host='localhost',
                             user='root',
                             password='1234',
                             db='temp_mon_sys',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)'''

app = Flask(__name__)


@app.route('/')
def hello_world():
    try:
        connection = pymysql.connect(host='localhost',
                             user='root',
                             password='1234',
                             db='temp_mon_sys',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
        with connection.cursor() as cursor:
            cursor.execute("TRUNCATE temperaturedb")
            connection.commit()
    
    finally:            
        TS = urllib.request.urlopen("https://api.thingspeak.com/channels/572348/feeds.json?results=")
    
        response = TS.read()
        data=json.loads(response)
        
        
        
        feild_1=data['feeds']
        
        
        
        t=[]
        times=[]
        for x in feild_1:
            t = list(filter(None,t))
            times = list(filter(None,times))
            t.append(x['field1'])
            times.append(x['created_at'])
            
            with connection.cursor() as cursor:
                sql = "INSERT INTO temperaturedb(Temperature,Date) VALUES(%s,%s)"
                cursor.execute(sql,(t[-1],times[-1]))
                connection.commit()
            
        return render_template('indexwithbootstrap.html') 
    
@app.route('/history')
def history():
   connection = pymysql.connect(host='localhost',
                             user='root',
                             password='1234',
                             db='temp_mon_sys',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
   with connection.cursor() as cursor:
        sql = "select * from temperaturedb"
        cursor.execute(sql)
        rows = cursor.fetchall();
   return render_template('history.html',rows = rows)
    
    
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True,port=5000)
        
    
        
        
        
    
    	


