from flask import Flask, render_template, url_for, request, jsonify

app = Flask(__name__,)

#URL => endpoint /
@app.route("/")
def hello_world():
    name = request.args.get("name", default="anonymous")
    subject = request.args.get("subject")

    return render_template("index.html", name=name, subject=subject)

@app.route("/msg")
def hell ():
    data = {
        "message": "welcome to the platform!"
    }
    return jsonify(data), 200

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        name = request.form["username"]
        password = request.form["password"]

        # send it to database & verify
        friends = ["Adam", "Bob", "Charlie", "Dan"]
        header = "<header>ABC Website</header>"


        return render_template("welcome.html", name=name, password= password , friends=friends, header=header)

    else:
        return render_template("login.html")
     

if __name__ == "__main__":
    app.run(debug=True) 

#run
#app.run(debug = True)
