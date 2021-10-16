"""
The template of the script for playing the game in the ml mode
"""
import random
import os.path
import pickle
from random import seed,randint,random
import math
import numpy as np

class MLPlay:
    def __init__(self):
        """
        Constructor
        """
        filename = 'model_KNN.pickle'
        filepath = os.path.join(os.path.dirname(__file__), filename)
        self.model = pickle.load(open(filepath, 'rb'))

        self.headx = 0
        self.heady = 0
        self.x_dir = 0
        self.y_dir = 0
        self.foodx = 0
        self.foody = 0
        self.current_x = 0
        self.current_y = 0
        self.last_x = 0
        self.last_y = 0
        
        self.wall_disx = 0
        self.wall_disy = 0

        self.direction = 0#上下左右 :1,2,3,4 
        self.wall = 0
        self.body = 0

    def update(self, scene_info):
        """
        Generate the command according to the received scene information
        """
        if scene_info["status"] == "GAME_OVER":
            return "RESET"

        snake_head = scene_info["snake_head"]
        food = scene_info["food"]

        if scene_info["frame"] == 0:
            
            self.current_x = snake_head[0]
            self.current_y = snake_head[1]
            self.last_x = snake_head[0]
            self.last_y = snake_head[1]
            self.x_dir = 0
            self.y_dir = 0

            self.wall_disx = 30
            self.wall_disx = 270
            self.body = 0
            self.wall = 0

            self.direction = 0 #上下左右 :1,2,3,4 

        else:
                        

            command = self.model.predict([[snake_head[0], snake_head[1]]])
            #print(command)
            if command == 0: 
                return "UP"
            elif command == 1: 
                return "DOWN"
            elif command == 2: 
                return "LEFT"
            elif command == 3: 
                return "RIGHT"
            else: 
                return "NONE"


            
        

    def reset(self):
        """
        Reset the status if needed
        """
        pass

