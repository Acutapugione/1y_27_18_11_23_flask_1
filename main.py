from flask import Flask, render_template, request, redirect, url_for


app = Flask(
    __name__,
    static_folder="frontend/static",
    template_folder="frontend/site",
)


# @app.route("/main", methods=["GET"]) # Bad practice
@app.get("/main/<path:name>/info")
@app.get("/main")
def main(name: str = None):
    print(request.args.get("item"))
    dct = {
        "name": name,
        "numbers": range(100),
    }

    return render_template("index.html", **dct)


@app.get("/register")
def register_page():
    return render_template("register.html", name="Register")


@app.post("/register")
def register():
    nickname = request.form.get("nickname")
    password = request.form.get("password")
    password_repeat = request.form.get("password_repeat")
    assert password == password_repeat
    print(nickname, "->", password)
    return redirect(url_for("main"))


@app.get("/login")
def login_page():
    return render_template("login.html", name="Login")


@app.post("/login")
def login():
    nickname = request.form.get("nickname")
    password = request.form.get("password")
    print(nickname, "->", password)
    return redirect(url_for("main"))


if __name__ == "__main__":
    app.run(
        # host="0.0.0.0",
        # port=4040,
        debug=True,
    )
