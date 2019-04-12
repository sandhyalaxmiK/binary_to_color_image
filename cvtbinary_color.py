import cv2
import numpy as np
import sys,os
palette=[[155, 65, 195], [244, 25, 164], [49, 53, 89], [42, 185, 54], [49, 163, 190], [243, 244, 195], [136, 224, 167], [47, 142, 28], [181, 75, 68], [168, 35, 187], [143, 163, 177], [204, 211, 228], [53, 79, 187], [5, 8, 175], [121, 189, 16], [244, 133, 199], [154, 170, 38], [0, 220, 48], [185, 72, 36], [234, 239, 204], [182, 77, 74], [41, 229, 19], [109, 125, 19], [45, 38, 149], [74, 160, 124], [235, 148, 30], [246, 127, 167], [194, 54, 86], [19, 186, 198], [91, 148, 78], [165, 223, 68], [180, 228, 152], [235, 188, 219], [220, 88, 138], [189, 158, 6]]
palette1=[[131, 63, 167], [82, 149, 224], [30, 102, 88], [64, 9, 20], [81, 150, 178], [233, 105, 128], [138, 127, 207], [94, 12, 87], [171, 33, 27], [130, 243, 69], [97, 122, 117], [75, 132, 14], [205, 90, 240], [119, 155, 101], [18, 123, 224], [53, 244, 71], [181, 23, 47], [197, 232, 35], [109, 23, 197], [237, 67, 215], [19, 192, 117], [54, 78, 247], [24, 241, 171], [117, 110, 64], [38, 49, 25], [238, 95, 43], [67, 192, 190], [140, 142, 234], [9, 118, 116], [55, 199, 202], [108, 126, 112], [90, 212, 140], [62, 60, 24], [86, 66, 26], [248, 54, 9]]

#for i in range(35):
#	palette.append(np.array(np.random.random_integers(0,255,3),dtype=np.uint8))
nums=[np.array([i,i,i]) for i in range(35)]
imgdir=sys.argv[1]
if not os.path.exists(sys.argv[2]):
	os.mkdir(sys.argv[2])
count=1
for inp in os.listdir(imgdir):
	print "processing {}: {} ".format(count,inp)
	img=cv2.imread(imgdir+'/'+inp)
	img1=img.copy()
	for i in range(img1.shape[0]):
		for j in range(img1.shape[1]):
			if img1[i][j][0]!=0:
				np.copyto(img1[i][j],np.array(palette[img1[i][j][0]],dtype=np.uint8),casting='same_kind',where=True)
	
	cv2.imwrite(sys.argv[2]+'/'+inp,img1)
	count+=1



