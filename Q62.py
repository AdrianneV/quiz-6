#Adrianne Verstraete
class Ambulance:
    """Represents the quaities of an ambulance with sttributes: speed, priority and capacity"""

myAmbulance=Ambulance()
myAmbulance.priority=1
#"0 if there is no patient in the ambulance, 1 if there is"
myAmbulance.speed=80
#"mmax speed of the ambulance"
myAmbulance.capacity=3
#"the number of patients inside the ambulance"

def drive(t):
    controlled_velocity=-10*(1-t.priority)+2.37(t.speed/10)**3.98+30*(t.capacity+1.2)
    return controlled_velocity
print(drive(myAmbulance))
