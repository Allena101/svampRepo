from main import db, Mushroom, MushroomImage, Svamp
from sqlalchemy.orm import query, join
from sqlalchemy import join
from PIL import Image
from IPython.display import display
from sqlalchemy.orm import joinedload
import io


# Create 5 Mushroom objects
# mushrooms = [
#     Mushroom(name="kantarell", color="yellow", size=2, shape=1),
#     Mushroom(name="flugsvamp", color="red/white", size=5, shape=2),
#     Mushroom(name="champinjon ", color="vit", size=2, shape=3),
#     Mushroom(name="Mushroom 4", color="Pink", size=2, shape=1),
#     Mushroom(name="Mushroom 5", color="Purple", size=1, shape=2),
# ]
# # Add the Mushroom objects to the database
# db.session.add_all(mushrooms)
# db.session.commit()


svampar = [
    Svamp(name="kantarell", color="green", size="small", shape="circle"),
    Svamp(name="flugsvamp", color="red", size="big", shape="square"),
    Svamp(name="champinjon ", color="blue", size="small", shape="triangle"),
    Svamp(name="Mushroom 4", color="blue", size="big", shape="triangle"),
    Svamp(name="Mushroom 5", color="green", size="medium", shape="square"),
    Svamp(name="Svamp 6", color="purple", size="small", shape="circle"),
    Svamp(name="Svamp 7", color="red", size="medium", shape="square"),
    Svamp(name="Svamp 8", color="yellow", size="big", shape="circle"),
]
# Add the Mushroom objects to the database
db.session.add_all(svampar)
db.session.commit()


print("add_data script has run")


# Get the Mushroom objects you want to associate the images with
# mushrooms = db.session.query(Mushroom).limit(3).all()
# for i in mushrooms:
#     print(i.color)


img1 = r"C:\Users\Magnus\Desktop\images\m1.jpg"
img2 = r"C:\Users\Magnus\Desktop\images\m2.jpg"
img3 = r"C:\Users\Magnus\Desktop\images\m3.jpg"
img4 = r"C:\Users\Magnus\Desktop\images\m4.jpg"


# Function to convert image file to binary data
def convertToBinaryData(filename):
    with open(filename, "rb") as file:
        blobData = file.read()
    return blobData


# Define the SQL query
sql = "INSERT INTO mushroom_image (image, mushroom_fact_id) VALUES (?, ?)"

# Convert the image file to binary data
image_data1 = convertToBinaryData(img1)
image_data2 = convertToBinaryData(img2)
image_data3 = convertToBinaryData(img3)
image_data4 = convertToBinaryData(img4)


# images = [
#     MushroomImage(image=image_data1, mushroom_id=1),
#     MushroomImage(image=image_data2, mushroom_id=1),
#     MushroomImage(image=image_data3, mushroom_id=2),
#     MushroomImage(image=image_data4, mushroom_id=3),
# ]

# # ? Using name as foreign key makes querying easer
# images = [
#     MushroomImage(image=image_data1, mushroom_id="kantarell"),
#     MushroomImage(image=image_data2, mushroom_id="flugsvamp"),
#     MushroomImage(image=image_data3, mushroom_id="champinjon"),
#     MushroomImage(image=image_data4, mushroom_id="kantarell"),
# ]
# # # Add the Mushroom objects to the database
# db.session.add_all(images)
# db.session.commit()


mushrooms = db.session.query(Mushroom).all()

for i in mushrooms:
    print(i.name)
mushrooms = Mushroom.query.options(joinedload(Mushroom.image)).all()


# for mushroom in mushrooms:
#     print("Mushroom:", mushroom.name)
#     for image in mushroom.image:
#         print("Image:", image.id)

import imghdr

# ? to not print all of them (slicing the result)
for mushroom in mushrooms:
    print("Mushroom:", mushroom.name)
    for image in mushroom.image[:1]:
        print("Image:", image.id)
        # img = Image.open(image_buffer)

        # img = Image.open(image)
        # img.show()
        # img.show()


# # Open the image
# image = Image.open('path/to/image.jpg')

# # Display the image
# display(image)


mushroom_images = db.session.query(MushroomImage).all()

for img in mushroom_images:
    print(img.mushroom_id)
    # img = Image.open(image.image, "rb")
    # img.show()
    # image_data = io.BytesIO(img.image)

    # with open(image_data) as img_file:
    #     oj = Image.open(img_file)
    #     oj.show()
    image_data = io.BytesIO(img.image)

    # Open the image using Image.open()
    oj = Image.open(image_data)
    oj.show()


# Create 5 Svamp objects


# svamp = Svamp(name="Min_svamp", color="red", size="big", shape="triangle")
# db.session.add(svamp)
# db.session.commit()
