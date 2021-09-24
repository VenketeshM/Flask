from flask import Flask, render_template

app = Flask(__name__) 
# app = Flask(__name__, template_folder='template') 


@app.route("/")
def hello():
    return render_template('index.html')


@app.route("/about")
def harry():
    name = "venky"
    return render_template('about.html', name=name)

@app.route("/bootstrap")
def bootstrap():
    return render_template('bootstrap.html')


if __name__ == '__main__':
    app.run(debug=True)

