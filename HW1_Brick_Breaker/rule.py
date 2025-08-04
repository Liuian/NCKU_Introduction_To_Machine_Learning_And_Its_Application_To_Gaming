"""
The template of the main script of the machine learning process
"""
from random import seed,randint
import math
import time

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

    def update(self, scene_info):

        """
        Generate the command according to the received scene_info.
        """
        #print(scene_info)
        # Make the caller to invoke reset() for the next round.
        if (scene_info["status"] == "GAME_OVER" or
            scene_info["status"] == "GAME_PASS"):
            return "RESET"

        if not self.ball_served:
            self.ball_served = True
            self.start_frame = scene_info["frame"]
            seed()
            rnd_val = randint(0,1)
            if rnd_val == 1:
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
                    #ball's x_velo == 7 or -7
                #if self.current_ball_x - self.last_ball_x == 7 or self.current_ball_x - self.current_ball_x == -7:
                    # ball go right
                    if self.current_ball_x>self.last_ball_x:
                        self.des_x=(400-self.current_ball_y)+self.current_ball_x
                    # ball go left	
                    else:
                        self.des_x=self.current_ball_x-(400-self.current_ball_y)
                    #ball's x_velo == 10 or -10
                    """
                    else:
                        # ball go right
                        if self.current_ball_x>self.last_ball_x:
                            self.des_x = self.current_ball_x +((400 - self.current_ball_y) * 10 / 7)
                        # ball go left
                        else:
                            self.des_x=self.current_ball_x - ((400-self.current_ball_y) * 10 / 7)
                    """
                # ball go up
                else:
                    self.des_x=80
                
                #record current position for next update
                self.last_ball_x = scene_info["ball"][0]
                self.last_ball_y = scene_info["ball"][1]
            
            #修正預測落點
            while self.des_x>200 or self.des_x<0:
                if self.des_x>200:
                    self.des_x=(200-(self.des_x-200))
                else:
                    self.des_x=-self.des_x
            #落點不定

            seed()
            extra_range = randint(-10,10)
            self.des_x = self.des_x + extra_range
            #command
            if self.des_x<scene_info["platform"][0]+20:
                command = "MOVE_LEFT"
            elif self.des_x>scene_info["platform"][0]+20:
                command = "MOVE_RIGHT"
            else:
                command = "NONE"	
        
        #time.sleep(0.5)   
        return command

    def reset(self):
        """
        Reset the status
        """
        self.ball_served = False
