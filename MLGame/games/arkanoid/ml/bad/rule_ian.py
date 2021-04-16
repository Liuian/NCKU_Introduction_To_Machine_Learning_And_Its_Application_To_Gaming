#first
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

    def update(self, scene_info):

        """
        Generate the command according to the received scene_info.
        """
        global current_ball_x,current_ball_y,des_x,last_ball_x,last_ball_y
        # Make the caller to invoke reset() for the next round.
        if (scene_info["status"] == "GAME_OVER" or
            scene_info["status"] == "GAME_PASS"):
            return "RESET"

        if not self.ball_served:
            self.ball_served = True
            #隨機向左右發球
            seed()
            rnd_val = randint(0,1)
            if rnd_val == 1:
                command = "SERVE_TO_LEFT"
            else:
                command = "SERVE_TO_RIGHT"
        else:
            global current_ball_x
            global current_ball_y
            global des_x                                            #預測落到盤子的點
            global last_ball_x 
            global last_ball_y 
            #command = "MOVE_LEFT"   原始的程式碼
            #print(scene_info)
            
            if scene_info["frame"]==0 or scene_info["frame"]==1:
                current_ball_x=scene_info["ball"][0]
                current_ball_y=scene_info["ball"][1]
                last_ball_x = 100
                des_x = 80
            else:
                last_ball_x = current_ball_x
                last_ball_y = current_ball_y
                current_ball_x=scene_info["ball"][0]
                current_ball_y=scene_info["ball"][1]
                #假設球都是45度動的狀態下
                if current_ball_x - last_ball_x == 7 or current_ball_x - last_ball_x == -7:
                    #print("loop")
                    if current_ball_y>last_ball_y:                      #下降中
                        if current_ball_x>last_ball_x:                  #正在往右
                            des_x=(400-current_ball_y)+current_ball_x   #預測球落下的位置 是球x座標加上（運動方向）球與盤子的距離 
                        else:                                           #正在往左
                            des_x=current_ball_x-(400-current_ball_y)   #同上
                    else:                      #正在往上
                        des_x= 80                                       #不預測位置
                #假設球是以（+-10, +- 7)的角度動的話
                else:
                    if current_ball_y>last_ball_y:                      #下降中
                        if current_ball_x>last_ball_x:                  #正在往右
                            des_x=(400-current_ball_y) * 10 / 7 + current_ball_x   #預測球落下的位置 
                        else:                                           #正在往左
                            des_x=current_ball_x - (400-current_ball_y) * 10 / 7   #同上
                    if current_ball_y<last_ball_y:                      #正在往上
                        des_x= 80                                       #不預測位置
            #預測點調整回遊戲螢幕
            while des_x>200 or des_x<0:                             
                if des_x>200:
                    des_x=(200-(des_x-200))                         
                else:
                    des_x=-des_x
            
            #log/third.pickle使用的方法:隨機掉到板子的點
            #球落板子的點隨機
            extra_range = randint(-10, 10)
            des_x = des_x + extra_range
            if des_x < scene_info["platform"][0] + 20:
                command = "MOVE_LEFT"
            elif des_x > scene_info["platform"][0] + 20:
                command = "MOVE_RIGHT"
            else:
                command = "NONE"
            #print(current_ball_x, last_ball_x)
        return command

    def reset(self):
        """
        Reset the status
        """
        self.ball_served = False
"""
    #log/second.pickle使用的方法＿在球夠低時隨機移動板子
            if current_ball_y < 395:#若球還很高預測點動盤子
                if des_x<scene_info["platform"][0]+20:
                    command = "MOVE_LEFT"
                elif des_x>scene_info["platform"][0]+20:
                    command = "MOVE_RIGHT"
                else:
                    command = "NONE"
            else:#若球夠低，隨機動盤子
                randplate = randint(0, 2)
                if randplate == 0:
                    command = "MOVE_LEFT"
                elif randplate == 1:
                    command = "MOVE_RIGHT"
                else:
                    command = "NONE"
"""
