from kalman_filter_2d import *
from helpers import *

class circular_kf_estimator:
    def predict(self, history, measurement):
        if len(history) < 2:
            return measurement
        if len(history) == 2:
            d_theta = self.points_to_distance_and_rotation(history[-1], measurement)
            d_theta_p = self.points_to_distance_and_rotation(history[-2], history[-1])
            d_theta_o = self.points_to_distance_and_rotation((0,0), history[-1])
            # When the robot has moved at least twice, we want set theta to be the difference between measurements.
            # This works but it shouldn't
            theta = d_theta[1] - d_theta_o[1]
            d_theta = (d_theta[0], theta)
            print('First d_theta_o: {}'.format(d_theta_o))
            print('First d_theta_p: {}'.format(d_theta_p))
            print('First d_theta: {}'.format(d_theta))
            self.kf = kalman_filter_2d(d_theta)
            d_est, theta_est = self.kf.predict()
            theta_est += d_theta_p[1]
            return self.point_distance_and_rotation_to_point(measurement, d_est, theta_est)

        # Update Kalman filter
        d_theta = self.points_to_distance_and_rotation(history[-1], measurement)
        d_theta_p = self.points_to_distance_and_rotation(history[-2], history[-1])
        # When the robot has moved at least twice, we want set theta to be the difference between measurements.
        theta = d_theta[1] - d_theta_p[1]
        if theta < -pi:
            theta += 2*pi
        d_theta = (d_theta[0], theta)

        print('Update d_theta: {}'.format(d_theta))
        self.kf.update(d_theta)
        # Get prediction from Kalman filter
        d_est, theta_est = self.kf.predict()
        print('Estimated d_theta: {}'.format((d_est, theta_est)))
        theta_est += d_theta_p[1]
        return self.point_distance_and_rotation_to_point(measurement, d_est, theta_est)

    def points_to_distance_and_rotation(self, pt1, pt2):
        d = distance_between(pt1, pt2)
        pt1x, pt1y = pt1
        pt2x, pt2y = pt2
        theta = atan2(pt2y - pt1y, pt2x - pt1x)
        return (d, theta)

    def point_distance_and_rotation_to_point(self, pt1, d, theta):
        pt1x, pt1y = pt1
        pt2x = pt1x + cos(theta) * d
        pt2y = pt1y + sin(theta) * d
        print('pt1x: {}, pt1y: {}, d: {}, theta: {}, pt2x: {}, pt2y: {}'.format(pt1x, pt1y, d, theta, pt2x, pt2y))
        return (pt2x, pt2y)
