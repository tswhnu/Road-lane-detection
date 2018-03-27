# Road-lane-detection
Learning how to use opencv-python to detect the road lane in the photograph or in the video
# 主体思路
首先利用```cv2.GaussianBlur()```函数来对照片进行降噪处理
之后利用```cv2.canny()```函数来对图片进行边缘提取后利用```cv2.HoughLinesP()```来进行直线检测
# 函数解析
```cv2.GaussianBlur(img, kernel_size, sigma)```<br>
'img'为原照片，‘kernel’为高斯矩阵大小，越大越模糊，‘sigma’为方差，前者越大照片越模糊，后者越小照片越模糊
