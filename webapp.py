# Entry point for the application.
from . import app    # For application discovery by the 'flask' command.
from . import views  # For import side-effects of setting up routes.
from flask_session import Session

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)