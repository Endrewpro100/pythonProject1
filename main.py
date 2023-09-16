import cv2
from PIL import Image

image_cat="cat.jpeg"
cat=Image.open(image_cat)
image_glasses="glasses.png"
glasses=Image.open(image_glasses)
cat=cat.convert("RGBA")
glasses=glasses.convert("RGBA")
cat_cascade=cv2.CascadeClassifier("haarcascade_frontalcatface_extended.xml")
img=cv2.imread(image_cat)
cat_face=cat_cascade.detectMultiScale(img)
print(cat_face)

for (x, y, w, h) in cat_face:
    glasses=glasses.resize((w, int(h/3)))
    cat.paste(glasses, (x, int(y+h/4)), glasses)

cat.save("kit.png")
kit=cv2.imread("kit.png")
cv2.imshow("cat", kit)
cv2.waitKey(0)