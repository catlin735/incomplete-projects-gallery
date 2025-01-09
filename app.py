from flask import Flask,render_template,redirect,request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///projects.sqlite'

db = SQLAlchemy(app)
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(1000), nullable=False)
    description = db.Column(db.Text)

@app.route('/')
def index():
    projects = Project.query.all()
    return render_template('index.html',projects=projects)

@app.route('/submit/', methods=('GET', 'POST'))
def submit():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        project = Project(title=title,
                          description=description)
        db.session.add(project)
        db.session.commit()
    return redirect('/')