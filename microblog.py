from app import app, db, mail, cli
from app.models import User, Post


@app.shell_context_processor
def make_shell_context():
    return {"db": db, "User": User, "Post": Post, "mail": mail}
