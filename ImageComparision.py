import webbrowser
import pyautogui
import time
import cv2

time.sleep(3)


def open_portal():
    url = "https://stackoverflow.com/questions/70354134/open-website-in-python-with-url-parameters"
    browser = webbrowser.get()
    browser.open(url, new=0, autoraise=True)
    time.sleep(3)

def main():
    pyautogui.FAILSAFE = True
    # pyautogui.PAUSE = 1
    # pyautogui.size()
    image_name = "img.png"
    open_portal()
    try:
        # img_found = pyautogui.locateOnScreen(image_name,confidence=0.6,grayscale=False)
        x,y = pyautogui.center(pyautogui.locateOnScreen(image_name,confidence=0.6,grayscale=False))
        time.sleep(2)

        if x:
            print(x,y," image found")
            pyautogui.moveTo(x,y)
            pyautogui.click(x, y)
        else:
            print("not found")
    except Exception as e:
        print(e)


if __name__=="__main__":
    main()
    print('done')