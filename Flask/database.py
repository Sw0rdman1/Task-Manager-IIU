from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

# Define the Task model here
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    done = db.Column(db.Boolean, nullable=False, default=False)

    def __repr__(self):
        return '<Task %r>' % self.title

def init_app(app):
    db.init_app(app)
    migrate.init_app(app, db)

def create_task(title, description="", done=False):
    task = Task(title=title, description=description, done=done)
    db.session.add(task)
    db.session.commit()
    return task

def get_all_tasks():
    tasks = Task.query.all()
    return tasks

def get_task_by_id(id):
    task = Task.query.get_or_404(id)
    return task

def update_task(task, done):
    print(task,done)
    task.done = done
    db.session.commit()
    return task

def delete_task(task):
    db.session.delete(task)
    db.session.commit()
    tasks = Task.query.all()
    return tasks
