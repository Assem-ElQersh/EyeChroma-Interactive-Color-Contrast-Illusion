# EyeChroma: Color Contrast Illusion

## Overview

**EyeChroma** is an interactive demonstration of the **color contrast illusion**, where a neutral gray eye appears to shift in color due to the surrounding hues. This effect highlights how our visual system interprets colors in context, influenced by simultaneous contrast and chromatic adaptation.

![Example](https://github.com/user-attachments/assets/fceba59c-f1f3-4508-a5c5-8f8b233301bd)

## How It Works

In this illusion:
- A **grayscale image** of a face is displayed.
- A **colored overlay** (default: red) is applied to half of the image.
- Both **eyes are identical** in the original image.
- The eye in the **colored region appears blue-green**, even though it remains unchanged.
- A **cutout in the overlay** ensures that no color is directly applied to the eye itself.
- An **interactive slider** allows adjustment of the overlay transparency, altering the illusion's strength.

## The Science Behind It

This effect is explained by two key principles in visual perception:

### 1. Simultaneous Color Contrast
- Colors are perceived in relation to their surroundings.
- When a neutral gray is surrounded by red, it appears shifted toward its complementary color—**blue-green**.

### 2. Chromatic Adaptation
- When exposed to a dominant color (e.g., red), the retina **adapts** by reducing sensitivity to that color.
- When viewing neutral gray afterward, the brain compensates, making it appear as the **opposite hue**.

## Features

- **Interactive slider** to adjust overlay transparency.
- **Precise eye cutout** ensuring the eye remains unaltered.
- **Demonstration of visual perception effects** in real time.

## Requirements

To run the script, install the following dependencies:

- Python 3.x
- OpenCV (`cv2`)
- NumPy
- Matplotlib

Install dependencies via pip:
```bash
pip install opencv-python numpy matplotlib
```

## Usage

Run the script to start the interactive demonstration:
```bash
python eyechroma.py
```

Adjust the transparency slider and observe how the eye color perception changes.

## Notes

- The illusion is **most effective** with red overlays at **30-50% opacity**.
- Works best with an image where the eyes are naturally neutral gray.
- The eye coordinates in the code can be adjusted for different images.

## References & Further Reading
- Kingdom, F. A. A. (2003). *Color contrast and contextual influences on color perception*.
- Ware, C. (2012). *Information Visualization: Perception for Design*.

## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/Assem-ElQersh/EyeChroma-Interactive-Color-Contrast-Illusion/blob/main/LICENSE) file for details.

---

### Contributions
Contributions, suggestions, and improvements are welcome! Feel free to open an issue or submit a pull request.

