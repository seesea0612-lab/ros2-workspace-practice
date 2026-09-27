# ROS2 Command Notes

Common ROS 2 commands used in this practice.

---

# 1. ROS 2 Environment

Check ROS distribution:

```bash
echo $ROS_DISTRO
```

Source ROS environment:

```bash
source /opt/ros/jazzy/setup.bash
```

Source workspace:

```bash
source ~/ros2_ws/install/setup.bash
```

---

# 2. Workspace Commands

Create workspace:

```bash
mkdir -p ~/ros2_ws/src
```

Enter workspace:

```bash
cd ~/ros2_ws
```

Build workspace:

```bash
colcon build
```

Build selected package:

```bash
colcon build --packages-select package_name
```

Clean build files:

```bash
rm -rf build install log
```

---

# 3. Package Commands

Create Python package:

```bash
ros2 pkg create package_name --build-type ament_python
```

List packages:

```bash
ros2 pkg list
```

Check package:

```bash
ros2 pkg prefix package_name
```

---

# 4. Node Commands

Run node:

```bash
ros2 run package_name node_name
```

List running nodes:

```bash
ros2 node list
```

Node information:

```bash
ros2 node info node_name
```

---

# 5. Topic Commands

List topics:

```bash
ros2 topic list
```

Show topic information:

```bash
ros2 topic info /topic_name
```

Display topic messages:

```bash
ros2 topic echo /topic_name
```

---

# 6. turtlesim Practice Commands

Start turtlesim:

```bash
ros2 run turtlesim turtlesim_node
```

Run turtle controller:

```bash
ros2 run turtle_publisher_py turtle_controller
```

The controller publishes:

```text
/turtle1/cmd_vel
```

using:

```text
geometry_msgs/Twist
```

---

# 7. Git Commands

Initialize repository:

```bash
git init
```

Check status:

```bash
git status
```

Add files:

```bash
git add .
```

Commit:

```bash
git commit -m "message"
```

Push to GitHub:

```bash
git push
```

---

# 8. My First ROS2 Package

## Create Package

```bash
cd ~/ros2_ws/src
ros2 pkg create my_first_package --build-type ament_python
```

## Inspect Package Structure

```bash
cd ~/ros2_ws/src/my_first_package
tree
```

## Create Node File

```bash
cd ~/ros2_ws/src/my_first_package/my_first_package
touch my_node.py
code my_node.py
```

## Configure ROS2 Executable

Edit:

```bash
cd ~/ros2_ws/src/my_first_package
code setup.py
```

The console script entry is:

```text
my_node = my_first_package.my_node:main
```

## Build Package

```bash
cd ~/ros2_ws
colcon build --packages-select my_first_package
```

## Source Workspace

```bash
source /opt/ros/jazzy/setup.bash
source ~/ros2_ws/install/setup.bash
```

## Run Node

```bash
ros2 run my_first_package my_node
```

## Check Running Nodes

In another terminal:

```bash
source /opt/ros/jazzy/setup.bash
source ~/ros2_ws/install/setup.bash
ros2 node list
```

Expected output:

```text
/my_first_node
```

## Check Environment

```bash
printenv ROS_DISTRO
lsb_release -ds
python3 --version
uname -m
ros2 pkg prefix my_first_package
```

Recorded environment:

```text
ROS_DISTRO: jazzy
Ubuntu: 24.04.4 LTS
Python: 3.12.3
Architecture: x86_64
Package prefix: /home/wangcc/ros2_ws/install/my_first_package
```
