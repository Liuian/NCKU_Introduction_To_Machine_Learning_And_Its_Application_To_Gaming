"""
The template of the script for the machine learning process in game pingpong
"""


class MLPlay:
    import random
    def __init__(self, side):
        """
        Constructor

        @param side A string "1P" or "2P" indicates that the `MLPlay` is used by
               which side.
        """
        self.ball_served = False    #self.ball_served記錄球被發出去了沒
        self.side = side
        self.ball_x = 0
        self.prev_ball_x = 0
        self.ball_y = 0
        self.prev_ball_y = 0
        self.des_x = 100             #75 is initial place
        self.blocker_x = 0
        self.prev_blocker_x = 0


    def update(self, scene_info):
        """
        Generate the command according to the received scene information
        """
        #if game pass pr game over -> reset
        if scene_info["status"] != "GAME_ALIVE":
            print(scene_info["ball_speed"])
            return "RESET"

        #if self.ball_served is False, serve the ball
        if not self.ball_served:    
            if scene_info["frame"] == 149:
                self.ball_served = True
                rand = self.random.randint(0, 1)
                if rand == 0:
                    #print("left")
                    return "SERVE_TO_LEFT"
                else:
                    return "SERVE_TO_RIGHT"

        #if self.ball_serve is true, move the plate
        else:                       
            #update the parmeters
            self.prev_ball_x = self.ball_x
            self.prev_ball_y = self.ball_y
            self.ball_x = scene_info["ball"][0]
            self.ball_y = scene_info["ball"][1]
            velo_ball_x = self.ball_x - self.prev_ball_x
            velo_ball_y = self.ball_y - self.prev_ball_y
            self.prev_blocker_x = self.blocker_x
            self.blocker_x = scene_info["blocker"][0]
            velo_blocker = self.blocker_x - self.prev_blocker_x
            hit = 0
            #print(self.prev_blocker_x, self.blocker_x)
            #print("------")

            if self.side == "1P":
                if self.ball_y > 260:                                           #if ball_y > 240, ball may hit block
                    dist = self.ball_y - 260
                    if velo_ball_x < 0:
                        des_x_ball = self.ball_x - dist                        #des_x_block record x when ball's y = 260
                    else:
                        des_x_ball = self.ball_x + dist
                    while des_x_ball > 200 or des_x_ball < 0:
                        if des_x_ball > 200:
                            des_x_ball = (200 - (des_x_ball - 200))
                        else:
                            des_x_ball = -des_x_ball
                    
                    if velo_blocker < 0:
                        des_x_blocker = self.blocker_x - (dist / 7) * 5
                    else:
                        des_x_blocker = self.blocker_x + (dist / 7) * 5
                    while des_x_blocker > 200 or des_x_blocker < 0:
                        if des_x_blocker > 200:
                            des_x_blocker = (200 - (des_x_blocker - 200))
                        else:
                            des_x_blocker = -des_x_blocker
                    if(des_x_ball > des_x_blocker and des_x_ball < des_x_blocker + 30):
                        hit = 1
                    else:
                        hit = 0
                    #print(hit, des_x_ball, des_x_blocker)

                #judge the ball's x destination
                if velo_ball_y > 0:                                             #ball go down
                    if velo_ball_x < 0:                                         #ball move left
                        self.des_x = self.ball_x - (420 - self.ball_y)
                    else:                                                       #ball move right
                        self.des_x = self.ball_x + (420 - self.ball_y)
                else:                                                           #ball move up
                    if hit == 1:                                                #ball will hit blocker
                        if velo_ball_x < 0:
                            self.des_x = self.ball_x - (360 - (420 - self.ball_y))
                        else:
                            self.des_x = self.ball_x + (360 - (420 - self.ball_y))
                        
                    else:                                                       #ball will NOT hit blocker
                        if velo_ball_x < 0:
                            self.des_x = self.ball_x - (680 - (420 - self.ball_y))
                        else:
                            self.des_x = self.ball_x + (680 - (420 - self.ball_y))
                
                #adjest the destination into the scene
                while self.des_x > 200 or self.des_x < 0:
                    if self.des_x > 200:
                        self.des_x = (200 - (self.des_x - 200))
                    else:
                        self.des_x = -self.des_x
                
                #judge the cammand
                #print(scene_info["platform_1P"][0], self.des_x)
                if scene_info["frame"] <= 150:                                  
                    return "NONE"
                elif (scene_info["platform_1P"][1] > 410 and scene_info["platform_1P"][0] + 20 + 10 > self.des_x and scene_info["platform_1P"][0] + 20 - 10 < self.des_x):
                    return "NONE"                                               #when plate in the des_x plate don't move 
                elif scene_info["platform_1P"][0] + 20 < self.des_x:            #plate at ball's right, plate move left
                    return "MOVE_RIGHT"
                elif scene_info["platform_1P"][0] + 20 > self.des_x:
                    return "MOVE_LEFT"
                else:
                    return "NONE"
            
            else:                                                               #if self.side == 2P
                
                if self.ball_y < 240:                                           #if ball_y > 240, ball may hit block
                    dist = 240 - self.ball_y
                    if velo_ball_x < 0:
                        des_x_ball = self.ball_x - dist                        #des_x_block record x when ball's y = 260
                    else:
                        des_x_ball = self.ball_x + dist
                    while des_x_ball > 200 or des_x_ball < 0:
                        if des_x_ball > 200:
                            des_x_ball = (200 - (des_x_ball - 200))
                        else:
                            des_x_ball = -des_x_ball
                    
                    if velo_blocker < 0:
                        des_x_blocker = self.blocker_x - (dist / 7) * 5
                    else:
                        des_x_blocker = self.blocker_x + (dist / 7) * 5
                    while des_x_blocker > 200 or des_x_blocker < 0:
                        if des_x_blocker > 200:
                            des_x_blocker = (200 - (des_x_blocker - 200))
                        else:
                            des_x_blocker = -des_x_blocker
                    if(des_x_ball > des_x_blocker and des_x_ball < des_x_blocker + 30):
                        hit = 1
                    else:
                        hit = 0
                    #print(hit, des_x_ball, des_x_blocker)
                
                #judge the ball's x destination
                if velo_ball_y < 0:                                             #ball move up
                    if velo_ball_x < 0:                                         #ball move left
                        self.des_x = self.ball_x - (self.ball_y - 80)
                    else:                                                       #ball move right   
                        self.des_x = self.ball_x + (self.ball_y - 80)
                else:                                                           #ball move down  
                    if hit == 1:
                        if velo_ball_x < 0:                                         #ball move left
                            self.des_x = self.ball_x - (380 - (self.ball_y - 80))
                        else:                                                       #ball move right
                            self.des_x = self.ball_x + (380 - (self.ball_y - 80))
                    else:
                        if velo_ball_x < 0:                                         #ball move left
                            self.des_x = self.ball_x - (680 - (self.ball_y - 80))
                        else:                                                       #ball move right
                            self.des_x = self.ball_x + (680 - (self.ball_y - 80))
                #adjest the destination into the scene
                while self.des_x > 200 or self.des_x < 0:
                    if self.des_x > 200:
                        self.des_x = (200 - (self.des_x - 200))
                    else:
                        self.des_x = -self.des_x
                #judge the cammand
                if scene_info["frame"] <= 150:
                    return "NONE"
                elif (scene_info["platform_2P"][1] < 60 and scene_info["platform_2P"][0] + 20 + 10 > self.des_x and scene_info["platform_2P"][0] + 20 - 10 < self.des_x):
                #elif scene_info["platform_1P"][1] <
                    return "NONE"                                               #when plate in the des_x plate don't move
                elif scene_info["platform_2P"][0] + 20 < self.des_x:            #plate at ball's right, plate move left
                    return "MOVE_RIGHT"
                elif scene_info["platform_2P"][0] + 20 > self.des_x:
                    return "MOVE_LEFT"
                else:
                    return "NONE"
            
    def reset(self):
        """
        Reset the status
        """
        self.ball_served = False
