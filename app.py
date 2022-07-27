from flask import Flask, redirect, render_template,url_for,request,redirect,send_from_directory
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from KMap import kmap4
import os

def calling_python_Kmap_code(a,b):
    index=[]
    for i in range(16):
        if a[i]=='1':
            index+=[i]
    x1,x2,x3,x4=b
    ans=kmap4(2,index,x1,x2,x3,x4)
    return(ans)

port = int(os.environ.get('PORT', 5000))


app=Flask('__name__')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path,'static'),'favicon.ico',mimetype='image/favicon.png')

@app.route('/',methods=['POST','GET'])

def index():
    if request.method=="POST":
        a=[]
        b=[]
        for i in ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16']:
            a+=[request.form[i] ] 
        for i in ['floating1','floating2','floating3','floating4']:
            b+=[request.form[i]]

        tasks=calling_python_Kmap_code(a,b)
        return render_template('index_4x4.html',tasks=tasks)

    else:
        try:
            return render_template('index_4x4.html',tasks=tasks)
        except:
            return render_template('index_4x4.html')

if __name__== "__main__":
    app.debug=True
    app.run()
