#!/usr/bin/python

#Example program to demonstrate the use of the GripperCommandAction gripper controller, to be used with the gazebo_ros_control Gazebo plugin
 
import rospy
import actionlib
from control_msgs.msg import GripperCommandGoal, GripperCommandActionResult, GripperCommandAction
     
rospy.init_node('gripper_control')
     
    # Create an action client
    #Be sure to spawn the required controller beforehand, of type positionControllers/GripperActionController
client = actionlib.SimpleActionClient('/gripper_controller/gripper_cmd', GripperCommandAction)
        
    # Wait until the action server has been started and is listening for goals
client.wait_for_server()
print("Found server")     
    # Create a goal to send (to the action server)
goal = GripperCommandGoal()
#Open the gripper
goal.command.position = 0.0   #Completely open
goal.command.max_effort = -1.0  # Do not limit the effort
print(goal)
print("Created gripper open goal message")
client.send_goal(goal)
client.wait_for_result()
print(client.get_result())

#Sleep for 1 second
rospy.sleep(1)

#Close the gripper
goal.command.position = 0.85   #Completely closed
goal.command.max_effort = -1.0  # Do not limit the effort
print(goal)
print("Created gripper open goal message")
client.send_goal(goal)
client.wait_for_result()
print(client.get_result())
