#!/usr/bin/python
     
import rospy
import actionlib
from control_msgs.msg import GripperCommandGoal, GripperCommandActionResult, GripperCommandAction
     
rospy.init_node('gripper_control')
     
    # Create an action client
client = actionlib.SimpleActionClient('/gazebo_gripper/gripper_cmd', GripperCommandAction)
        
    # Wait until the action server has been started and is listening for goals
client.wait_for_server()
print("Found server")     
    # Create a goal to send (to the action server)
goal = GripperCommandGoal()
goal.command.position = 0.3   # From 0.0 to 0.8
goal.command.max_effort = 10.0  # Do not limit the effort
print(goal)
print("Created goal message")
client.send_goal(goal)

client.wait_for_result()
print(client.get_result())
