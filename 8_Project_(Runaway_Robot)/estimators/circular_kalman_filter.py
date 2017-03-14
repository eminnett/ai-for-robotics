from kalman_filter_2d import *
from helpers import *

class circular_kf_estimator:
    def __init__(self):
        self.predictions = []

    def predict(self, history, measurement):
        if len(history) < 2:
            return measurement

        d_theta = self.points_to_distance_and_rotation(history[-2], history[-1], measurement)
        print('d_theta: {}'.format(d_theta))
        if len(history) == 2:
            self.kf = kalman_filter_2d(d_theta)
        else:
            self.kf.update(d_theta)
        d_est, theta_est = self.kf.predict()
        print('d_est: {}, theta_est: {}'.format(d_est, theta_est))
        theta_est += self.angle_between_vector_and_horizontal(history[-1], measurement)
        print('theta_est (after addition): {}'.format(theta_est))

        prev_prediction = self.predictions[-1] if len(self.predictions) > 0 else measurement
        prediction = self.point_distance_and_rotation_to_point(prev_prediction, d_est, theta_est)
        self.predictions.append(prediction)
        return prediction

    def points_to_distance_and_rotation(self, pt1, pt2, pt3):
        d = distance_between(pt2, pt3)
        x1, y1 = pt1
        x2, y2 = pt2
        x3, y3 = pt3
        # The vector between pt1 and pt2
        a = (x2 - x1, y2 - y1)
        # The vector between pt2 and pt3
        b = (x3 - x2, y3 - y2)
        # theta is the angle of rotation between the line extending from a and b.
        theta = acos(dot(a, b)/(distance_between(pt1, pt2)*distance_between(pt2, pt3)))
        return (d, theta)

    def angle_between_vector_and_horizontal(self, pt1, pt2):
        pt0 = pt1[0] - 1, pt1[1]
        theta = self.points_to_distance_and_rotation(pt0, pt1, pt2)[1]
        if pt2[1] < pt1[1]:
            theta *= -1
        return theta

    def point_distance_and_rotation_to_point(self, pt1, d, theta):
        pt1x, pt1y = pt1
        pt2x = pt1x + cos(theta) * d
        pt2y = pt1y + sin(theta) * d
        print('pt1x: {}, pt1y: {}, d: {}, theta: {}, pt2x: {}, pt2y: {}'.format(pt1x, pt1y, d, theta, pt2x, pt2y))
        return (pt2x, pt2y)
