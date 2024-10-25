#!/bin/sh

/opt/labelme_yolo_utils/predetect_yolo2labelme.py --input=./photos2/out/ --model=/opt/yolo/exp/weights/best.onnx --classes=/mnt/Data/graffiti/kgd/class_names.txt --threshold=0.2 --imgsz 1920 1088

