#Area = 2*PI *R H + 2 * PI * R**2

import math
import argparse

# Create a parser that will get the values of radius and hieght from input
parser1=argparse.ArgumentParser(description='compute the are of cylinder')
parser1.add_argument('radius', type=int, help='radius of the cylinder')
parser1.add_argument('height', type=int, help='height of the cylinder')
args=parser1.parse_args()


# Function for calculating the Area of Cylinder
def cylinder_area(radius,height):
    area = ((2*math.pi*args.radius*args.height)+2*math.pi*args.radius**2)
    print(f'The Area of the Cylinder is {area}')

# call the function, get the values of radius and height from parser
cylinder_area(args.radius,args.height)

