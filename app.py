from flask import Flask
from flask import render_template, request, url_for, redirect
from database import *

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def catbook_home():
    
    if request.method=='GET':
        cats = get_all_cats()
        return render_template("home.html", cats=cats)
    else:
        name=request.form['search']
        cat=search(name)
        return redirect(url_for('cb_dts',cat.id))

@app.route('/cats/<int:cat_id>')
def cb_dts(cat_id):
    cat = get_cat(cat_id)
    return render_template("cat.html", cat=cat)
@app.route('/cats/add', methods=['GET','POST'])
def add_cat():
    if request.method=='GET':
        return render_template('create.html')
    else:
        name=request.form['name']
        create_cat(name)
        return redirect(url_for('catbook_home'))
    
if __name__ == '__main__':
   app.run(debug = True)
