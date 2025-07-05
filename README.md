# 🔍 Defect Detection in Manufacturing Using Computer Vision and Deep Learning

This repository contains the code, models, and documentation for my **Industry Internship Project** completed at **Proglint's Software Solutions** as part of the **Industry Internship Programme (IIP) - XXI 700** in Semester VI of the **B.Tech in Computer Science and Engineering (AIML)** 

---

## 📌 Project Overview

This project focuses on building a real-time defect detection system in manufacturing using an ensemble of **YOLOv8, CNN, and EfficientNet**. It aims to improve defect detection accuracy by combining localization and classification models in a modular and scalable pipeline.

### 🔧 Defects Detected:
- Dent  
- Scratch  
- Corner Defect  
- Spidol Mark

The system also classifies defects by **severity level**: Minor, Moderate, Severe.

---

## 📸 Sample Output

<p align="center">
  <img src="visualizations/sample_output.png" width="600" alt="Sample Visualization">
</p>

🟥 Severe | 🟨 Moderate | 🟩 Minor — Color-coded bounding boxes from ensemble output

---

## 🎯 Objectives

- Build a real-time, automated defect detection pipeline.
- Use ensemble modeling to reduce false positives/negatives.
- Perform classification with severity categorization.
- Enable scalable deployment in smart manufacturing environments.
- Train and test using a custom industrial dataset.

---

## 🛠️ Technology Stack

| Component        | Tool/Library        |
|------------------|---------------------|
| Object Detection | YOLOv8 (Ultralytics)|
| Classification   | CNN (Keras), EfficientNet |
| Visualization    | Matplotlib, OpenCV  |
| Language         | Python              |
| IDE              | Jupyter Notebook    |
| Deployment       | Streamlit (Optional) |

---

## 🧪 Methodology

### Pipeline Architecture:

1. **Detection** → YOLOv8 detects ROIs.
2. **Classification** → CNN and EfficientNet classify the cropped ROI.
3. **Fusion** → Weighted averaging based on model confidence.
4. **Severity Scoring** → Minor (0.0–0.5), Moderate (0.5–0.8), Severe (0.8–1.0).
5. **Visualization** → Color-coded bounding boxes.

---

---

## 🧠 Model Architectures

### YOLOv8
- Real-time detection with bounding boxes and segmentation
- mAP@0.5: **96.58%**

### CNN (Custom)
- 3 Conv + Dense layers (lightweight)
- Accuracy: **74%**

### EfficientNet (B0)
- Transfer learning, deep representation
- Accuracy: **86%**

### Ensemble Fusion
- **Weighted Average** of predictions:
  - YOLOv8: 96.6%
  - CNN: 74%
  - EfficientNet: 86%

---

## 📊 Model Results Summary

| Model        | Training | Validation | Testing |
|--------------|----------|------------|---------|
| YOLOv8       | 98.2%    | 96.9%      | 96.6%   |
| CNN          | 82.0%    | 75.0%      | 74.0%   |
| EfficientNet | 90.5%    | 87.2%      | 86.0%   |

✅ Ensemble gives improved classification accuracy and robustness.

---



