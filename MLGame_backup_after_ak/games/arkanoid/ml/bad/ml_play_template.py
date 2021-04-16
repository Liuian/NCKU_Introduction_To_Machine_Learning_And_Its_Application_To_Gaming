"""
The template of the main script of the machine learning process
"""

class MLPlay:
    def __init__(self):
        """
        Constructor
        """
        self.ball_served = False

    def update(self, scene_info):
        """
        Generate the command according to the received `scene_info`.
        """
        # Make the caller to invoke `reset()` for the next round.
        if (scene_info["status"] == "GAME_OVER" or
            scene_info["status"] == "GAME_PASS"):
            return "RESET"

        if not self.ball_served:
            self.ball_served = True
            command = "SERVE_TO_LEFT"#ball to left
        else:
            #origional code
            #command = "MOVE_LEFT"#plate to left
            if scene_info["frame"] == 0:
                current_ball_x = scene_info["ball"][0]
                current_ball_y = scene_info["ball"][1]
            else:
                prev_ball_x = current_ball_x
                prev_ball_y = current_ball_y
                current_ball_x = scene_info["ball"][0]
                cuttent_ball_y = scene_info["ball"][1]
        return command

    def reset(self):
        """
        Reset the status
        """
        self.ball_served = False
