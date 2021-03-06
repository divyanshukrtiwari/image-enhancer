import argparse
import time
import cv2
import os

ap = argparse.ArgumentParser()
ap.add_argument("-m","--model",required=True,help="../models/EDSR_x4.pb")
ap.add_argument("-i","--image",required=True,help="../images/img1.jpg")
args = vars(ap.parse_args())

modelName = args["model"].split(os.path.sep)[-1].split("_")[0].lower()
modelScale = args["model"].split("_x")[-1]
modelScale = int(modelScale[:modelScale.find(".")])

print("[INFO] loading super resolution model: {}".format(args["model"]))
print("[INFO] model name: {}".format(modelName))
print("[INFO] model scale: {}".format(modelScale))
sr = cv2.dnn_superres.DnnSuperResImpl_create()
sr.readModel(args["model"])
sr.setModel(modelName, modelScale)

image = cv2.imread(args["image"])
print("[INFO] w: {}, h: {}".format(image.shape[1], image.shape[0]))
start = time.time()
upscaled = sr.upsample(image)
end = time.time()
print("[INFO] super resolution took {:.6f} seconds".format(end - start))
print("[INFO] w: {}, h: {}".format(upscaled.shape[1],upscaled.shape[0]))

cv2.imshow("Original", image)
cv2.imshow("Super Resolution", upscaled)
cv2.waitKey(0)