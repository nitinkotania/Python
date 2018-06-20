
#required package import goes here
from robot import Robot


#Robot driver module
if __name__ == "__main__":
    #creating obect of robot class
    print("*********************************Starting driver program for robot*************************")
    b = Robot()
    
    while(1):
        user_input = str(input("\nChoose one of the following option \n1 : Walk \n2 : Walk and Carry \n3 : Carry \n4 : Charge \nq : Exit\n"))

        if('1' == user_input):
            try:
                dist = float(input("Enter distance to walk: "))
                if not dist:
                    raise ValueError()
                b.walk(dist)
            except (ValueError) as  e:
                print(e)
                        
        elif('2' == user_input):
            try:
                dist = float(input("Enter distance to walk: "))
                weight = float(input("Enter weight to carry: "))
                if not dist or not weight:
                    raise ValueError()
                b.walk_and_carry(dist,weight)
            except (ValueError) as  e:
                print(e)

        elif('3' == user_input):
            try:
                weight = float(input("Enter weight to carry: "))
                if not weight:
                    raise ValueError()
                b.carry(weight)
            except (ValueError) as e:
                print(e)

        elif('4' == user_input):
            try:
                energy = float(input("Enter the amount of energy to charge robot battery: "))
                if not energy:
                    raise ValueError()
                b.rs.set_charging_status(energy)
                print("Current battery level" + str(b.rs.get_charging_status()) + "\n")
            except (ValueError) as e:
                print(e)

        elif('q' == user_input):
            break

        else:
            print("Provided wrong input\n")

    print("*********************************Ending driver program for robot*************************")
    
