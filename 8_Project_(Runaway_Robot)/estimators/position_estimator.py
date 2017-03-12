from mean_position import *
from cartesian_kalman_filter import *
from polar_kalman_filter import *
from circular_kalman_filter import * 

class position_estimator:

    def __init__(self, strategy='mean_position'):
        self.history = []
        self.estimator = self.estimators()[strategy]()

    def estimators(self):
        return {
            'mean_position': mean_position_estimator,
            'cartesian_kalman_filter': cartesian_kf_estimator,
            'polar_kalman_filter': polar_kf_estimator,
            'circular_kalman_filter': circular_kf_estimator
        }

    def next_position(self, measurement):
        xy_estimate = self.estimator.predict(self.history, measurement)
        self.history.append(measurement)
        return xy_estimate
