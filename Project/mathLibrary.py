import math


# get the path of the projectile without wind
def noWindPath(pos, speed, angle, time, gravity):
    v0 = speed[0] * math.cos(angle)
    w0 = speed[1] * math.sin(angle)
    xt = v0 * time + pos[0]
    yt = (-1 / 2) * gravity * math.pow(gravity, 2) + w0 * time + pos[1]
    currentPos = [xt, yt]
    return currentPos


# get the path of the projectile with wind
def windPath(pos, speed, angle, time, friction, gravity):
    xt = pos[0] + ((speed[0] * math.cos(angle)) / friction) * (1 - math.exp(-friction * time))
    yt = pos[1] + ((speed[1] * math.sin(angle)) / friction) * (1 - math.exp(- friction * time)) - (
            (gravity * time) / friction)
    currentPos = [xt, yt]
    return currentPos
