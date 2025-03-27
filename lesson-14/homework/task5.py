import numpy as np
from PIL import Image

image_path = "images/birds.jpg"
image = Image.open(image_path)
image_array = np.array(image)

def flip_image(img_arr):
    """Flips the image horizontally and vertically."""
    return np.flipud(np.fliplr(img_arr))

def add_noise(img_array):
    """Adds random noise to the image."""
    noise = np.random.randint(0, 50, img_array.shape, dtype=np.uint8)  # Random noise (0-50)
    noisy_image = img_array + noise  # Add noise
    return np.clip(noisy_image, 0, 255)  # Ensure pixel values are in range

def brighten_channels(img_array, channel=0, value=40):
    """Brightens a specific color channel (default: red) by a fixed value."""
    img_copy = img_array.copy()
    img_copy[:, :, channel] = np.clip(img_copy[:, :, channel] + value, 0, 255)
    return img_copy

def apply_mask(img_array, mask_size=(100, 100)):
    """Applies a black mask at the center of the image."""
    h, w, _ = img_array.shape
    y_start = (h - mask_size[0]) // 2
    x_start = (w - mask_size[1]) // 2
    img_copy = img_array.copy()
    img_copy[y_start:y_start+mask_size[0], x_start:x_start+mask_size[1]] = [0, 0, 0]
    return img_copy

if __name__ == "__main__":
    # Apply transformations
    flipped_image = flip_image(image_array)
    noisy_image = add_noise(image_array)
    brightened_image = brighten_channels(image_array, channel=0, value=40)
    masked_image = apply_mask(image_array, mask_size=(100, 100))

    # Save modified images using PIL
    Image.fromarray(flipped_image).save("output_flipped.jpg")
    Image.fromarray(noisy_image).save("output_noisy.jpg")
    Image.fromarray(brightened_image).save("output_brightened.jpg")
    Image.fromarray(masked_image).save("output_masked.jpg")

    print("Image transformations completed and saved.")