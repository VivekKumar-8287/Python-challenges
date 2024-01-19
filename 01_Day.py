""" print(2+3)
print(3-1)
print(2*3)
print(3/2)
print(3**2)
print(3%2)
print(3//2) """

""" 
#Checking data types
print(type(3))
print(type(3.14))
print(type(1 + 3j))
print(type('Vivek'))
print(type([1,2,3]))
print(type({'name':'Vivek'}))
print(type((9.8,8.4,5.6)))
print(type({9.8,8.4,5.6}))
 """

# Find an Euclidian distance between (2, 3) and (10, 8)
import math

point1 = (2,3)
point2 = (10,8)

# Calculate Euclidean distance
distance = math.sqrt((point2[0]-point1[0])**2 + (point2[1]-point1[1])**2)

print("Euclidean distance between ", point1 ,"and", point2,"is: ", distance)