from application import app
@app.route("/")
@app.route("/earth")
def  index():
    return "<h1>Hello,Earth!</h1>"