# Name: Emily
# Date: July 11th
# Title: Rocket lander game

position = 100
velocity = 0
acceleration = 0
fuel = 100
gravity = -10

while position > 0:
    print "P: " + str(position) + " V: " + str(velocity) + " F: " + str(fuel)
    if fuel > 0:
        thrusters = input("Set thrusters(0-20): ")

        if thrusters < 0:
            print "No thrusters (0)!"
            thrusters = 0
        elif thrusters >= 20:
            print "Thrusters at max (20)!"
            thrusters = 20
        elif fuel < thrusters:
            print "Out of fuel! Thrusters at " + str(fuel)

        if fuel < thrusters:
            # acceleration -= (thrusters + 6)
            thrusters = fuel

        fuel -= thrusters
        acceleration = gravity + thrusters
        position += velocity + acceleration * 0.5
        velocity += acceleration

    else:
        print "No fuel -- rocket is in free-fall!"

        thrusters = 0
        fuel -= thrusters
        acceleration = gravity + thrusters
        position += velocity + acceleration * 0.5
        velocity += acceleration

if velocity > -3:
    print "Landing successful!"
else:
     print "Rocket crashed! Velocity was " + str(velocity) + " m/s"



