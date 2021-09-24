from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) 
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/codingera'
db = SQLAlchemy(app)

class Contacts(db.Model):
    '''
    sno, name, phone_num, msg, date, email
    '''
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    phone_num = db.Column(db.String(12), nullable=False)
    msg = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12), nullable=False)
    email = db.Column(db.String(20), nullable=False)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/post")
def post():
    return render_template('post.html')


@app.route("/contact", methods = ['GET', 'POST'])
def contact():
    if (request.method == 'POST'):
        '''Add Entry to database '''
    request.form.get('')
    return render_template('contact.html')




if __name__ == '__main__':
    app.run(debug=True)

