from flask import Flask, redirect, url_for, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
import url_class
import encode
import re


app = Flask(__name__)
app.secret_key = "not a secret"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
db = SQLAlchemy(app)

regex = regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)



@app.route("/", methods=["POST", "GET"])
def home():
    
    valid_url = True    
    if request.method == "POST":
        url = request.form["url"]
        
        if re.match(regex, url):
            
            modifier = request.form["modifier"] + '_'
            created_url = url_class.Url(long_url=url)
            
            db.session.add(created_url)
            db.session.commit()
            
            url_id = created_url.id
            
            created_url.short_url = encode.encode(modifier, url_id)
            
            db.session.add(created_url)
            db.session.commit()
            
            return render_template("index.html", url=created_url.short_url, valid=valid_url)
        else:
            valid_url = False
            
    return render_template("index.html", url="", valid=valid_url)


@app.route("/<suffix>/")
def send(suffix):
    print(suffix)
    url = url_class.Url.query.filter_by(short_url="http://127.0.0.1:5000/"+suffix).first()

    if url:
        long_url = url.long_url
        return redirect(long_url, code=302)
    else:
        return redirect(url_for("home"))


if __name__ == '__main__':
    url_class.init()
    app.run(debug=True)
    