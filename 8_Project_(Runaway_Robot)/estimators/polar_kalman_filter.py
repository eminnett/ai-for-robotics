from math import *
from kalman_filter_2d import *

class polar_kf_estimator:

    def __init__(self):
        self.angle_to_add = 0

    def predict(self, history, measurement):
        x, y = measurement

        if len(history) == 0:
            xy_estimate = measurement
            # initialise kalman filter
            self.kf = kalman_filter_2d((0, 0))
        else:
            xs = []
            ys = []
            for position in history:
                xs.append(position[0])
                ys.append(position[1])

            center = (sum(xs)/float(len(history)), sum(ys)/float(len(history)))

            polar_history = []
            angle = 0
            for position in history:
                xc = position[0] - center[0]
                yc = position[1] - center[1]
                polar_pos = self.cartesian_to_polar_with_center((xc, yc))
                if polar_pos[1] < angle:
                    angle += 2*pi
                polar_pos = (polar_pos[0], polar_pos[1] + angle)
                polar_history.append(polar_pos)

            self.kf.rewrite_history(polar_history)
            # Convert from cart to polar with a center
            polar = self.cartesian_to_polar_with_center(measurement)
            if polar[1] < self.angle_to_add:
                self.angle_to_add += 2*pi
            polar = (polar[0], polar[1] + self.angle_to_add)
            print(polar)
            # Update Kalman filter
            self.kf.update(measurement)
            # Get prediction from Kalman filter
            polar_estimate = self.kf.predict()
            # Convert predition from polar to cart
            xe, ye = self.polar_to_cartesian_with_center(polar_estimate)

            xy_estimate = (xe + center[0], ye + center[1])

        return xy_estimate

    def cartesian_to_polar_with_center(self, cartesian):
        x, y = cartesian
        rho = sqrt(x**2 + y**2)
        phi = atan2(y, x)
        return (rho, phi)

    def polar_to_cartesian_with_center(self, polar):
        rho, phi = polar
        x = rho * cos(phi)
        y = rho * sin(phi)
        return (x, y)
