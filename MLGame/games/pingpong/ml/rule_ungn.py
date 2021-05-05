"""
The template of the script for the machine learning process in game pingpong
"""

import math
class MLPlay:
    import random
    def __init__(self, side):
        
        """
        Constructor

        @param side A string "1P" or "2P" indicates that the MLPlay is used by
               which side.
        """
        self.ball_served = False
        self.side = side
        self.start_frame = 0
        self.current_ball_x = 0
        self.current_ball_y = 0
        self.last_ball_x = 0
        self.current_ball_y = 0
        self.des_x = 0

    def update(self, scene_info):
        """
        Generate the command according to the received scene information
        """
        if scene_info["status"] != "GAME_ALIVE":
            print(scene_info["ball_speed"])
            return "RESET"

        if not self.ball_served:
            if scene_info["frame"]==149:
                self.ball_served = True
                rand=self.random.randint(0,1)
                if rand==0:
                    return "SERVE_TO_LEFT"
                else:
                    return "SERVE_TO_RIGHT"
        else:
            if self.side == "1P":
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
                            if scene_info["ball_speed"][0]<=12 or scene_info["ball_speed"][1]<=9:
                                if scene_info["ball"][1]<200:
                                    self.des_x=(scene_info["ball_speed"][0]/scene_info["ball_speed"][1])*(420-self.current_ball_y)+self.current_ball_x+3 #
                                else:
                                    self.des_x=(scene_info["ball_speed"][0]/scene_info["ball_speed"][1])*(420-self.current_ball_y)+self.current_ball_x+3 #
                            else:
                                #if scene_info["ball_speed"][0]<=16:
                                    if scene_info["ball"][1]<200:
                                        self.des_x=(scene_info["ball_speed"][0]/scene_info["ball_speed"][1])*(420-self.current_ball_y)+self.current_ball_x+5#
                                    else:
                                        self.des_x=(scene_info["ball_speed"][0]/scene_info["ball_speed"][1])*(420-self.current_ball_y)+self.current_ball_x+5#
                                #else:
                                 #   if scene_info["ball"][1]<200:
                                  #      self.des_x=(scene_info["ball_speed"][0]/scene_info["ball_speed"][1])*(420-self.current_ball_y)+self.current_ball_x+2 #
                                   # else:
                                    #    self.des_x=(scene_info["ball_speed"][0]/scene_info["ball_speed"][1])*(420-self.current_ball_y)+self.current_ball_x+3 #
                    # ball go left 
                    else:
                        if scene_info["ball_speed"][0]<-12 or scene_info["ball_speed"][1]<=9:
                            if scene_info["ball"][1]<200:
                                self.des_x=self.current_ball_x+(-scene_info["ball_speed"][0]/scene_info["ball_speed"][1])*(420-self.current_ball_y)-3 #
                            else:
                                self.des_x=self.current_ball_x+(-scene_info["ball_speed"][0]/scene_info["ball_speed"][1])*(420-self.current_ball_y)-3 #
                        else:
                            #if scene_info["ball_speed"]<=16:
                                if scene_info["ball"][1]<200:
                                    self.des_x=self.current_ball_x+(-scene_info["ball_speed"][0]/scene_info["ball_speed"][1])*(420-self.current_ball_y)-5 #
                                else:
                                    self.des_x=self.current_ball_x+(-scene_info["ball_speed"][0]/scene_info["ball_speed"][1])*(420-self.current_ball_y)-6#
                            #else:
                             #   if scene_info["ball"][1]<200:
                              #      self.des_x=self.current_ball_x+(-scene_info["ball_speed"][0]/scene_info["ball_speed"][1])*(420-self.current_ball_y)-2 #
                               # else:
                                #    self.des_x=self.current_ball_x+(-scene_info["ball_speed"][0]/scene_info["ball_speed"][1])*(420-self.current_ball_y)-3 #
                    # ball go up
                    if self.current_ball_y<self.last_ball_y:
                        self.des_x=100
                
                #record current position for next update
                self.last_ball_x = scene_info["ball"][0]
                self.last_ball_y = scene_info["ball"][1]
                while self.des_x>200 or self.des_x<0:
                    if self.des_x>200:
                        self.des_x=(200-(self.des_x-200))
                    else:
                        self.des_x=-self.des_x

                if self.des_x < scene_info["platform_1P"][0] + 15 :
                    return "MOVE_LEFT"
                elif self.des_x == scene_info["platform_1P"][0] +15 :
                    return "NONE"
                else:
                    return "MOVE_RIGHT"               

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
                    # ball go up
                    if self.current_ball_y<self.last_ball_y:
                        # ball go right
                        if self.current_ball_x>self.last_ball_x:
                            if scene_info["ball_speed"][0]<=12 or scene_info["ball_speed"][1]<=-9:
                                self.des_x=(-scene_info["ball_speed"][0]/scene_info["ball_speed"][1])*(self.current_ball_y - 80)+ self.current_ball_x #
                            else:
                                #if scene_info["ball_speed"][0]<=16:
                                    if scene_info["ball"][1]<220:
                                        self.des_x=(-scene_info["ball_speed"][0]/scene_info["ball_speed"][1])*(self.current_ball_y - 80)+ self.current_ball_x+1 #
                                    else:
                                        self.des_x=(-scene_info["ball_speed"][0]/scene_info["ball_speed"][1])*(self.current_ball_y - 80)+ self.current_ball_x+2.2#
                                #else:
                                 #   if scene_info["ball"][1]<220:
                                  #      self.des_x=(-scene_info["ball_speed"][0]/scene_info["ball_speed"][1])*(self.current_ball_y - 80)+ self.current_ball_x+2 #
                                   # else:
                                    #    self.des_x=(-scene_info["ball_speed"][0]/scene_info["ball_speed"][1])*(self.current_ball_y - 80)+ self.current_ball_x+3 #
                    # ball go left 
                        else:
                            if scene_info["ball_speed"][0]<=-12 or scene_info["ball_speed"][1]<-9:
                                self.des_x=self.current_ball_x-(scene_info["ball_speed"][0]/scene_info["ball_speed"][1])*(self.current_ball_y - 80) # 
                            else:
                                #if scene_info["ball_speed"][0]<=16:
                                    if scene_info["ball"][1]<220:
                                        self.des_x=self.current_ball_x-(scene_info["ball_speed"][0]/scene_info["ball_speed"][1])*(self.current_ball_y - 80)-1 #
                                    else:
                                        self.des_x=self.current_ball_x-(scene_info["ball_speed"][0]/scene_info["ball_speed"][1])*(self.current_ball_y - 80)-2.2#
                                #else:
                                 #   if scene_info["ball"][1]<220:
                                  #      self.des_x=self.current_ball_x-(scene_info["ball_speed"][0]/scene_info["ball_speed"][1])*(self.current_ball_y - 80)-2 #
                                   # else:
                                    #    self.des_x=self.current_ball_x-(scene_info["ball_speed"][0]/scene_info["ball_speed"][1])*(self.current_ball_y - 80)-3 #
                    # ball go down
                    if self.current_ball_y>self.last_ball_y:
                        self.des_x=100
                
                #record current position for next update
                self.last_ball_x = scene_info["ball"][0]
                self.last_ball_y = scene_info["ball"][1]
            
                while self.des_x>200 or self.des_x<0:
                    if self.des_x>200:
                        self.des_x=(200-(self.des_x-200))
                    else:
                        self.des_x=-self.des_x

                if self.des_x < scene_info["platform_2P"][0] + 15 :
                    return "MOVE_LEFT"
                elif self.des_x == scene_info["platform_2P"][0] + 15 :
                    return "NONE"
                else:
                    return "MOVE_RIGHT"

    def reset(self):
        """
        Reset the status
        """
        self.ball_served = False
