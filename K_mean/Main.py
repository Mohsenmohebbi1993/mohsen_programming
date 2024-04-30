#---------------------Import Liberary--------------
import pprint as pp
from math import sqrt
from random import randint

#---------------------Functins---------------------
ppoint=tuple[float,float,float] # Format of point/
# distans Oghlidos--------------------------------
def distance_Oghlidos(p1:ppoint,p2:ppoint):
    """distance_Oghlidos Summeri
        :p1 = first Point :type = tuple[float,float,float]
        :p2 = second point:type = tuple[float,float,float]
        return = distance Oghlidos (sum(x)**2+sum(y)**2+sum(z)**2)**0.5
        """

    return sqrt(((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2)+((p1[2]-p2[2])**2))

def distance_malhatan(p1:ppoint,p2:ppoint):
        """distance_malhatan Summeri
        :p1 = first Point :type = tuple[float,float,float]
        :p2 = second point:type = tuple[float,float,float]
        return = distance Oghlidos (sum(x)**2+sum(y)**2+sum(z)**2)**0.5
        """
        
        distance = 0
        for key in p1:
            if key in p2:
                distance += abs(p1[key] - p2[key])
        return distance

#--------------------------------------------------
# Clustering function
def k_means(point:list[ppoint],centers: list[ppoint]):
    # dictionary of k center with points that relation with evry center
    # one empty value with a format 
    result = [
        {
            "center": center,
            "points": [],
        }
        for center in centers
    ]
    for point in points:
        index, minimum = 0, distance_Oghlidos(point, centers[0])
        
        i = 1
        while i < len(centers):
            d = distance_Oghlidos(point, centers[i])
            if d < minimum: # if distance < distancs with first center 
                index, minimum = i, d
            # next i , maximum i is k ( k ponits)    
            i += 1  

        result[index]["points"].append(point)

    return result

# --------------------First Step--------------------
# Import Data
main_file = open("points.txt", 'r') # open file
file_1 = [line.split(',') for line in main_file.readlines()] # Break to line
points=[] 
#------------------------------------
 # if a value is Wrang ( not float) -> delete that line and if all af value of a line are float append to file
for i in range(len(file_1)):
    try :
        float(file_1[i][0]),float(file_1[i][1]),float(file_1[i][2])
        points.append((float(file_1[i][0]),float(file_1[i][1]),float(file_1[i][2]))) 
    except ValueError:
        # If Have an Error go to first
        pass
main_file.close() # close file
print("Lenght Of File is   =   ",len(points))
#---------------------------------------------

k= int(input("Number of Poitns =  "))  # K is Number of points that You need
centers=[(randint(-10,10),randint(-10,10),randint(-10,10)) for _ in range(k)]
# ------------------------------------------
while True:
    clusters = k_means(points, centers)
    new_centers = []
    for cluster in clusters:
        x, y, z = zip(*cluster["points"])
        new_centers.append(
            (
                sum(x) / len(x),
                sum(y) / len(y),
                sum(z) / len(z),
            )
        )

    if new_centers == centers:
        break

    centers = new_centers


pp.pprint(clusters)











