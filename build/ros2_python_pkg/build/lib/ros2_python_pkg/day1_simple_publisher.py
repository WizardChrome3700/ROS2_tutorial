import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class simplePublisher(Node):
	def __init__(self):
		super().__init__("simple_publisher")
		self.pub = self.create_publisher(String, "chatter", 10)
		self.counter = 0
		self.timer = self.create_timer(1.0, self.timer_callback)

	def timer_callback(self):
		self.get_logger().info(f"publishing at frequency of 1 Hz.")
		msg = String()
		msg.data = f"Hello ROS2 - counter = {self.counter}."
		self.pub.publish(msg)
		self.counter += 1

def main(args=None):
	rclpy.init(args=args)
	publisherNode = simplePublisher()
	rclpy.spin(publisherNode)
	publisherNode.destroy_node()
	rclpy.shutdown()

if __name__ == "__main__":
	main()
