import random
from flask import Flask

b = int(input("unique coustomer user id: "))

app = Flask(__name__)


@app.route("/")
def tyre():
    global b
    random.seed(b)
    c = random.randint(1, 30)
    return str(c)


