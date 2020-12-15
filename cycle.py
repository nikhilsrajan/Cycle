from vec3 import Vec3, norm2
from math import radians, sin, cos, tan, atan2, pi

class Cycle():
    def __init__(self, F:Vec3=Vec3(0,0.5), B:Vec3=Vec3(0,-0.5)):
        if not isinstance(F, Vec3):
            raise TypeError(f'F must be of instance Vec3')
        if not isinstance(B, Vec3):
            raise TypeError(f'B must be of instance Vec3')
        self.F = F
        self.B = B
        self.theta = 0.0
        self.path_history = []
        self._record_position()

    def _record_position(self):
        self.path_history.append((self.F, self.B))

    def unpack_path_history(self):
        Fx = []; Fy = []; Bx = []; By = []
        for path in self.path_history:
            Fx.append(path[0].x); Fy.append(path[0].y)
            Bx.append(path[1].x); By.append(path[1].y)
        return Fx, Fy, Bx, By

    def set_theta(self, theta:float):
        self.theta = theta

    @staticmethod
    def calc_O(F:Vec3, B:Vec3, theta:float):
        """calculate the point of intersection of axes of wheels F and B"""
        if F == B:
            raise ValueError('F cannot be equal to B')
        if theta == 0.0:
            raise ValueError('theta cannot be equal to 0.0')
        L = F - B
        Ox = norm2(L) / tan(theta)
        phi = atan2(L.y, L.x)
        alpha = phi - pi/2.0
        return Vec3(cos(alpha)*Ox, sin(alpha)*Ox) + B

    @staticmethod
    def rotate_point_by(P:Vec3, O:Vec3, dtheta:float):
        """rotate point P about O by dtheta radians"""
        PO = P - O
        R = norm2(PO)
        cos_theta = PO.x / R
        sin_theta = PO.y / R
        cos_dtheta = cos(dtheta)
        sin_dtheta = sin(dtheta)
        cos_theta_plus_dtheta = cos_theta*cos_dtheta - sin_theta*sin_dtheta
        sin_theta_plus_dtheta = sin_theta*cos_dtheta + sin_dtheta*cos_theta
        return Vec3(cos_theta_plus_dtheta, sin_theta_plus_dtheta)*R + O

    def move_one(self, step_size:float=0.1):
        if self.theta == 0.0:
            """move straight"""
            L = self.F - self.B
            phi = atan2(L.y, L.x)
            dx = step_size * cos(phi)
            dy = step_size * sin(phi)
            self.F += Vec3(dx, dy)
            self.B += Vec3(dx, dy)
        else:
            """move in circle"""
            O = self.calc_O(self.F, self.B, self.theta)
            RF = norm2(self.F - O)
            mul = -1 * (self.theta > 0.0) + (self.theta < 0.0)
            dtheta = step_size / RF * mul
            self.F = self.rotate_point_by(self.F, O, dtheta)
            self.B = self.rotate_point_by(self.B, O, dtheta)
        self._record_position()
