

"""
Status class for Robot: Keeps track of Robot's parameteres
                        -- update robot parameters
                        -- provide updated robot parameters
"""

class Status():
    def __init__(self):
        self.charging_status = 100
        self.head_light_color = 'GREEN'
        self.max_weight_capacity = 10

    def get_charging_status(self):
        return self.charging_status

    def set_charging_status(self,remaining):
        if(100 < remaining):
             print("Charging not allowed more than 100%\n")
             return  False
        self.charging_status = round(remaining,2)
        if(15 > self.charging_status):
            self.head_light_color = 'RED'
        else:
            self.head_light_color = 'GREEN'
        return True

    def set_head_light_color(self,color):
        self.head_light_color = color.upper()
  
    
    def get_head_light_color(self):
        return self.head_light_color

    def get_max_weight_capacity(self):
        return self.max_weight_capacity
