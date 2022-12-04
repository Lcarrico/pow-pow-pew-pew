import math

"""
circle:
{
    radius:float
    x: float
    y: float
}


rectangle:
{
    x: float
    y: float
    width: float
    height: float
}
"""
def circleIntersectsCircle(circle1, circle2):
    return sum([circle1['radius'], circle2['radius']]) >= math.dist([circle1['x'], circle1['y']], [circle2['x'], circle2['y']])

def circleIntersectsRectangle(circle, rectangle):

    cDx = abs(circle['x'] - rectangle['x'])
    cDy = abs(circle['y'] - rectangle['y'])

    if cDx > (rectangle['width']/2 + circle['radius']): return False
    if cDy > (rectangle['height']/2 + circle['radius']): return False

    if cDx <= (rectangle['width']/2): return True
    if cDy <= (rectangle['height']/2): return True
    
    cornerDs = (cDx - rectangle['width']/2)**2 + (cDy - rectangle['height']/2)**2

    return cornerDs <= circle['radius']**2