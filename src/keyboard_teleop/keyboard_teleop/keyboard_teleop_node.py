import sys
import select
import termios
import tty

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class KeyboardTeleop(Node):

    def __init__(self):
        super().__init__('keyboard_teleop')

        self.publisher = self.create_publisher(
            Twist,
            '/turtle1/cmd_vel',
            10
        )

        self.settings = termios.tcgetattr(sys.stdin)
        tty.setcbreak(sys.stdin.fileno())

        self.timer = self.create_timer(
            0.1,
            self.check_keyboard
        )

        self.current_command = Twist()

        self.get_logger().info(
            'Use W/A/S/D to move, X or Space to stop, Q to quit.'
        )

    def check_keyboard(self):
        if select.select([sys.stdin], [], [], 0.0)[0]:
            key = sys.stdin.read(1).lower()

            if key == 'w':
                self.current_command.linear.x = 2.0
                self.current_command.angular.z = 0.0

            elif key == 's':
                self.current_command.linear.x = -2.0
                self.current_command.angular.z = 0.0

            elif key == 'a':
                self.current_command.linear.x = 0.0
                self.current_command.angular.z = 2.0

            elif key == 'd':
                self.current_command.linear.x = 0.0
                self.current_command.angular.z = -2.0

            elif key == 'x' or key == ' ':
                self.current_command = Twist()

            elif key == 'q':
                self.current_command = Twist()
                self.publisher.publish(self.current_command)
                rclpy.shutdown()
                return

        self.publisher.publish(self.current_command)


def main(args=None):
    rclpy.init(args=args)

    node = KeyboardTeleop()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.publisher.publish(Twist())
        termios.tcsetattr(
            sys.stdin,
            termios.TCSADRAIN,
            node.settings
        )
        node.destroy_node()

        if rclpy.ok():
            rclpy.shutdown()


if __name__ == '__main__':
    main()
