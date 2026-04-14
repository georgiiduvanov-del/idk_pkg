import rclpy
from rclpy.node import Node

class TimerPrinter(Node):
 def __init__(self):
     super().__init__('time_printer')
     self.create_timer(5.0, self.print_time)
 def print_time(self):
     now = self.get_clock().now().nanoseconds / 1e9
     self.get_logger().info(f"Time: {now:.2f} sec")
    
def main():
    rclpy.init()
    node = TimerPrinter()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()
        
if __name__ == '__main__':
    main()
 
