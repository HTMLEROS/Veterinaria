from app import app
@app.route('/')
def index():
    return "Bienvenido a VetControl"