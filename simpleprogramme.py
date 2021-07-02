from flask import Flask
from flask import make_response
app=Flask(__name__)
@app.route("/")
def setcookies():
    response=make_response("Cookie Inserted")
    response.set_cookie('course','web_pentesting')
    return response
if __name__=="_main__":
    app.run(debug=True)
