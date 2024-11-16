# example_nodes
This is a ROS package with examples
example_nodes/
├── CMakeLists.txt
├── package.xml
├── README.md
├── nodes/
│ ├── node_example.py
└── src/
│ ├── pub_example.py
│ ├── sub_example.py


## Package Components
1. CMakeLists.txt: Used by CMake to configure package building. Contains instructions for compiling the package, dependencies, and message/service generation if any.
2. package.xml: Describes the package and its dependencies. Contains information such as package name, version, maintainer, and required dependencies.
3. nodes/: Contains ROS nodes (Python scripts) that are part of the package.
4. src/: Contains source code and implementation files.
5. srv/: Contains the custom services
6. msg/: Contains the custom msg

## Usage
To use these example packages:

1. Build the workspace
 cd ~/catkin_ws
 catkin_make

2. Source the setup file
 source devel/setup.bash

3. Run nodes
 rosrun example_nodes node_example.py
 rosrun robot_info pub_example.py
 rosrun robot_info sub_example.py

This package serves as a basic example of ROS package structure and naming conventions, demonstrating how to organize nodes and follow ROS best practices.

## ROS Naming Conventions
1. Package Names:
 - Use lowercase letters
 - Can include underscores
 - Must be unique in the ROS ecosystem
 - Example: example_nodes, robot_info
2. Node Names:
 - Use lowercase letters
 - Can include underscores
 - Should be descriptive of their function
 - Example: node_example.py, pub_example.py
3. Topic Names:
 - Use lowercase letters
 - Can include underscores
 - Should describe the data being transmitted
 - Example: example_topic
4. Service Names:
 - Use Uppercase letters for the first letter
 - Can include underscores
 - Should describe the data being transmitted
 - Example: Example_service