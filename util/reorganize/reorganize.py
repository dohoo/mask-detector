import os
import shutil

input_path = ["C:/Users/dohoo/Desktop/mask-detector/data/image/수집자료/사람 얼굴 1", "C:/Users/dohoo/Desktop/mask-detector/data/image/수집자료/사람 얼굴 2",
              "C:/Users/dohoo/Desktop/mask-detector/data/image/수집자료/사람 얼굴 3", "C:/Users/dohoo/Desktop/mask-detector/data/image/수집자료/사람 얼굴 4"]
output_path = "C:/Users/dohoo/Desktop/mask-detector/data/image/수집자료/result_no_mask"

def reorganize(input_path : list, output_path : str):
    for path in input_path:
        for num, file_name in enumerate(os.listdir(path)):
            shutil.copy(path + "/" + file_name, output_path + "/" + str(num + 1) + ".png")

if __name__ == "__main__":
    # file_num = input("file number : ")
    # input_path = []
    # for i in range(int(file_num)):
    #     path = input("input path ({}) : ".format(i+1))
    #     input_path.append(path)
    # output_path = input("output path : ")
    reorganize(input_path, output_path)