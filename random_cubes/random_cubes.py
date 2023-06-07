import random
import rospy
from visualization_msgs.msg import Marker

rospy.init_node('random_cubes')

marker_pub = rospy.Publisher('visualization_marker', Marker, queue_size=10)

name = "YOUR_NAME" # заменить на своё имя
surname = "YOUR_SURNAME" # заменить на свою фамилию
num_cubes = len(name) + len(surname)

for i in range(num_cubes):
    marker = Marker()
    marker.header.frame_id = "map"
    marker.type = Marker.CUBE
    marker.action = Marker.ADD
    marker.pose.position.x = random.uniform(-5, 5)
    marker.pose.position.y = random.uniform(-5, 5)
    marker.pose.position.z = 0.5
    marker.pose.orientation.x = 0.0
    marker.pose.orientation.y = 0.0
    marker.pose.orientation.z = 0.0
    marker.pose.orientation.w = 1.0
    marker.scale.x = random.uniform(0.1, 0.5)
    marker.scale.y = random.uniform(0.1, 0.5)
    marker.scale.z = random.uniform(0.1, 0.5)
    marker.color.r = random.uniform(0, 1)
    marker.color.g = random.uniform(0, 1)
    marker.color.b = random.uniform(0, 1)
    marker.color.a = 1.0
    marker.lifetime = rospy.Duration()
    marker_pub.publish(marker)

rospy.spin()
