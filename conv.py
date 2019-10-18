import numpy as np
import matplotlib.pyplot as plt

def apply_conv(input_img_path, filter):
    img = plt.imread(input_img_path)
    filter_size = filter.shape[0]
    pad_width = (filter_size-1)//2
    if len(img.shape)==3:
      filter_3D = np.stack((filter, filter, filter), axis=2)
      temp = np.pad(img, ((pad_width, pad_width), (pad_width, pad_width), (0, 0)), mode='constant', constant_values=0)
      temp = np.array([[np.sum(np.multiply(temp[i:i+filter_size, j:j+filter_size, :], filter_3D)) for j in range(temp.shape[1]-filter_size+1)] for i in range(temp.shape[0]-filter_size+1)])
    else:
      temp = np.pad(img, ((pad_width, pad_width), (pad_width, pad_width)), mode='constant', constant_values=0)
      temp = np.array([[np.sum(np.multiply(temp[i:i+filter_size, j:j+filter_size], filter)) for j in range(temp.shape[1]-filter_size+1)] for i in range(temp.shape[0]-filter_size+1)])
      
    temp[temp>255] = 255
    temp[temp<0] = 0
    return temp

def main():
    file_path = input("Enter the file path to which you want to apply conv :")
    filter = input("Enter filter by creating filter without channel in list form :")
    filter = np.array(filte)
    out = apply_conv(file_path, filter)
    plt.imshow(out, cmap='gray')

if __name__ == "__main__":
    main()