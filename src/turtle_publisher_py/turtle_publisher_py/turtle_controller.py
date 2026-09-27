import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class TurtleController(Node):

    def __init__(self):
        super().__init__('turtle_controller')

        self.publisher_ = self.create_publisher(
            Twist,
            '/turtle1/cmd_vel',
            10
        )

        # 每 0.1 秒执行一次控制函数
        self.timer_period = 0.1
        self.timer = self.create_timer(
            self.timer_period,
            self.move_turtle
        )

        # 当前状态：'forward' 或 'turn'
        self.state = 'forward'

        # 已经画了几条边
        self.edge_count = 0

        # 记录当前状态已经执行了多少次
        self.step_count = 0

        # 直走速度
        self.linear_speed = 2.0

        # 转动角速度
        self.angular_speed = 1.0

        # 直走时间，大约 2 秒
        self.forward_steps = 20

        # 转 144°
        # 时间 = 角度 / 角速度
        # 2.513 / 1.0 ≈ 2.5 秒
        self.turn_steps = 25

    def move_turtle(self):

        msg = Twist()

        # 已经画完 5 条边
        if self.edge_count >= 5:
            msg.linear.x = 0.0
            msg.angular.z = 0.0

            self.publisher_.publish(msg)

            self.get_logger().info('Star finished!')

            self.timer.cancel()
            return

        # 直走状态
        if self.state == 'forward':

            msg.linear.x = self.linear_speed
            msg.angular.z = 0.0

            self.step_count += 1

            if self.step_count >= self.forward_steps:
                self.state = 'turn'
                self.step_count = 0

        # 转弯状态
        elif self.state == 'turn':

            msg.linear.x = 0.0
            msg.angular.z = self.angular_speed

            self.step_count += 1

            if self.step_count >= self.turn_steps:
                self.state = 'forward'
                self.step_count = 0
                self.edge_count += 1

        self.publisher_.publish(msg)


def main(args=None):

    rclpy.init(args=args)

    node = TurtleController()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()