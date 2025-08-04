"""
The template of the main script of the machine learning process
"""
from random import seed,randint
import math

class MLPlay:
    def __init__(self):
        """
        Constructor
        """
        self.ball_served = False
        self.current_ball_x = 0
        self.current_ball_y = 0
        self.des_x = 100
        self.last_ball_x = 0
        self.last_ball_y = 0
        self.start_frame = 0
        seed()
        self.rnd_val = randint(0,1)
        self.level4 = False

    def update(self, scene_info):

        """
        Generate the command according to the received scene_info.
        """
        # Make the caller to invoke reset() for the next round.
        if (scene_info["status"] == "GAME_OVER" or
            scene_info["status"] == "GAME_PASS"):
            return "RESET"

        if not self.ball_served:
            for (i,j) in scene_info['bricks']:
                if j > 250:
                    self.level4 = True
                    if self.rnd_val == 1:
                        while scene_info['platform'][0] + 20 < 160 and scene_info['platform'][0] + 20 > 40:
                            command = "MOVE_RIGHT"
                            return command
                    else:
                        while scene_info['platform'][0] +20  < 160 and scene_info['platform'][0] + 20 > 40:
                            command = "MOVE_LEFT"
                            return command

            self.ball_served = True
            self.start_frame = scene_info["frame"]
            if self.rnd_val == 1:
                command = "SERVE_TO_LEFT"
            else:
                command = "SERVE_TO_RIGHT"
        else:
            
            if scene_info["frame"]==self.start_frame or scene_info["frame"]==self.start_frame + 1:
                self.current_ball_x=scene_info["ball"][0]
                self.current_ball_y=scene_info["ball"][1]
                self.des_x = 80
            else:
                self.last_ball_x = self.current_ball_x
                self.last_ball_y = self.current_ball_y
                self.current_ball_x=scene_info["ball"][0]
                self.current_ball_y=scene_info["ball"][1]
                # ball go down
                if self.current_ball_y>self.last_ball_y:
                    # ball go right
                    if self.current_ball_x>self.last_ball_x:
                        if self.level4 == True:
                            self.des_x = (450-self.current_ball_y)+self.current_ball_x
                        else:
                            self.des_x=(400-self.current_ball_y)+self.current_ball_x
                    # ball go left	
                    else:
                        if self.level4 == True:
                            self.des_x = self.current_ball_x-(450-self.current_ball_y)
                        else:
                            self.des_x=self.current_ball_x-(400-self.current_ball_y)
                # ball go up
                if self.current_ball_y<self.last_ball_y:
                        self.des_x=80
                
                #record current position for next update
                self.last_ball_x = scene_info["ball"][0]
                self.last_ball_y = scene_info["ball"][1]

            while self.des_x>200 or self.des_x<0:
                if self.des_x>200:
                    self.des_x=(200-(self.des_x-200))
                else:
                    self.des_x=-self.des_x

            extra_rng = randint(-15,15)
            self.des_x = self.des_x + extra_rng
            if self.des_x<scene_info["platform"][0]+20:
                command = "MOVE_LEFT"
            elif self.des_x>scene_info["platform"][0]+20:
                command = "MOVE_RIGHT"
            else:
                command = "NONE"	
		    
        return command

    def reset(self):
        """
        Reset the status
        """
        self.ball_served = False
