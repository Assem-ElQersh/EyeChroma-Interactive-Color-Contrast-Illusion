import cv2
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider

# Load a grayscale face image
img = cv2.imread('face.jpg', cv2.IMREAD_GRAYSCALE)
height, width = img.shape

# Create RGB version (still grayscale values)
rgb_img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)

# Create mask for the left half
mask = np.zeros((height, width), dtype=np.uint8)
mask[:, :width//2] = 1

# Create function to apply colored overlay with transparency
def apply_overlay(image, color, alpha, mask):
    # Create colored overlay with the same shape as the input image
    overlay = np.ones_like(image, dtype=np.uint8)
    overlay[:, :, 0] = color[0] * 255  # B
    overlay[:, :, 1] = color[1] * 255  # G
    overlay[:, :, 2] = color[2] * 255  # R
    
    # Apply mask and blend with transparency
    result = image.copy()
    masked_region = (mask > 0)
    
    # Convert masked regions to correct format for blending
    img_masked = image[masked_region].astype(np.uint8)
    overlay_masked = overlay[masked_region].astype(np.uint8)
    
    # Blend the images
    blended = cv2.addWeighted(img_masked, 1-alpha, overlay_masked, alpha, 0)
    
    # Put the blended result back into the original image
    result_flat = result.reshape(-1, 3)
    masked_indices = np.where(mask.flatten() > 0)[0]
    result_flat[masked_indices] = blended
    result = result_flat.reshape(image.shape)
    
    # Create a hole in the mask around the eye
    eye_x, eye_y = 265.0, 236.5
    eye_radius = 15
    
    y, x = np.ogrid[:height, :width]
    eye_mask = (x - eye_x)**2 + (y - eye_y)**2 <= eye_radius**2
    
    # Restore original eye pixels
    result[eye_mask] = image[eye_mask]
    
    return result

# Create the interactive figure
fig, ax = plt.subplots(figsize=(10, 8))
plt.subplots_adjust(bottom=0.25)

# Set initial values
initial_color = [1, 0, 0]  # Red
initial_alpha = 0.3  # 30% opacity

# Apply initial overlay
result_img = apply_overlay(rgb_img, initial_color, initial_alpha, mask)
img_display = ax.imshow(result_img)

# Create slider for transparency
ax_alpha = plt.axes([0.25, 0.1, 0.65, 0.03])
alpha_slider = Slider(ax_alpha, 'Transparency', 0, 1, valinit=initial_alpha)

# Update function for slider
def update(val):
    alpha = alpha_slider.val
    result_img = apply_overlay(rgb_img, initial_color, alpha, mask)
    img_display.set_data(result_img)
    fig.canvas.draw_idle()

alpha_slider.on_changed(update)

plt.show()