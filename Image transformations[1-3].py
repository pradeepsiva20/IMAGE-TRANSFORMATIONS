import numpy as np
import cv2
import matplotlib.pyplot as plt

# i) Image Translation
input_img = cv2.imread("color image of flower.jpg")
input_img = cv2.cvtColor(input_img, cv2.COLOR_BGR2RGB)
plt.axis('off')
plt.imshow(input_img)
plt.show()

rows, cols, dim = input_img.shape

# Translation matrix (shifting the image by 20 pixels right and 50 pixels down)
M = np.float32([[1, 0, 20],
                [0, 1, 50],
                [0, 0, 1]])
translated_img = cv2.warpPerspective(input_img, M, (cols, rows))

plt.axis('off')
plt.imshow(translated_img)
plt.show()

# ii) Image Scaling
scaled_img = cv2.warpPerspective(input_img, M, (cols, rows))
plt.axis('off')
plt.imshow(scaled_img)
plt.show()

# iii) Image Shearing
M_x = np.float32([[1, 0.2, 0],
                  [0, 1, 0],
                  [0, 0, 1]])
M_y = np.float32([[1, 0, 0],
                  [0.2, 1, 0],
                  [0, 0, 1]])

# Shearing on x-axis
sheared_img_xaxis = cv2.warpPerspective(input_img, M_x, (cols, rows))

# Shearing on y-axis
sheared_img_yaxis = cv2.warpPerspective(input_img, M_y, (cols, rows))

# Displaying sheared images
plt.axis('off')
plt.imshow(sheared_img_xaxis)
plt.show()

plt.axis('off')
plt.imshow(sheared_img_yaxis)
plt.show()
