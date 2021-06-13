"""
The template of the script for playing the game in the ml mode
"""

class MLPlay:
    def __init__(self):
        """
        Constructor
        """
        self.direction = 0#上下左右 :1,2,3,4 
        self.current_x = 0
        self.current_y = 0
        self.last_x = 0
        self.last_y = 0
        self.x_dir = 0
        self.y_dir = 0
        #pass

    def update(self, scene_info):
        """
        Generate the command according to the received scene information
        """
        if scene_info["status"] == "GAME_OVER":
            snake_body = scene_info["snake_body"]
            print(len(snake_body))
            return "RESET"

        snake_head = scene_info["snake_head"]
        food = scene_info["food"]
        snake_body = scene_info["snake_body"]

        if scene_info["frame"] == 0:
            self.direction = 0 #上下左右 :1,2,3,4 
            self.current_x = snake_head[0]
            self.current_y = snake_head[1]
            self.last_x = snake_head[0]
            self.last_y = snake_head[1]
            self.x_dir = 0
            self.y_dir = 0
        
        else:
            
            self.current_x = snake_head[0]
            self.current_y = snake_head[1]
            self.x_dir = self.current_x - self.last_x
            self.y_dir = self.current_y - self.last_y
            
            if self.x_dir > 0 and self.y_dir == 0:#right
                self.direction = 4
            if self.x_dir < 0 and self.y_dir == 0:#left
                self.direction = 3
            if self.x_dir == 0 and self.y_dir > 0:#down
                self.direction = 2
            if self.x_dir == 0 and self.y_dir < 0:#up
                self.direction = 1
            self.last_x = snake_head[0]
            self.last_y = snake_head[1]
           #重複繞滿整個場地 
            if (self.current_x != 0 and self.current_x != 10 and self.current_x != 290):
                if(((self.current_y / 10) % 2) == 0):
                    return "RIGHT"
                elif(((self.current_y / 10) % 2) == 1):
                    return "LEFT"
            elif (self.current_x == 0):
                if (self.current_y == 0):
                    return "RIGHT"
                else:
                    return "UP"
            elif (self.current_x == 10):
                if(self.current_y == 290):
                    return "LEFT"
                elif((self.current_y / 10) % 2 == 0):
                    return "RIGHT"
                elif((self.current_y / 10) % 2 == 1):
                    return "DOWN"
            elif (self.current_x == 290):
                if((self.current_y / 10) % 2 == 0):
                    return "DOWN"
                elif((self.current_y / 10) % 2 == 1):
                    return "LEFT"

            if snake_head[0] > food[0]:
                return "LEFT"
            elif snake_head[0] < food[0]:
                return "RIGHT"
            elif snake_head[1] > food[1]:
                return "UP"
            elif snake_head[1] < food[1]:
                return "DOWN"

    def reset(self):
        """
        Reset the status if needed
        """
        pass
