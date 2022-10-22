from flask import Flask,render_template,redirect,request
app = Flask(__name__,template_folder="templates")


@app.route('/', methods=['GET',"POST"])
def world():
   

    if request.method == "POST":
        age1 = request.form.get('age1')
        smoke1 = request.form.get('smoke1')
        alcohol1 = request.form.get('alcohol1')
        waist1 = request.form.get('waist1')
        physical1 = request.form.get('physicalact')
        family1= request.form.get('family1')
        add = int(age1)+int(smoke1)+int(alcohol1)+int(waist1)+int(physical1)+int(family1)
        return render_template('final.html', add=add)
    return render_template('index.html')

@app.route('/back',methods=['POST','GET'])
def back():
    if request.method=='POST':
        return render_template('index.html')
if __name__ =="__main__":
    app.run(debug=True,port=8000)
