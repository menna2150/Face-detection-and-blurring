 # **face-anonymizer-python**

Face anonymizer using Python and OpenCV! This project detects faces in images and videos and applies blurring/pixelation effects to protect privacy and anonymize individuals.

![Face Anonymizer Demo](https://github.com/menna2150/Face-detection-and-blurring/blob/main/opencv_face_blurring_example.webp?raw=true)
*Figure 1: Example of face detection and blurring in action*

## 📋 **Table of Contents**
- [Overview](#-overview)
- [Features](#-features)
- [How It Works](#-how-it-works)
- [Technologies Used](#-technologies-used)
- [Installation](#-installation)
- [Usage](#-usage)
  - [Blur Faces in an Image](#1-blur-faces-in-an-image)
  - [Pixelate Faces in an Image](#2-pixelate-faces-in-an-image)
  - [Real-Time Face Anonymization from Webcam](#3-real-time-face-anonymization-from-webcam)
- [Code Explanation](#-code-explanation)
- [Customization Options](#-customization-options)
- [Use Cases](#-use-cases)
- [License](#-license)

## 🔍 **Overview**

In an era where privacy is paramount, this **Face Anonymizer** tool helps protect identities by automatically detecting and obscuring faces in visual media. Whether you're processing photos for public sharing, anonymizing video footage for research, or creating content for social media, this tool provides a simple yet effective solution.

## ✨ **Features**

- ✅ **Face Detection**: Automatically detects faces in images and webcam streams
- ✅ **Multiple Anonymization Methods**:
  - Gaussian Blur (smooth, natural-looking obscuring)
  - Pixelation/Mosaic effect
  - Solid rectangle overlay
- ✅ **Real-Time Processing**: Works with live webcam feed
- ✅ **Adjustable Detection Sensitivity**: Fine-tune face detection parameters
- ✅ **Lightweight**: Minimal dependencies, fast processing

## ⚙️ **How It Works**

1. **Load Input**: Read image or webcam feed
2. **Convert to Grayscale**: Haar Cascade works better with grayscale images
3. **Detect Faces**: Use pre-trained classifier to locate faces
4. **Apply Anonymization**: For each detected face, apply blur/pixelation
5. **Output Result**: Display the anonymized media

## 🛠️ **Technologies Used**

| Technology | Purpose |
|:---|:---|
| **Python 3.x** | Core programming language |
| **OpenCV (cv2)** | Face detection and image processing |
| **Haar Cascade Classifier** | Pre-trained model for face detection |
| **NumPy** | Array operations and image manipulation |

## 📦 **Installation**

### **Prerequisites**
- Python 3.6 or higher installed
- pip (Python package manager)

### **Step 1: Clone the Repository**
```bash
git clone https://github.com/your-username/face-anonymizer-python.git
cd face-anonymizer-python
