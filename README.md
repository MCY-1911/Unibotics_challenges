# Unibotics Challenges

This repository contains solutions and results for the various robotics challenges provided by **Unibotics**. The main focus so far is the **line-following autonomous driving challenge**, implemented using different control strategies in Python. The scripts run directly in the browser by connecting to a Docker simulation environment. For more detailed instrucctions you can consult this slides.

---

## Challenge: Line-Following Robot

The goal of this challenge is to control a robot so that it follows a line on the ground using its camera and velocity commands.  
Three control strategies have been implemented:

### Proportional Control (P)
Uses only the proportional term of the error.  
- Simple and fast to implement  
- Responds directly to line-position error  
- May oscillate or fail in sharp turns  

### Proportional–Derivative Control (PD)
Adds a derivative term to reduce oscillations.  
- Smoother and more stable than P  
- Reduces overshoot  
- Works better in narrow or curved tracks  

### Proportional–Integral–Derivative Control (PID)
Adds an integral term for accumulated error.  
- Eliminates steady-state errors  
- Useful for long curves or persistent drifts  
- Requires careful tuning to avoid instability  

The repository currently includes one Python script for each control strategy.

---

## Running Instructions

1. **Start the Docker image**  
   Launch the Unibotics-provided Docker container that includes the robot simulation environment.

2. **Open the challenge in Unibotics**  
   Go to the Unibotics platform and open the *Line-Following Challenge*.

3. **Connect Docker image and simulator**  
   Use the “connect” option in the platform to link your browser session with the running Docker container.

4. **Download a script from this repository**  
   Choose one of the controller scripts (P, PD, PID) and load it into the Unibotics interface.

5. **Execute the script**  
   Run the file to start the robot’s autonomous behaviour.

6. **Observe the results**  
   Monitor the robot’s performance and analyze how each controller behaves.

---

## Repository Structure
```
.
├── P_controller.py        # Proportional controller
├── PD_controller.py       # Proportional-Derivative controller
├── PID_controller.py      # Proportional-Integral-Derivative controller
└── README.md
```
---

## Performance Comparison

Below is a table to record the execution times obtained by each team member for every control strategy:

| Pilot             | Time (P) | Time (PD) | Time (PID) |
|-------------------|----------|-----------|------------|
| Abel Anang        |          |           |            |
| Rodrigo Aquije    |          |           |            |
| Erik Artigas      |          |           |            |
| Ángela Ausina     | 120.56   | 112.08    | 109.07     |
| Alejandro Díaz    | 107.43   | 87        |            |
| Jose Georgescu    | 84       | 78        | 78.36      |
| Javier Herrero    | 124.68   | 131.20    | 125.86     |
| Pau Martinavarro  |          | 90.85     |            |
| Eduard Munteanu   | 88       | 78.06     | 85.97      |
| Inés Pérez        |          | 102.77    | 105.54     |
| Joel Ramos        |          |           |            |
| Oscar Renau       | 94.09    | 87.88     | 136.70     |
| Carlos Rodríguez  | 123.05   | 119.17    | 124.23     |
| Celia Sáenz       | 109.96   | 96.67     | 126.41     |
| Ayush Sagar       |          |           |            |
| Diego Solsona     | 106.66   | 100       | 99.55      |
| Gaston Tognola    | 119.10   | 98        | 100.85     |

---

## Results & Conclusions

The collected times clearly show how each control strategy behaves under the same circuit conditions:

- **P Control** performs the worst overall. While it reacts quickly, it tends to oscillate, especially in curves, causing longer run times.
- **PD Control** delivers the best performance for most pilots. The derivative term stabilizes the robot’s trajectory and minimizes oscillations, making it the most efficient controller for this circuit.
- **PID Control** should theoretically outperform PD by eliminating residual error, but in this specific track it slightly **worsens performance**.  
  This is because the circuit layout contains frequent direction changes and short straights, which cause the **integral term** to accumulate error unnecessarily, leading to overshoot and reduced stability.

**Conclusion:**  
*PD is the most effective controller for this challenge.*  
*PID shows good performance, but its integral component becomes counterproductive due to the circuit’s geometry.*  
*P is functional but significantly less stable and less competitive than PD or PID.*

---

## Challenge: Rescue Drone – Archimedean Spiral Search & Face Detection

### Challenge Description

The objective of this challenge is to design an **autonomous rescue drone** capable of searching a predefined area to **locate human survivors** using onboard vision.  
The drone must take off, reach a target search zone, systematically explore the area following an **Archimedean spiral trajectory**, detect human faces using a computer vision algorithm, and finally return to the base once the mission is completed.

---

### Mission Overview

The rescue mission is divided into the following phases:

1. Takeoff and altitude stabilization  
2. Navigation to the search area  
3. Spiral-based area exploration  
4. Face detection and survivor localization  
5. Return to base and landing  

---

### Navigation & Control

#### Takeoff and Altitude Control

The drone takes off to a fixed altitude of **3 meters** and maintains it using vertical error correction:

```python
err_z = height - z
HAL.set_cmd_vel(15, -15, err_z, 0)
```

This guarantees stable flight during navigation and scanning.

---

#### Navigation to the Search Area

Before starting the spiral search, the drone moves to a predefined braking zone and then centers itself at the search origin point.

- **Braking point:** `(x_frenada, y_frenada)`
- **Search center:** `(x_objetivo, y_objetivo)`

The braking point is used to reduce velocity and stabilize the drone before switching to precise position control.  
Once stabilized, the drone navigates accurately to the search center coordinates.

Position control ensures correct alignment before initiating the spiral search pattern.

---

#### Takeoff and Altitude Control

The drone takes off to a fixed altitude of **3 meters** and maintains it using continuous vertical error correction.

The altitude error is computed as the difference between the desired height and the current altitude, and is applied as vertical velocity correction.

This guarantees stable flight during navigation and perception tasks.

---
### Perception System

The drone is equipped with a ventral camera used to detect human survivors during the search mission.

All perception tasks are performed in real time using onboard image processing techniques.

Human detection is performed using **Haar Cascade classifiers** provided by OpenCV.

This algorithm is lightweight and fast, making it suitable for real-time face detection in simulation environments.

The ventral camera image is converted to grayscale before applying the detection algorithm.

---

#### Image Rotation for Robust Detection

To increase detection robustness, the ventral camera image is rotated through multiple angles:

0°, 45°, 90°, 135°, 180°, 225°, 270°, 315°, 360°

For each rotation:
- The image is transformed
- Converted to grayscale
- Analysed for face detection

This approach compensates for different face orientations on the ground.

---

### Survivor Localization Logic

When a face is detected, the drone stores its current (x, y) position as a survivor location.

To avoid duplicate detections, a minimum distance threshold of **3 meters** is enforced between detected survivors.

Only detections sufficiently far from existing ones are registered.  
All survivor locations are stored in a set to ensure uniqueness.

---

### Return to Base

Once the spiral search is completed, the drone navigates back to the home position `(0, 0)`.

During the return:
- Altitude is maintained at 3 meters
- Position control ensures safe navigation

After reaching the home position, the drone executes a controlled landing sequence.

----
### Results & Discussion

- The Archimedean spiral provides efficient and systematic area coverage.
- Image rotation improves face detection reliability.
- Distance-based filtering prevents duplicate survivor detections.
- Haar Cascade detection performs well in controlled simulation conditions.
- 
---
### Conclusions

This challenge demonstrates a complete autonomous rescue system combining navigation, control, perception, and decision-making.

The implemented solution successfully detects survivors while ensuring full area coverage and safe mission execution.

## Authors

This project is developed by:

- **[Alejandro Díaz Rivero](https://github.com/MCY-1911)**

---



