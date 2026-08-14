# Zero Robotics Visualizations

Interactive 3D visualizations for the **Zero Robotics Galactic Garden** simulation. The project visualizes robot behavior and program execution in real time, allowing students to see how their code translates into robot movement and game actions.

## Overview

The visualization simulates two robots competing in Galactic Garden:

* **Red robot** — executes a predefined sequence of movement, planting, watering, and harvesting actions.
* **Blue robot** — follows a separate strategy that uses a randomly selected bonus crop.
* **3D simulation** — renders the game environment, robots, plots, watering zone, and astronaut zone using Three.js.
* **Code execution visualization** — highlights the currently executing line of code as each robot performs an action.
* **Game state** — displays the game timer, scores, bonus crops, and winner.
* **Interactive controls** — supports playing, pausing, and stepping through the simulation, as well as rotating and zooming the 3D scene.

## Features

### Program Execution

Each robot has a sequence of actions representing its program. As the simulation runs, the corresponding line of code is highlighted to show the relationship between the program and the robot's behavior.

### 3D Robot Simulation

The environment is rendered using [Three.js](https://threejs.org/), including:

* Red and blue robot models
* Three plots for each team
* Watering zone
* Astronaut zone
* Robot home positions
* Labeled game objects
* Interactive camera controls

### Game Mechanics

The simulation models several Galactic Garden mechanics:

* Planting crops
* Watering crops
* Crop growth wait times
* Harvesting crops
* Bonus crops
* Crop-specific scoring
* Team scoring
* Win detection

The four supported crops are:

| Crop       | Growth Time | Base Score |
| ---------- | ----------- | ---------- |
| Tomato     | 6s          | 6          |
| Cabbage    | 8s          | 7          |
| Strawberry | 5s          | 4          |
| Melon      | 10s         | 11         |

Bonus crops can provide additional points when harvested after being obtained from the astronaut zone.

## Visualization and Physics

Robot movement uses a **spring-damper model** rather than directly interpolating between positions. The simulation applies spring forces, damping, and a small wobble effect as robots approach their targets to create more realistic movement.

```javascript
const k = 0.015;  // spring stiffness
const c = 0.35;   // damping
```

The renderer uses Three.js WebGL rendering along with `OrbitControls` for interactive camera movement and `CSS2DRenderer` for labels.

## Controls

| Control   | Description                           |
| --------- | ------------------------------------- |
| **Play**  | Runs the simulation continuously      |
| **Pause** | Pauses the simulation                 |
| **Step**  | Advances the simulation by one action |
| **Mouse** | Rotate and zoom the 3D scene          |

The simulation also starts automatically when the page loads.

## Technologies

* **JavaScript**
* **HTML/CSS**
* **Three.js**

  * WebGLRenderer
  * OrbitControls
  * CSS2DRenderer
  * GLTFLoader
* **GLTF/GLB** 3D models
* **Python** for local development server

## Running Locally

### Requirements

* Python 3
* A modern web browser

### Start the Server

From the project directory:

```bash
python3 -m http.server 8000
```

Then open:

```text
http://localhost:8000/<roundx>.html
```

The project uses a local HTTP server because the visualization loads external JavaScript libraries and local `.glb` robot models. The HTML loads the `honey.glb` and `bumble2.glb` models at runtime.

## Project Structure

```text
ZR_visualizations/
│
├── zr_viz.html          # Main visualization
├── honey.glb            # Red robot 3D model
├── bumble2.glb          # Blue robot 3D model
└── ...
```

Additional visualization files can be launched using the same local server by replacing `zr_viz.html` with the desired HTML file.

## Project Context

Developed for the **Zero Robotics** program at the MIT Media Lab to help students visualize program execution and understand the relationship between their code and robot behavior.

The visualization was designed to support students working with robot movement, crop mechanics, resource management, and game strategy.

