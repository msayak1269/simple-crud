from flask import(
    Flask,redirect,render_template,url_for,request
)
import os
import json
import requests

app = Flask(__name__,static_url_path="")
app.config["SEND_FILE_MAX_AGE_DEFAULT"]=0
app.secret_key="msaya1269"

APP_ROOT=os.path.dirname(os.path.abspath(__file__))

@app.route("/",methods=["POST","GET"])
def home():
    if request.method == "GET":
        json_file = open(f"{APP_ROOT}/db/data.json","r")
        data = json.load(json_file)
        json_file.close()
        messege=data["messege"]
        if len(messege)==0:
            messege+="No Messege Yet!!!Please add one"
            return render_template("index.html",messege=messege,title="",time="")
        else:
            title=data["title"]
            time=data["time"]
            return render_template("index.html",title=title,messege=messege,time=time)
    
    else:
        title=request.form.get("title")
        messege=request.form.get("messege")
        time=request.form.get("time")
        data={
            "title":title,
            "messege":messege,
            "time":time
        }
        json_file = open(f"{APP_ROOT}/db/data.json","w")
        json_file.seek(0)
        json.dump(data,json_file,indent=2)
        json_file.close()
        return redirect(url_for("home"))
        
@app.route("/form")
def form():
    json_file = open(f"{APP_ROOT}/db/data.json","r")
    data = json.load(json_file)
    json_file.close()
    messege=data["messege"]
    if len(messege)==0:
        return render_template("form.html",messege=messege,title="",time="")
    else:
        title=data["title"]
        time=data["time"]
        return render_template("form.html",title=title,messege=messege,time=time)

# @app.route("/news")
# def news():
#     return render_template("news.html")


if __name__=="__main__":
    app.run(port=5001,debug=True,host='0.0.0.0')