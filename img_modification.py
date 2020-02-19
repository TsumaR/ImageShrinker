import os
import glob
import cv2

MAGNIFICATION = 10

def shrink(m, in_dir, out_dir):
    files = in_dir
    files_file = glob.glob("%s/*" % files)
    for i in files_file:
        img = cv2.imread(i, cv2.IMREAD_COLOR)
        out_img = cv2.resize(img, dsize=None, fx=1/m, fy=1/m, interpolation = cv2.INTER_LINEAR)
        i_base = os.path.basename(i) 
        cv2.imwrite('%s/%s_resize.jpg' % (out_dir, i_base), out_img)
