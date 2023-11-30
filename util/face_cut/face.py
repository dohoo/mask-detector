import os
import cvlib as cv
import cv2
from PIL import Image

num = 0

def face_cut(file_path : str, output_path : str):
    img_cv = cv2.imread(file_path)
    img = Image.open(file_path)

    faces, confidences = cv.detect_face(img_cv)

    if len(faces) > 1:
        for idx in range(len(faces)):
            print(faces[idx])
            x, y, x2, y2 = faces[idx]
            cropped_img = img.crop((x, y, x+100, y+100))
            cropped_img.save(output_path + str(num) + ".png", "PNG")

    else:
        for x, y, x2, y2 in faces:
            cropped_img = img.crop((x, y, x+100, y+100))
            cropped_img.save(output_path + str(num) + ".png", "PNG")

if __name__ == "__main__":
    # file_path_input = input("file_path_input : ")
    # file_path_output = input("file_path_output : ")
    file_path_input = "C:/Users/dohoo/Desktop/mask-detector/data/image/result_no_mask/"
    file_path_output = "C:/Users/dohoo/Desktop/mask-detector/data/image/cut_result_no/"

    for file in os.listdir(file_path_input):
        num += 1
        face_cut(file_path_input + file, file_path_output)
        print(num)