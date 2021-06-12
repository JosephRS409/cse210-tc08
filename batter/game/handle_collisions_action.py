
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
        score = cast["score"] [0]
        lives = cast["lives"] [0]
        
        ball_v = ball.get_velocity()
        paddle_xy = paddle.get_position()
        ball_xy = ball.get_position()
        ball_vx = Point.get_x(ball_v) 
        ball_vy = Point.get_y(ball_v)
        
        if Point.get_y(ball_xy) == 1:
            position = Point(ball_vx, 1)
            ball.set_velocity(position)
        
        if Point.get_x(ball_xy) <= 2:
            position = Point(1, ball_vy)
            ball.set_velocity(position)

        if Point.get_x(ball_xy) >= 78:
            position = Point(-1, ball_vy)
            ball.set_velocity(position)

        paddle_x = Point.get_x(paddle_xy)
        paddle_y = Point.get_y(paddle_xy)
        ball_x = Point.get_x(ball_xy)
        ball_y = Point.get_y(ball_xy)

        if ball_y == 18 and lives._lives == 0:
            print("""
                ██╗░░░██╗░█████╗░██╗░░░██╗  ██╗░░░░░░█████╗░░██████╗███████╗  ██╗░░██╗
                ╚██╗░██╔╝██╔══██╗██║░░░██║  ██║░░░░░██╔══██╗██╔════╝██╔════╝  ╚═╝░██╔╝
                ░╚████╔╝░██║░░██║██║░░░██║  ██║░░░░░██║░░██║╚█████╗░█████╗░░  ░░░██╔╝░
                ░░╚██╔╝░░██║░░██║██║░░░██║  ██║░░░░░██║░░██║░╚═══██╗██╔══╝░░  ░░░╚██╗░
                ░░░██║░░░╚█████╔╝╚██████╔╝  ███████╗╚█████╔╝██████╔╝███████╗  ██╗░╚██╗
                ░░░╚═╝░░░░╚════╝░░╚═════╝░  ╚══════╝░╚════╝░╚═════╝░╚══════╝  ╚═╝░░╚═╝""")
            sys.exit()
        elif ball_y == 19 and lives._lives > 0:
            position = Point(ball_vx, -1)
            ball.set_velocity(position)
            lives._lives -= 1
            lives.set_text(f"Lives: {lives._lives}")

        for _ in range(1, 11):

            if paddle_x == ball_x and paddle_y -1 == ball_y or ball_vx == 3:
                if ball_vx == 1 or ball_vx == 2:
                    ball_vx = random.randint(1,2)
                elif ball_vx == -1 or ball_vx == -2 or ball_vx == -3:
                    ball_vx = random.randint(-2,-1)
                position = Point(ball_vx, -1)
                ball.set_velocity(position)
            paddle_x += 1
            
        i = 0

        for brick in bricks:
            position = brick.get_position()
            brick_x = Point.get_x(position)
            brick_y = Point.get_y(position)

            if brick_x  == ball_x and brick_y == ball_y:
                bricks.pop(i)
                score._points +=1
                score.set_text(f"Score: {score._points}")
                if ball_vy == 1:
                    ball_vy = -1
                elif ball_vy == -1:
                    ball_vy = 1

                if ball_vx == 1:
                    ball_velocity = Point(-1, ball_vy)
                else:
                    ball_velocity = Point(1, ball_vy)
                ball.set_velocity(ball_velocity)

            i += 1
