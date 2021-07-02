from flask import Flask
from flask import make_response
app=flask(__name__)
@app.route("/")
def setcookies():
    response=make_response("Cookie Inserted")
    response.set_cookie('course','web_pentesting')
    return response
if __name__=="_main__":
    app.run(debug=True)