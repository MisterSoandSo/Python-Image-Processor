import pytesseract
import pyscreenshot as ImageGrab
from pynput import mouse
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

click = True
x1 = 0
y1 = 0

def get_Words_from_Image(a,b,c,d):
    im = ImageGrab.grab(bbox=(a,b,c,d))
    print(pytesseract.image_to_string(im))

def store_Words_from_Image(a,b,c,d):
    im = ImageGrab.grab(bbox=(a,b,c,d))
    return pytesseract.image_to_string(im).split('\n')

def get_pos():
    def on_click(x, y, button, pressed):
        global click, x1, y1
        if pressed:
            if click:
                print('Mouse clicked at ({0}, {1})'.format(x, y))
                x1,y1 = x,y 
                click = False
            else:
                print('Mouse clicked at ({0}, {1})'.format(x, y))
                temp = store_Words_from_Image(x1,y1,x,y)
                print(temp[0])
                return False
    with mouse.Listener(on_click=on_click) as ls:
        ls.join()

if __name__ == '__main__':
    get_pos()
 
