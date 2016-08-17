import cv2
import numpy as np
from PIL import Image
import PIL.ImageGrab
#import pytesseract
import scipy.ndimage as sp

class ScreenInterpreter(object):
    def __init__(self):
        """
        Static class, constructor doesn't really
        do anything.
        """
        pass

    def takeScreenshot(self):
        """
        Capture a screenshot of the entire screen

        Returns:
            (Image)
        """

        return PIL.ImageGrab.grab()

    def find_subimages(self, primary, subimage, confidence=0.80):
        """
        Credit:
            https://github.com/johnoneil/subimage (8/16/2016)
        """
        primary_edges = cv2.Canny(primary, 32, 128, apertureSize=3)
        subimage_edges = cv2.Canny(subimage, 32,128, apertureSize=3)

        result = cv2.matchTemplate(primary_edges, subimage_edges, cv2.TM_CCOEFF_NORMED)
        (y, x) = np.unravel_index(result.argmax(),result.shape)

        result[result>=confidence]=1.0
        result[result<confidence]=0.0
        
        ccs = self.get_connected_components(result)
        return self.correct_bounding_boxes(subimage, ccs)  


    def cc_shape(self, component):
        """
        Credit:
            https://github.com/johnoneil/subimage (8/16/2016)
        """
        x = component[1].start
        y = component[0].start
        w = component[1].stop-x
        h = component[0].stop-y
        return (x, y, w, h)

    def correct_bounding_boxes(self, subimage, connected_components):
        """
        Credit:
            https://github.com/johnoneil/subimage (8/16/2016)
        """
        (image_h, image_w)=subimage.shape[:2]
        corrected = []
        for cc in connected_components:
            (x, y, w, h) = self.cc_shape(cc)
            presumed_x = x+w/2
            presumed_y = y+h/2
            corrected.append((slice(presumed_y, presumed_y+image_h), slice(presumed_x, presumed_x+image_w)))
        return corrected

    def get_connected_components(self, image):
        """
        Credit:
            https://github.com/johnoneil/subimage (8/16/2016)
        """
        s = sp.morphology.generate_binary_structure(2,2)
        labels,n = sp.measurements.label(image)#,structure=s)
        objects = sp.measurements.find_objects(labels)
        return objects

    def draw_bounding_boxes(self, img,connected_components,max_size=0,min_size=0,color=(0,0,255),line_size=2):
        """
        Credit:
            https://github.com/johnoneil/subimage (8/16/2016)
        """
        for component in connected_components:
            if min_size > 0 and area_bb(component)**0.5<min_size: continue
            if max_size > 0 and area_bb(component)**0.5>max_size: continue
            (ys,xs)=component[:2]
            cv2.rectangle(img,(xs.start,ys.start),(xs.stop,ys.stop),color,line_size)

class ScrabbleBoggleInterpreter(ScreenInterpreter):
    def __init__(self):
        ScreenInterpreter.__init__(self)

    def locateBoard(self, img):
        ref_pt_1 = cv2.imread("../resources/scrabble-boggle_img/game-area_top-left.png")
        ref_pt_2 = cv2.imread("../resources/scrabble-boggle_img/game-area_bottom-right.png")

        top_left = self.find_subimages(img, ref_pt_1)[0]
        top_left_x = top_left[1]
        top_left_y = top_left[0]

        bottom_right = self.find_subimages(img, ref_pt_2)[0]
        bottom_right_x = bottom_right[1]
        bottom_right_y = bottom_right[0]

sbi = ScrabbleBoggleInterpreter()

img1 = cv2.imread("../resources/scrabble-boggle_img/sample-fullscreen.png")

sbi.locateBoard(img1)