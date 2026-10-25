# ROS 2 Keyboard Teleop for Turtlesim

A small keyboard teleoperation node: **W/A/S/D** to move, **X** or **Space** to stop, **Q** to quit. Publishes `Twist` on `/turtle1/cmd_vel` and restores the terminal settings on exit.

## Packages

- `keyboard_teleop` (ament_python): `keyboard_teleop`

## Requirements

- Ubuntu 24.04, ROS 2 Jazzy
- `turtlesim` (`sudo apt install ros-jazzy-turtlesim`)

## Build

```bash
cd teleop_ws
source /opt/ros/jazzy/setup.bash
colcon build
source install/setup.bash
```

## Run

Source `install/setup.bash` in every new terminal first.

```bash
# Terminal 1
ros2 run turtlesim turtlesim_node

# Terminal 2 (keep this terminal focused)
ros2 run keyboard_teleop keyboard_teleop
```

## Concepts practised

non-blocking keyboard input (`termios`, `select`), clean shutdown
