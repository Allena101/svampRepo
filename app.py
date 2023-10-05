from io import BytesIO
import base64
from flask import Flask, render_template, request, send_file
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db_222.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Upload(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(50))
    data = db.Column(db.LargeBinary)


# class Mushroom(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), unique=True)
#     color = db.Column(db.String(50))
#     size = db.Column(db.Integer)
#     shape = db.Column(db.Integer)
#     image = db.relationship("MushroomImage", backref="mushroom", lazy=True)


class MushroomImage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.LargeBinary)
    mushroom_id = db.Column(db.Integer, db.ForeignKey("mushroom.name"))


class Mushroom(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    color = db.Column(db.String(50))
    size = db.Column(db.String(50))
    shape = db.Column(db.String(50))
    image = db.relationship("MushroomImage", backref="mushroom", lazy=True)


# Create info class that holds more general text info in a few text fields
# figure out how to link it
# class MushroomInfo(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), unique=True)
#     color = db.Column(db.String(50))
#     size = db.Column(db.String(50))
#     shape = db.Column(db.String(50))
#     image = db.relationship("MushroomImage", backref="mushroom", lazy=True)


with app.app_context():
    db.create_all()


#! green , big
@app.route("/", methods=["GET", "POST"])
def index():
    image_data_list = []
    name = None
    form_submitted = True

    if request.method == "POST":
        # form_submitted = True
        # color = request.form["color"]
        # color = request.form["color"]
        color = request.form.get("color")
        size = request.form.get("size")
        shape = request.form.get("shape")
        # print(color)
        print(color)
        print(size)
        print(shape)

        # svamp =  Mushroom(pizza_id=new_pizza.id, name=i)
        # mushrooms = Mushroom.query.filter_by(name=i).all()
        mushrooms = Mushroom.query.filter_by(color=color, size=size, shape=shape).all()
        # name = None
        for i in mushrooms:
            print(i.name)
            name = i.name

        # name = i.name
        images = MushroomImage.query.filter_by(mushroom_id=name).all()
        for i in images:
            print(i.mushroom_id)

        # mushroom_images = db.session.query(mushroomimage).all()
        mushroom_images = MushroomImage.query.filter_by(mushroom_id=name).all()
        image_data_list = []
        for img in mushroom_images:
            print(img.mushroom_id)
            image_data = img.image
            image_data_base64 = base64.b64encode(image_data).decode("utf-8")
            image_data_list.append(image_data_base64)

    print("OJOJ")
    return render_template(
        "index.html", images=image_data_list, name=name, form_submitted=form_submitted
    )


# @app.route("/", methods=["get", "post"])
# def index():
#     if request.method == "post":
#         # ...
#         mushroom_images = db.session.query(mushroomimage).all()
#         image_data_list = []
#         for img in mushroom_images:
#             print(img.mushroom_id)
#             image_data = img.image
#             image_data_base64 = base64.b64encode(image_data).decode('utf-8')
#             image_data_list.append(image_data_base64)
#         return render_template("index.html", images=image_data_list)


# @app.route("/", methods=["GET", "POST"])
# def index():
#     if request.method == "POST":
#         file = request.files["file"]

#         upload = Upload(filename=file.filename, data=file.read())
#         db.session.add(upload)
#         db.session.commit()

#         return f"Uploaded: {file.filename}"
#     return render_template("index.html")


@app.route("/download/<upload_id>")
def download(upload_id):
    upload = Upload.query.filter_by(id=upload_id).first()
    return send_file(
        BytesIO(upload.data), attachment_filename=upload.filename, as_attachment=True
    )


@app.route("/hitta_svamp", methods=["POST"])
def hitta_svamp():
    color = request.form["color"]
    color2 = request.form.get("color")
    print(color)
    print(color2)
    print("OJOJ")
    # your code
    # return a response


# @app.route("/test")
# def test():
#     mushroom_name = "ingen_svamp"
#     return render_template("test.html", mushroom_name=mushroom_name)


@app.route("/test/<mushroom_name>")
def test(mushroom_name):
    return render_template("test.html", mushroom_name=mushroom_name)


if __name__ == "__main__":
    app.run(debug=True)


# @stock.route("/deletePizza", methods=["GET", "POST"])
# def deletePizza():
#     if request.method == "POST":
#         if "delete_pizza" in request.form:
#             pizza_name = request.form["pizzaName"]
#             pizza = Pizza.query.filter_by(name=pizza_name).first()

#             # Could have used cascade but tried implementing it to late which caused issues , but i worked fine to manually delete the pizzaID first from PizzaPrice and PizzaTopping and then finally just delete the record from the Pizza table so
#             pizza_prices_to_delete = PizzaPrice.query.filter_by(pizza=pizza_name).all()
#             for pizza_price in pizza_prices_to_delete:
#                 db.session.delete(pizza_price)

#             pizza_toppings_to_delete = PizzaTopping.query.filter_by(
#                 pizza_id=pizza.id
#             ).all()
#             for pizza_topping in pizza_toppings_to_delete:
#                 db.session.delete(pizza_topping)

#             db.session.delete(pizza)
#             db.session.commit()
#             flash(f"You have deleted {pizza_name} from the store", "success")
#             return redirect(url_for("stock.deletePizza"))

#         elif "delete_topping" in request.form:
#             # I made it so that you can only delete a pizza or a topping at a time.
#             topping_name = request.form["toppingName"]
#             topping = Topping.query.filter_by(name=topping_name).first()
#             db.session.delete(topping)
#             db.session.commit()
#             flash(f"You have deleted {topping_name} from the store", "success")
#             return redirect(url_for("stock.deletePizza"))

#     toppings = Topping.query.all()
#     pizzas = Pizza.query.all()
#     toppingList = []
#     pizzaList = []
#     # These loops are for getting a list of Pizza names and Toppings that can then be populated by the drop down menus (select tag).
#     for pizza in pizzas:
#         pizzaList.append(pizza.name)
#     for topping in toppings:
#         toppingList.append(topping.name)

#     return render_template(
#         "deletePizza.html",
#         toppings=toppings,
#         pizzas=pizzas,
#         pizzaList=pizzaList,
#         toppingList=toppingList,
#         no_sidebar=True,
#     )
