from math import radians, cos, sin, asin, sqrt

def haversine(lon1, lat1, lon2, lat2):
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles
    return c * r *1000 # result in meters


def check_points_in_range(long1,lat1,long2,lat2,radius):
    res = haversine(long1,lat1,long2,lat2)
    print('Distance (meters) : '+ str(res)+" meters")
    inout=""
    if res <= radius:
        inout="inside"
    else:
        inout="outside"
    return inout
    

if __name__ == "__main__":
    print(check_points_in_range(12.122234, 72.44424, 12.122434, 72.4423,500))