import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/cclab/ROS2_tutorial/install/ros2_python_pkg'
