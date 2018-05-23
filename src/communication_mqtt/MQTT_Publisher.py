# Publisher.py
import paho.mqtt.client as mqtt
import rospy
from std_msgs.msg import *

global remote_control


class publish():
    def __init__(self):
        self.mqttc = mqtt.Client("python_pub")
        self._g_cst_ToMQTTTopicServerIP = "localhost"
        self._g_cst_ToMQTTTopicServerPort = 1883  # port
        self._g_cst_MQTTTopicName = "my_topic"
        rospy.Subscriber('/my_topic', String, self.remote_controller)
    def remote_controller(self, msg):
        self.mqttc.connect(self._g_cst_ToMQTTTopicServerIP, self._g_cst_ToMQTTTopicServerPort)
        try:
            self.mqttc.publish(self._g_cst_MQTTTopicName, msg.data)
        except:
            print("[nc] Exception :" )



if __name__ == '__main__':
    rospy.init_node('elevator_RC', anonymous=False)

    while not rospy.is_shutdown():
        try:
            publish()
        except rospy.ROSInterruptException:
            pass

