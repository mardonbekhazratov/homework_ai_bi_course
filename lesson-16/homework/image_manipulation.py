from pathlib import Path
import numpy as np
from PIL import Image


def flip(img_arr):
    return img_arr[::-1,::-1]

def add_random_noise(img_arr):
    mean = 0
    std_dev = 25
    noise = np.random.normal(mean, std_dev, img_arr.shape)

    noisy_image_array = np.clip(img_arr + noise, 0, 255).astype(np.uint8)
    return noisy_image_array

def brighten_channels(img_arr):
    return np.clip(img_arr + 15, 0, 255)

def apply_mask(img_arr):
    height, width, channels = img_arr.shape
    img_arr[height//2-50 : height//2+50, width//2-50 : width//2+50] = [0, 0, 0]
    return img_arr

def save_img(arr, name, mode):
    current_dir = Path(__file__).resolve().parent
    img = Image.fromarray(arr, mode)
    img.save(current_dir / f"images/{name}.jpg")

def main():
    current_dir = Path(__file__).resolve().parent
    with Image.open(current_dir/ "images/birds.jpg") as img:
        img_arr = np.array(img)
    flipped_arr = flip(img_arr)
    save_img(flipped_arr, "flipped", "RGB") # save flipped image
    save_img(add_random_noise(img_arr), "noisy", "RGB") # save noisy image
    save_img(brighten_channels(img_arr), "brightened", "RGB") # save brightened image
    save_img(apply_mask(img_arr), "mask", "RGB") # save mask applied image

if __name__=="__main__":
    main()