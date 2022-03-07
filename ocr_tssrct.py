import cv2
from easyocr import Reader

lang = ['en', 'hi', '']


def read_txt(file_path):
    image = cv2.imread(file_path)
    reader = Reader(lang, gpu=True)
    output = reader.readtext(image)
    output_tt = []
    for tupls in output:
        output_tt.append(tupls[1])
    return output_tt



