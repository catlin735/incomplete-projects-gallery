from flask import Flask,render_template,redirect,request
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///projects.db'

db = SQLAlchemy(app)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(1000), nullable=False)
    description = db.Column(db.Text)

@app.route('/',methods=('GET', 'POST'))
def index():
    with app.app_context():
        db.create_all()
    projects = Project.query.all()
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        project = Project(title=title,
                          description=description)
        db.session.add(project)
        db.session.commit()
        return redirect('/')
    return render_template('index.html',projects=projects)