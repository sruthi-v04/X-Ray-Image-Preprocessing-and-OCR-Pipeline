import os
import json
from paddleocr import PaddleOCR

ocr_engine = PaddleOCR(
    det_model_dir="ocr_models/ch_PP-OCRv4_det_infer",
    rec_model_dir="ocr_models/ch_PP-OCRv4_rec_infer",
    cls_model_dir="ocr_models/ch_ppocr_mobile_v2.0_cls_infer",
    rec_char_dict_path="ocr_models/ppocr_keys_v1.txt",
    use_angle_cls=True,
    lang="en",
    det_db_box_thresh=0.4,
    drop_score=0.3
)

input_dir = r"C:\Users\sruth\Desktop\xrayimagespreprocess"
output_dir = r"C:\Users\sruth\Desktop\pppppppp"


if not os.path.exists(output_dir):
    os.mkdir(output_dir)

json_f_list = []

for imagefileinfo in os.listdir(input_dir):
    if imagefileinfo.endswith(('.png', '.jpeg','.jpg')):
        try:
            print("Processing image:", imagefileinfo)
            imagepath = os.path.join(input_dir, imagefileinfo)
            
            ocr_result = ocr_engine.ocr(imagepath, cls=True)

            bounded_texts = []
            for line in ocr_result[0]:
                bbox = line[0]
                text = line[1][0]
                score = line[1][1]
                bounded_texts.append({
                    "bbox": bbox,
                    "text": text,
                    "score": score,
                    "x1": bbox[0][0],
                    "y1": bbox[0][1],
                    "xend": bbox[2][0],
                    "yend": bbox[2][1]
                })

            obj = []
            for bounded_text in bounded_texts:
                bboxes = {
                    "x1": bounded_text["x1"],
                    "y1": bounded_text["y1"],
                    "xend": bounded_text["xend"],
                    "yend": bounded_text["yend"]
                }
                relativecoordinates = {
                    "center_x": (bounded_text["x1"] + bounded_text["xend"]) / 2 / 1280,  # Assuming image width is 1280
                    "center_y": (bounded_text["yend"] + bounded_text["y1"]) / 2 / 720,  # Assuming image height is 720
                    "width": (bounded_text["xend"] - bounded_text["x1"]) / 1280,  # Assuming image width is 1280
                    "height": (bounded_text["yend"] - bounded_text["y1"]) / 720  # Assuming image height is 720
                }
                object_ = {
                    "class_id": bounded_text["text"],
                    "confidence": bounded_text["score"],
                    "name": "name",
                    "relative_coordinate": relativecoordinates
                }
                obj.append(object_)

            json_ = {
                "filename": imagefileinfo,
                "frame_id": 0,
                "object": obj,
                "bounded_texts": bounded_texts
            }
            json_f_list.append(json_)

        except Exception as e:
            print(f"Error processing image file {imagefileinfo}: {str(e)}")

json_obj = json.dumps(json_f_list, indent=3)
with open("Xray.json", "w") as outfile:
    outfile.write(json_obj)





