import random
import sys
from game import constants
from game.action import Action
from game.point import Point

class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        bricks = cast["brick"] # there's only one
        paddle = cast["paddle"][0] # there's only one
        ball = cast["ball"] [0]
        
        
        ball_v = ball.get_velocity()
        paddle_xy = paddle.get_position()
        ball_xy = ball.get_position()
        ball_vx = Point.get_x(ball_v) 
        ball_vy = Point.get_y(ball_v)
        
        if Point.get_y(ball_xy) == 1:
            position = Point(ball_vx, 1)
            ball.set_velocity(position)
        
        if Point.get_x(ball_xy) == 1:
            position = Point(1, ball_vy)
            ball.set_velocity(position)

        if Point.get_x(ball_xy) == 79:
            position = Point(-1, ball_vy)
            ball.set_velocity(position)

        paddle_x = Point.get_x(paddle_xy)
        paddle_y = Point.get_y(paddle_xy)
        ball_x = Point.get_x(ball_xy)
        ball_y = Point.get_y(ball_xy)

        if ball_y == 19:
            print("you suck")
            sys.exit()

        for _ in range(1, 11):

            if paddle_x == ball_x and paddle_y -1 == ball_y:
                position = Point(ball_vx, -1)
                ball.set_velocity(position)
            paddle_x += 1
            
            
           

            # ball.get_position()  (ball.get_velocity())

            # Velocity is based off of an x,y endpoint. 0 indicates that it isn't going left, right, up or down
            # x = -1 is left 1 is right
            # y = -1 is up 1 is down
            # (1, 1) = right and down
            # (1, -1) = right and up
            # (-1, -1) = left and up
            # (-1, 1) = left and down

            # 
            # three types of colisions:
            #   1. ball with paddel
            #   2. ball with brick
            #   3. ball with sides of terminal
        
        
        # for brick in bricks:
        #     if paddel.get_position().equals(ball.get_position()):
        #        pass
                # description = artifact.get_description()
                # marquee.set_text(description) 
