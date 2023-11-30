from selenium import webdriver
from selenium.webdriver.common.by import By
import cvlib as cv
import cv2
import os
# from selenium.common.exceptions import WebDriverException
# from selenium.webdriver.common.keys import Keys

def detect_face_bool(image):
    face, confidence = cv.detect_face(image)
    if len(face) == 0:
        return False
    else:
        return True

def search_selenium(search_name, search_limit) :
    search_url = "https://www.google.com/search?q=" + str(search_name) + "&hl=ko&tbm=isch"

    driver.get(search_url)

    image_count = len(driver.find_elements(By.CSS_SELECTOR, 'img.rg_i.Q4LuWd'))

    print("로드된 이미지 개수 : ", image_count)

    driver.implicitly_wait(2)
    ii = 0
    for i in range(search_limit):
        ii += 1
        try:
            image = driver.find_elements(By.CSS_SELECTOR, 'img.rg_i.Q4LuWd')[i]
            image.screenshot("c:/users/dohoo/desktop/mask-detector/data/image/mask/" + str(i) + ".png")

        except:
            print("이 검색어에서 검색 할 수 있는 이미치 개수는", ii, "개 입니다.")
            break
            
        # except WebDriverException:
        #     # 이미지 로딩중 발생하는 '이미지 더보기' 버튼 클릭
        #     driver.find_element(By.XPATH, '//*[@id="islmp"]/div/div/div/div/div[1]/div[2]/div[2]/input').send_keys(Keys.ENTER)

        # except IndexError:
        #     # '이미지 더보기' 버튼 클릭 
        #     try:               
        #         driver.find_element(By.XPATH, '//*[@id="islmp"]/div/div/div/div/div[2]/span').send_keys(Keys.ENTER)
        #     except:
        #         driver.find_element(By.XPATH, '//*[@id="islmp"]/div/div/div/div/div[1]/div[2]/div[2]/input').send_keys(Keys.ENTER)


if __name__ == "__main__":
    search_name = input("검색하고 싶은 키워드 : ")
    search_limit = int(input("원하는 이미지 수집 개수 : "))
    driver = webdriver.Chrome('c:/users/dohoo/desktop/mask-detector/util/crwal/driver/chromedriver.exe')
    # search_maybe(search_name, search_limit, search_path)
    search_selenium(search_name, search_limit)

    for i in range(len(os.listdir("c:/users/dohoo/desktop/mask-detector/data/image/mask/"))):
        image = cv2.imread("c:/users/dohoo/desktop/mask-detector/data/image/mask/" + str(i) + ".png")
        if not detect_face_bool(image):
            os.remove("c:/users/dohoo/desktop/mask-detector/data/image/mask/" + str(i) + ".png")
            print( i, "번째 이미지는 얼굴이 없어 삭제합니다.")
        else:
            pass

    driver.close()
    print("총 ", len(os.listdir("c:/users/dohoo/desktop/mask-detector/data/image/mask/")), "개의 이미지가 수집되었습니다.")