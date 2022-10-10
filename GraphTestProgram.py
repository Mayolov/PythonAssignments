import matplotlib.pyplot as plt

# reverses a list
def reverse(list):
    reversedList = list[::-1]
    return reversedList

yVelocity= [0,2.95,3.94,4.10,4.10,3.94,3.86,3.56,3.41]
xPE = [8.13,4.93,1.81,.46,.39,.39,.39,.39,.39]
xPER = reverse(xPE)
print(xPER)

yHeight = [114.5,69.5,25.5,6.5,5.5,5.5,5.5,5.5,5.5]
xDistance = [102.5,202.5,261.5,291.2,501.9,702.2,888.2,1088.5,1146.5]

#Graph view of the track
plt.plot(xDistance,yHeight,label = "height")

#velocity over distance
plt.plot(xDistance,yVelocity,label = "velocity")

plt1 = plt
#plt1.plot(xPER,yHeight)

plt.xlabel('Distance')
plt.ylabel('Height or velocity')

plt.title('Velocity over distance')
plt.legend()
plt.show()
