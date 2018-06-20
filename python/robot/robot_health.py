
"""Utilit class for Robot """

class Health():

    #can_carry() checks: provided weight is allowed or not.
    def can_carry(self, rs, weight, required_charging):	
        if(weight > rs.get_max_weight_capacity()):
            print("LED chest display: Overweight")
            print("Maximum allowed weight: " + str(rs.get_max_weight_capacity()) + "kg")
            print("Robot Remaining charge level: " + str(rs.get_charging_status()) + " %")
            print("************************************************")
            return False
        else:
            return self.power_check(rs, required_charging)
            #return True

    #power_check() checks: Robot has sufficeint chargin or not to perform the task
    def power_check(self, rs, required_charging):
        availble_charging = rs.get_charging_status();
        if(availble_charging < required_charging):
            print("Insufficient Charging For Task")
            print("Required charging: " + str(required_charging) + " %")
            print("Available charging: " + str(availble_charging)+ " %")
            return False
        else:
            remaining = availble_charging - required_charging
            rs.set_charging_status(remaining)
            if(remaining < 15):
                rs.set_head_light_color('RED')
                print("Head light color chagned to RED\n")
            return True
