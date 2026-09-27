# ROS2 Command Notes


## Workspace

Create workspace:

```bash
mkdir -p ~/ros2_ws/src

Build:
colcon build

Source environment:
source install/setup.bash

Package
Create package:
ros2 pkg create package_name --build-type ament_python

List packages:
ros2 pkg list

Node
Run node:
ros2 run package_name executable_name

List nodes:
ros2 node list

Node information:
ros2 node info node_name

Topic
List topics:
ros2 topic list

Echo topic:
ros2 topic echo /topic_name
