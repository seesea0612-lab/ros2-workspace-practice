# ROS2 Workspace Practice

This repository contains a ROS 2 workspace practice project for DASE7503.

The project demonstrates the creation of a ROS 2 package, node execution, workspace management, and GitHub documentation workflow.

---

## Environment

- OS: Ubuntu 24.04.4 LTS
- ROS 2 Distribution: Jazzy Jalisco

---

## Workspace Structure

Workspace path:

```bash
~/ros2_ws
```

Directory structure:

```text
ros2_ws
├── src
│   └── turtle_publisher_py
├── build
├── install
└── log
```

---

## Package Information

Package name:

```text
turtle_publisher_py
```

Node name:

```text
turtle_controller
```

Function:

The node publishes velocity commands (`geometry_msgs/Twist`) to control the turtlesim turtle.

The turtle moves forward and rotates to generate a star-shaped trajectory.

---

## Build Process

### Initial build

The command:

```bash
colcon build
```

was tested first.

The build failed because the ROS tutorial package contained dependency configuration issues:

```text
The generic dependency on 'std_msgs' is redundant with:
exec_depend
```

### Solution

Build only the required package:

```bash
colcon build --packages-select turtle_publisher_py
```

The package was successfully built.

---

## Running the Node

### Terminal 1: Start turtlesim

```bash
source /opt/ros/jazzy/setup.bash

ros2 run turtlesim turtlesim_node
```

### Terminal 2: Run turtle controller

```bash
source /opt/ros/jazzy/setup.bash

source ~/ros2_ws/install/setup.bash

ros2 run turtle_publisher_py turtle_controller
```

---

## Result

The turtle controller runs successfully.

The turtlesim window shows the turtle drawing a star trajectory.

The successful execution screenshot is stored in:

```text
screenshots/success.png
```

---

## GitHub Workflow

Repository management:

```bash
git add .
git commit -m "Update documentation"
git push
```

The project is version-controlled using Git and uploaded to GitHub.
