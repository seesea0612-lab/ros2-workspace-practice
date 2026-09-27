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

---

# My First ROS2 Package and Node

## Task

Create a ROS2 Python package and run a custom ROS2 node.

Package:

```text
my_first_package
```

Node:

```text
/my_first_node
```

## Environment

```text
ROS 2: Jazzy
Ubuntu: 24.04.4 LTS
Python: 3.12.3
Architecture: x86_64
```

## Source Files

Main node source:

```text
src/my_first_package/my_first_package/my_node.py
```

Package configuration:

```text
src/my_first_package/setup.py
src/my_first_package/package.xml
```

## Create the Package

```bash
cd ~/ros2_ws/src
ros2 pkg create my_first_package --build-type ament_python
```

The package uses `ament_python`, the ROS 2 Python build system.

## Build

Because another existing `turtlesim` package in the workspace currently has a `package.xml` dependency error, only this package was built:

```bash
cd ~/ros2_ws
colcon build --packages-select my_first_package
```

Successful build output:

```text
Starting >>> my_first_package
Finished <<< my_first_package

Summary: 1 package finished
```

## Run

Load the workspace environment:

```bash
source /opt/ros/jazzy/setup.bash
source ~/ros2_ws/install/setup.bash
```

Run the node:

```bash
ros2 run my_first_package my_node
```

Successful output:

```text
[INFO] [...] [my_first_node]: Hello ROS2, my first node!
```

## Verify the Node

In another terminal:

```bash
source /opt/ros/jazzy/setup.bash
source ~/ros2_ws/install/setup.bash
ros2 node list
```

Output:

```text
/my_first_node
```

This confirms that the node is running and registered in the ROS 2 system.

## Problem and Solution

Running:

```bash
colcon build
```

attempted to build every package in the workspace and failed on the existing local `turtlesim` package.

The relevant error was:

```text
The generic dependency on 'std_msgs' is redundant with: exec_depend
```

This error came from:

```text
src/ros_tutorials/turtlesim/package.xml
```

It was unrelated to `my_first_package`.

For this task, the problem was avoided by building only the required package:

```bash
colcon build --packages-select my_first_package
```

`my_first_package` then built and ran successfully.
