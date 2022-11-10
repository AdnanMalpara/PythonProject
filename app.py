from flask import Flask,render_template,request,url_for,redirect
import database as db 

app=Flask(__name__)
@app.route('/')
def home():
    data=db.readall()
    print(data) 
    return render_template("index.html",data=data,msg="Welcome") 

@app.route('/insert')
def insert():
    id=request.args.get("ID")
    name=request.args.get("Name")
    location=request.args.get("Location")
    companyname=request.args.get("CompanyName")
    post=request.args.get("Post")
    print(id,name,location,companyname,post)
    if not(id==None or name==None or location==None or companyname==None or post==None):
        db.insertrecord(id,name,location,companyname,post)
        return redirect(url_for('home'))
    return render_template("insert.html")

@app.route('/delete/<id>')
def delete(id):
    db.deleterecord(id)
    return redirect(url_for('home'))

@app.route('/update')
def updaterecord():

    id=request.args.get('ID')
    name=request.args.get('Name')
    location=request.args.get("Location")
    companyname=request.args.get("CompanyName")
    post=request.args.get("Post")
    data=(id,name,location,companyname,post)
    db.updaterecord(data)
    return redirect(url_for('home'))


@app.route('/update/<id>')
def update(id):
    data=db.readbyid(id)
    return render_template("update.html",data=data)

app.run(debug=True) 
