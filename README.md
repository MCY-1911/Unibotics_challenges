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

## 📂 Repository Structure
.
├── P_controller.py # Proportional controller
├── PD_controller.py # Proportional-Derivative controller
├── PID_controller.py # Proportional-Integral-Derivative controller
└── README.md


---

## 🏁 Performance Comparison

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

## Authors

This project is developed by:

- **[Alejandro Díaz Rivero](https://github.com/MCY-1911)**

---



