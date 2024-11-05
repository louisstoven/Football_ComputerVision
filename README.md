# Football Analysis System with Computer Vision

## Overview
This repository contains a Football Analysis System developed using machine learning, computer vision, and deep learning techniques. The project utilizes YOLO, a state-of-the-art object detection model, to detect players, referees, and footballs during matches. It also implements tracking algorithms to follow these objects across frames and enhance the analysis.

The system includes custom training of an object detector to improve detection accuracy, pixel segmentation using KMeans to assign players to teams based on their shirt colors, and optical flow methods to measure camera movement. By applying perspective transformations, the system accurately quantifies player movements in meters, enabling the calculation of speed and distance covered during the game.

This project is suitable for both beginners and experienced machine learning engineers and addresses various concepts in sports analytics.

## Project Goals
The main objectives of this project are to:

Implement an object detection system for real-time football match analysis.
Utilize tracking techniques to monitor player and ball movements across video frames.
Train a custom YOLO model to enhance detection performance on specific datasets.
Segment players from the background using KMeans clustering based on shirt colors.
Measure player movement accurately using optical flow and perspective transformations.
Calculate players' speed and distance covered on the field.

## Learning Resources
YouTube Tutorial: Football Analysis System Tutorial - This video provided essential concepts and techniques for building the football analysis system. (https://www.youtube.com/watch?app=desktop&v=neBZ6huolkg)

## Technologies Used
YOLOv8: For real-time object detection of players, referees, and footballs.
Ultralytics: For using and fine-tuning YOLO models.
OpenCV (cv2): For video processing, optical flow analysis, and perspective transformations.
KMeans: For pixel segmentation and clustering to accurately identify team colors.
NumPy: For numerical operations and data manipulation.
Matplotlib: For visualizing analysis results.

## Datasets
Kaggle Dataset (Note: Video links were removed from Kaggle)
Alternative Video Link
Roboflow Football Dataset

## Getting Started
To run the Football Analysis System locally, follow these steps:

## Prerequisites
Ensure you have the following installed:

Python 3.x
PyTorch (follow installation instructions from the official website)
OpenCV
NumPy
Matplotlib
