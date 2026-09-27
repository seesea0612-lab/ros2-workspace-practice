# ROS2 Workspace Practice

## Environment

- Ubuntu
- ROS2 Jazzy


## Workspace

Workspace path:


~/ros2_ws

Structure:


ros2_ws
├── src
├── build
├── install
└── log


## Package

Package:


turtle_publisher_py

Node:


turtle_controller


## Build

The original workspace contains an old turtlesim source package.

Running:

```bash
colcon build

caused an error:
The generic dependency on 'std_msgs' is redundant with:
exec_depend

Solution:
Build only the required package:
colcon build --packages-select turtle_publisher_py

Run
Terminal 1:
source /opt/ros/jazzy/setup.bash
ros2 run turtlesim turtlesim_node

Terminal 2:
source /opt/ros/jazzy/setup.bash
source ~/ros2_ws/install/setup.bash

ros2 run turtle_publisher_py turtle_controller

Result
The turtle controller runs successfully and generates trajectory in turtlesim.
