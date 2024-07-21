from flask import Flask, render_template, request


app = Flask(
    __name__,
    static_folder="frontend/static",
    template_folder="frontend/site",
)


# @app.route("/main", methods=["GET"]) # Bad practice
@app.get("/main/<path:name>/info")
@app.get("/main")
def main(name: str = None):
    1 / 0
    print(request.args.get("item"))
    dct = {
        "name": name,
    }

    return render_template("index.html", **dct)


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=4040,
        debug=False,
    )
