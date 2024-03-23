from flask import Flask as F

app = F(__name__)


@app.route("/")
def home():
  return "Hello"


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
