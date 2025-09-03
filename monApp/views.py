from .app import app
from config import ABOUT
@app.route('/')
def index():
    return "Hello world !"

@app.route("/about")
def about():
    return ABOUT
if __name__ == "__main__":
    app.run()