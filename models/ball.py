from models.ball_type import BallType

class Ball :

    ball_type = None
    ball_number = None

    def __init__(self, ball_type : BallType, ball_number : int) : 
        self.ball_type = ball_type
        self.ball_number = ball_number
        