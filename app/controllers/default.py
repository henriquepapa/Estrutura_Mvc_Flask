from app import app

@app.route("/")
def index():
    return "Oi eu sou o Papa!"
