# importing required libraries
import matplotlib.pyplot as plt
import matplotlib.image as img

blur_ratio = 2
black_color_code = 0
white_color_code = 255


def get_arr_sum(arr):
    summary = 0
    for index in range(0, len(arr)):
        summary = summary + arr[index]
    return summary


def get_ratio(x):
    x_mid = []
    for radioIndex in x:
        x_mid_sum = get_arr_sum(radioIndex) / len(radioIndex)
        x_mid.append(x_mid_sum)
    return get_arr_sum(x_mid) / len(x_mid)


# reading the image
testImage = img.imread('image_library/image.png')
new_image = []

print(f'Image dimensions are: width - {len(testImage)}px, height - {len(testImage[0])}px')
for heightIndex in range(blur_ratio, len(testImage) - blur_ratio):
    m = []
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
        mid_value = get_ratio(value_list)
        orig_value = get_arr_sum(testImage[heightIndex][widthIndex]) / len(testImage[heightIndex][widthIndex])
        diff = orig_value - mid_value
        color_code = white_color_code
        if diff > 0.0078:
            color_code = black_color_code
        print(diff, color_code)
        m.append([color_code, color_code, color_code])
    new_image.append(m)

# displaying the image
print(new_image)
plt.imshow(new_image)
plt.show()
