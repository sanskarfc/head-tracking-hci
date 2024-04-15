# Head Control Interface for VR Accessibility

## Introduction

The Head Control Interface (HCI) for VR Accessibility is a software project aimed at improving accessibility for individuals with disabilities, particularly in virtual reality (VR) environments. This project utilizes head tracking and facial gesture recognition to provide an intuitive interface for controlling VR applications, aiding communication, and enhancing experiences in social, professional, and academic settings.

## Features

- **Head Tracking**: Utilizes a webcam and the dlib library to track the user's head movements in real-time.
- **Facial Gesture Recognition**: Detects facial gestures such as blinks and nods to perform actions such as mouse clicks.
- **Mouse Control**: Allows the user to control the mouse cursor using head movements and trigger mouse clicks with facial gestures.
- **Nod Detection**: Recognizes nodding gestures to simulate left mouse clicks, enhancing the usability of the interface.
- **VR Accessibility**: Designed specifically for VR applications, enabling individuals with disabilities to interact with virtual environments effectively.
- **Customizable**: Parameters such as blink detection thresholds and cooldown periods can be adjusted to suit individual preferences and needs.

## Getting Started

### Prerequisites

- Python 3.x
- OpenCV
- dlib
- pyautogui
- scipy

### Installation

1. Clone the repository:

```bash
git clone https://github.com/sanskarfc/head_tracking_hci.git
