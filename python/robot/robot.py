
#require import goes here
from robot_health import Health
from robot_status import Status
from validate_decorator import Validate_input

#Primary class which perform all activities/tasks of the Robot.
class Robot(Health,Status):

    def __init__(self):
        self.rh = Health()
        self.rs = Status()
    
    #Walk activity
    @Validate_input
    def walk(self, dist_km):
        print("************************************************")
        print("Task (walk): walk " + str(dist_km) + " km")
        required_charging = dist_km * 20              #20% battery discharged per km
        if(self.rh.power_check(self.rs, required_charging)):
            print("Robot walked " + str(dist_km) + "km \nCharging used " + str(round(required_charging,2)) + " % \nRemaining charge level " + str(self.rs.get_charging_status()) + " %")
            print("Robot headlight color "+ self.rs.get_head_light_color())
            print("************************************************")
            return True
        else:
            print("Robot headlight color "+ self.rs.get_head_light_color())
            return False

    #Carry activity
    @Validate_input
    def carry(self, weight):
        print("************************************************")
        print("Task (carry): carry " + str(weight) + " kg")
        required_charging = weight * 2              #2% battery discharged per kg
        if(self.rh.can_carry(self.rs,weight,required_charging)):
            print("Weight is allowed to carry: " + str(weight))
            print("Robot Remaining charge level " + str(self.rs.get_charging_status()) + " %")
            print("Robot headlight color "+ self.rs.get_head_light_color())
            return True
        else:
            print("Robot headlight color "+ self.rs.get_head_light_color())
            return False
   
    #walk and carry activity
    @Validate_input
    def walk_and_carry(self, dist, weight):
        print("************************************************")
        print("Task (carry and walk): carry " + str(weight) + " kg, " + "walk " + str(dist))
        required_charging = dist * 20  + 2 * weight #can write a separate api to calculate this stuf
        if(self.rh.can_carry(self.rs, weight,required_charging)):
            if(self.rh.power_check(self.rs, required_charging)):
                print("Robot carried "+ str(weight)+"kg \nCharging used "+ str(round(required_charging,2)) + " % \nRemaining charge level  " + str(self.rs.get_charging_status()) + " %")
                print("Robot headLight color "+ self.rs.get_head_light_color())
                print("************************************************")
                return True
            else:
                print("Robot headlight color "+ self.rs.get_head_light_color())
                return False

