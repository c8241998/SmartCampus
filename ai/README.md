# AI part of our project
This directory will conclude but not limited to `face detection`, `face landmark localization`,`face verification`, `object detection` and `ReID`.

## Schedule
|Task|Finished|
|---|---|
|face detection|`yes`|  
|face landmark localization|`yes`|
|face verification|`yes`|
|object detection| `yes`|
|ReID|`no`|

## Prerequisites
```
Pillow==5.1.0
face-recognition==1.2.3
face-recognition-models==0.3.0
dlib==19.17.0
numpy==1.14.3
torch==1.0.0
torchvision==0.2.1
```
Other version of the above package may work but not guaranteed.

## Notes
Detection requires freezed data model, which is available in [yolo website](https://pjreddie.com/darknet/yolo/).
The model is about 300M, so it is not concluded in this repo.

This repo supports fully functioning detection api, you can get in `det` directory and view the markdown file for instructions.

## Demo
Be advised two demo videos has been uploaded.