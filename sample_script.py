from cgi import print_arguments
from locale import normalize
from turtle import width
import requests
import base64
import cv2
import os
import json


url = "http://127.0.0.1:5544/extract_text"

filepath = r"C:\Users\sruth\Desktop\rawCR_flash"
outputpath = r"C:\Users\sruth\Desktop\xrayimagespreprocess"

if(not(os.path.exists(outputpath))):
    os.mkdir(outputpath)
cnt = 0
json_f_list = []
for imagefileinfo in os.listdir(filepath):
    try:
        print("processing image ",imagefileinfo)
        cnt +=1
        imagepath = os.path.join(filepath, imagefileinfo)
        outputimagepath = os.path.join(outputpath, imagefileinfo)
        # imagepath = imagepath

        with open(imagepath, "rb") as img:
            image_b64 = base64.b64encode(img.read()).decode()

        res = requests.post(url=url, data={"image": image_b64})
        print("bimread")
        im = cv2.imread(imagepath)
        print("Image read done")
        obj = []
        result_json = res.json()
        for i in result_json:
            x1 = int(i["bbox"][0][0])
            y1 = int(i["bbox"][0][1])
            xend = int(i["bbox"][2][0])
            yend = int(i["bbox"][3][1])
            width  = int(i["bbox"][2][0] - i["bbox"][0][0])
            height = int(i["bbox"][3][1] - i["bbox"][0][1])
            centerx = x1 + (width/2)
            centery = y1 + (height/2)
            normalizeX = centerx/im.shape[1]
            normalizeY = centery/im.shape[0]
            normalizeWidth = width/im.shape[1]
            normalizeHeight = height/im.shape[0]

            x = (x1,y1)
            y = (xend,yend)
            cv2.rectangle(im, x, y, (0, 0, 255), 3)
            relativecoordinates = {
                "center_x" : normalizeX,
                "center_y" : normalizeY,
                "width" : normalizeWidth,
                "height" : normalizeHeight
            }
            object_ = {
                "class_id" : i["text"],
                "confidence" : i["score"],
                "name" : "name",
                "relative_coordinate" : relativecoordinates
            }
            obj.append(object_)
        json_ = {
            "filename" : imagefileinfo,
            "frame_id" : cnt,
            "object" : obj
        }
        json_f_list.append(json_)
        # print()
        cv2.imwrite(outputimagepath, im)
        # print(imagefileinfo ," : ",result_json)
        # print()
        # print(imagefileinfo.filename)
    except:
        print("imagefileinfo",imagefileinfo)
json_obj =  json.dumps(json_f_list,indent=3)
with open("canny.json", "w") as outfile:
    outfile.write(json_obj)

# import json
 
# # Data to be written
# dictionary = {
#     "name": "sathiyajith",
#     "rollno": 56,
#     "cgpa": 8.6,
#     "phonenumber": "9976770500"
# }
 
# # Serializing json
# json_object = json.dumps(dictionary, indent=4)
 
# # Writing to sample.json
# with open("sample.json", "w") as outfile:
#     outfile.write(json_object)

# # add image file path here
# imagepath = "E:/todaywork/images/3-RadNoAD2054_Y12654_W12345_SMAW_Thk14mm_SFD16inch_Exp6sec.png"
# im = cv2.imread(imagepath)
# with open(imagepath, "rb") as img:
#     image_b64 = base64.b64encode(img.read()).decode()

# res = requests.post(url=url, data={"image": image_b64})
# result_json = res.json()
# for i in result_json:
#     x1 = int(i["bbox"][0][0])
#     y1 = int(i["bbox"][0][1])
#     xend = int(i["bbox"][2][0])
#     yend = int(i["bbox"][3][1])
#     x = (x1,y1)
#     y = (xend,yend)
#     cv2.rectangle(im, x, y, (0, 0, 255), 1)

# cv2.imwrite("E:/todaywork/images/3-RadNoAD2054_Y12654_W12345_SMAW_Thk14mm_SFD16inch_Exp6sec_marked.png", im)