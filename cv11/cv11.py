import cv2
import numpy as np

for i in range(1, 7):
    img = cv2.imread(f"cv11/Cv11_c0{i}.bmp", cv2.IMREAD_GRAYSCALE)
    dp = 1
    minDist = 1
    param1 = 50
    param2 = 0.89
    minRadius = 2
    maxRadius = 0
    circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT_ALT,
                               dp, minDist,
                               param1=param1, param2=param2,
                               minRadius=minRadius, maxRadius=maxRadius)
    print(circles)

    img_with_count = cv2.cvtColor(img.copy(), cv2.COLOR_GRAY2BGR)
    font = cv2.FONT_HERSHEY_SIMPLEX
    centerOfText = (78, 192)
    fontScale = 5
    fontColor = (0, 255, 0)
    thickness = 5
    lineType = cv2.LINE_AA

    cv2.putText(img_with_count, f"{len(circles[0]) if circles is not None else 0}",
                centerOfText, font, fontScale, fontColor, thickness, lineType)
    
    cv2.imwrite(f"cv11/Cv11_c0{i}_count.bmp", img_with_count)

def encode_decode_markers(path):
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE) / 255
    kernel = np.ones((3, 3), np.uint8)
    h = img.shape[0] // 2
    
    for i, part in enumerate([img[:h, :], img[h:, :]]):
        eroded = part.copy()
        iters = 0
        
        while np.any(eroded):
            temp = cv2.erode(eroded, kernel)
            if not np.any(temp):
                break
            eroded = temp
            iters += 1
            
        coords = np.where(eroded > 0)
        print(f"Feature {i} coordinates:", list(zip(coords[0], coords[1])))
        print(f"Iterations: {iters}\n")
        
        decoded = cv2.dilate(eroded, kernel, iterations=iters)
        cv2.imshow(f"Part {i}", np.vstack([part, eroded, decoded]))
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

encode_decode_markers("cv11/Cv11_merkers.bmp")