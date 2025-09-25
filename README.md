# Autonomous Delivery Agent

This project implements an **autonomous delivery agent** that navigates a **2D grid city** to deliver packages while handling static obstacles, varying terrain costs, and dynamic moving obstacles. The agent is designed to be **rational**, choosing actions that maximize delivery efficiency under constraints such as **time** and **fuel**.

---

## Features

* **Environment Modeling**

  * Static obstacles (e.g., buildings, blocked roads)
  * Varying terrain costs (e.g., smooth road = 1, rough terrain = 3, traffic jam = 5)
  * Dynamic obstacles (moving vehicles, pedestrians)
* **Movement**: 4-connected grid (up, down, left, right). Diagonal moves optional (toggle in config).
* **Planning Algorithms**:

  * **Uninformed Search**: BFS, Uniform-Cost Search (UCS)
  * **Informed Search**: A* with admissible heuristic (Manhattan distance / Euclidean distance)
  * **Local Search (Dynamic Replanning)**: Hill-climbing with random restarts, Simulated Annealing
* **Dynamic replanning**: Agent adapts when obstacles appear or traffic costs change.

---

## Requirements

* Python 3.8+
* Required packages:

  ```bash
  pip install -r requirements.txt
  ```

### Dependencies

* `numpy`
* `matplotlib`
* `networkx`
* `tqdm`

---

## Usage

Run the program from the command line:

```bash
python main.py --map maps/medium_map.txt --algo astar
```

### Options

* `--map`: Path to map file (see [Maps](#maps) section).
* `--algo`: Algorithm to run (`bfs`, `ucs`, `astar`, `hill`, `annealing`).
* `--dynamic`: Enable dynamic obstacles for replanning test.
* `--diagonal`: Allow diagonal movement.

---

## Maps

Maps are stored as text files where:

* `S` = Start
* `G` = Goal (delivery location)
* `.` = Free road (cost 1)
* `#` = Static obstacle
* `1-9` = Terrain cost
* `D` = Dynamic obstacle start position

Example (`small_map.txt`):

```
S..2..
.#.##.
..3..G
```

---

## Experiments

The project includes experiments comparing algorithms:

* Path cost
* Nodes expanded
* Execution time

To run all experiments:

```bash
python experiments.py
```

Results will be stored in `results/` with CSV tables and plots.

---

## Deliverables

* **Source Code**: Modular Python code with CLI
* **Maps**: Four test cases (small, medium, large, dynamic)
* **Report**: 6-page analysis with results
* **Demo**: Screenshots or recorded video showing dynamic replanning

---

## Git Workflow

1. Clone repo:

   ```bash
   git clone <repo_url>
   cd autonomous-delivery-agent
   ```
2. Create feature branches for new algorithms.
3. Commit with clear messages.
4. Push and merge via pull requests.

---

## Example Run with Dynamic Replanning

```bash
python main.py --map maps/dynamic_map.txt --algo astar --dynamic
```

Output log:

```
Dynamic obstacle appeared at (3,4). Replanning...
New path found with cost = 18.
```

---

## License

MIT License
