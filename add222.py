from main import db, Mushroom, MushroomImage
from sqlalchemy.orm import query, join
from sqlalchemy import join
from PIL import Image
from IPython.display import display
from sqlalchemy.orm import joinedload
import io


# svampar = [
#     Mushroom(name="kantarell", color="green", size="small", shape="circle"),
#     Mushroom(name="flugsvamp", color="red", size="big", shape="square"),
#     Mushroom(name="champinjon ", color="blue", size="small", shape="triangle"),
#     Mushroom(name="Mushroom 4", color="blue", size="big", shape="triangle"),
#     Mushroom(name="Mushroom 5", color="green", size="medium", shape="square"),
#     Mushroom(name="Svamp 6", color="purple", size="small", shape="circle"),
#     Mushroom(name="Svamp 7", color="red", size="medium", shape="square"),
#     Mushroom(name="Svamp 8", color="yellow", size="big", shape="circle"),
# ]
# db.session.add_all(svampar)
# db.session.commit()


def convertToBinaryData(filename):
    with open(filename, "rb") as file:
        blobData = file.read()
    return blobData


img1 = r"C:\Users\Magnus\Desktop\images\m1.jpg"
img2 = r"C:\Users\Magnus\Desktop\images\m2.jpg"
img3 = r"C:\Users\Magnus\Desktop\images\m3.jpg"
img4 = r"C:\Users\Magnus\Desktop\images\m4.jpg"


image_data1 = convertToBinaryData(img1)
image_data2 = convertToBinaryData(img2)
image_data3 = convertToBinaryData(img3)
image_data4 = convertToBinaryData(img4)


images = [
    MushroomImage(image=image_data1, mushroom_id="kantarell"),
    MushroomImage(image=image_data2, mushroom_id="flugsvamp"),
    MushroomImage(image=image_data3, mushroom_id="champinjon"),
    MushroomImage(image=image_data4, mushroom_id="kantarell"),
]
# # Add the Mushroom objects to the database
db.session.add_all(images)
db.session.commit()
