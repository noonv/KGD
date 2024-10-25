#!/usr/bin/env python3

'''
resize files from photo

'''

__author__ = 'Vladimir'

import os
import cv2
import glob
import argparse

def main():

    # parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--input", required=True, dest="input", default="./photos2", type=str,
        help="path to directory with images")
    ap.add_argument("-o", "--output", required=True, dest="output", default="./photos2/out", type=str,
        help="path to directory for store results")
    args = vars(ap.parse_args())
    #print(args)

    print("Start...")

    # get files
    files = sorted( glob.glob( os.path.join(args['input'], '*.jpg') ) )
    print("files:", files)

    # create dirs
    dst_images_dir =args['output']
    if not os.path.exists(args['output']):
        os.makedirs(args['output'])

    for filename in files:
        print(filename)
        image = cv2.imread(filename)
        print(image.shape)
        height, width = image.shape[:2]
        print("Image size:", width, height)
        
        # resize image
        width2, height2 = 1440, 1920
        img_r = cv2.resize(image, (width2, height2), interpolation=cv2.INTER_AREA)
        print('Resize size:',  width2, height2)
        res_file_name = os.path.basename(filename)
        dst_res_path = os.path.join(dst_images_dir, res_file_name)
        cv2.imwrite(dst_res_path, img_r)
        #cv2.imshow("res", img_r)
        #if cv2.waitKey(0) & 0xFF == ord('q'):
        #  break
        #break

    print("Done.")

if __name__ == '__main__':
    main()
