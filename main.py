from flask import Flask, render_template, request, session, jsonify
#from dataEntrySignin import DataEntrySignin
#from income import Income
import json

app=Flask(__name__)
app.secret_key="good"

vehicle = {}

@app.route('/')
def hello_world():
    user = request.args.get('user')
    lat = request.args.get('lat')
    vehicle[user] = lat  
    #return render_template('firstPage.html')

@app.route('/fetchDriver')
def login_to_world():
    user = request.args.get('user')
    return vehicle[user]

'''@app.route('/register')
def register_in_world():
    #return "hello_world"
    return render_template('registration.html')


@app.route('/auth/login',methods=['GET','POST'])
def login_user():
    usermail = request.form['usermail']
    passw= request.form['passw']
    
    k=DataEntrySignin.validate(usermail,passw)
    if(k==1):
        return render_template("home.html")
    else:
        return render_template("tryagain.html")
    
@app.route('/auth/register',methods=['POST'])
def register_user():
    usermail = request.form['usermail']
    passw= request.form['passw']
    
    #DataEntrySignin.
    #if(usermail!=" " and passw!=" "):
    d = DataEntrySignin(usermail,passw)
    d.register()
    
    return render_template("login.html") #,usermail=session['usermail'])



@app.route('/incomefinder',methods=['GET','POST'])
def loan_income_predict():
    state = request.form['st']
    district= request.form['dis']
    land=request.form['land']
    crop=request.form['crop']
        
    
    i=Income(state,district,land,crop)
    i.predictor()    
    
    l=DataEntrySignin.showIncome()
    print(l)
    
    return render_template("result.html" , data=l)'''

          
if __name__ == "__main__":
    #app.debug=True
    app.run()
