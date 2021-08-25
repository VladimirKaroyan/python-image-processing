# importing required libraries
import matplotlib.pyplot as plt
import matplotlib.image as img

blur_ratio = 30


def get_arr_sum(arr):
    summary = 0
    for index in range(0, len(arr)):
        summary = summary + arr[index]
    return summary


def get_ratio(x):
    x_mid = []
    for radioIndex in range(0, len(x)):
        x_mid.append(get_arr_sum(x[radioIndex]) / len(x[radioIndex]))
    return get_arr_sum(x_mid) / len(x_mid)


# reading the image
testImage = img.imread('image_library/image.png')

print(f'Image dimensions are: width - {len(testImage)}px, height - {len(testImage[0])}px')
for heightIndex in range(blur_ratio, len(testImage) - blur_ratio):
    for widthIndex in range(blur_ratio, len(testImage[heightIndex]) - blur_ratio):
        value_list = []
        for ratio in range(1, blur_ratio):
            value_list = value_list + [
                testImage[heightIndex - 1][widthIndex - ratio],
                testImage[heightIndex - 1][widthIndex],
                testImage[heightIndex - 1][widthIndex + ratio],
                testImage[heightIndex][widthIndex - ratio],
                testImage[heightIndex][widthIndex],
                testImage[heightIndex][widthIndex + ratio],
                testImage[heightIndex + 1][widthIndex - ratio],
                testImage[heightIndex + 1][widthIndex],
                testImage[heightIndex + 1][widthIndex + ratio]
            ]
        value = get_ratio(value_list)
        testImage[heightIndex][widthIndex] = [value, value, value]

# displaying the image
plt.imshow(testImage)
plt.show()
