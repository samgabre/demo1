from flask import Flask

app=Flask(__name__)

@app.route("/home")
def home():
  return "welcome"

@app.route("/coffee")
def coffee():
  return "coffee"

if __name__=="__main__:
  app.run()
