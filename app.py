from flask import Flask
from flask import render_template
from database import *

app = Flask(__name__)

@app.route('/')
def catbook_home():
    cats = get_all_cats()
    return render_template("home.html", cats=cats)

@app.route('/cats/<int:cat_id>')
def cb_dts(cat_id):
    cat = get_cat(cat_id)
    return render_template("cat.html", cat=cat)
    
if __name__ == '__main__':
   app.run(debug = True)
