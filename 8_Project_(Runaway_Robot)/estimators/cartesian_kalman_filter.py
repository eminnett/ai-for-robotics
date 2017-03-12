from kalman_filter_2d import *

class cartesian_kf_estimator:
    def predict(self, history, measurement):
        x, y = measurement

        if len(history) == 0:
            xy_estimate = measurement
            # initialise kalman filter
            self.kf = kalman_filter_2d(measurement)
        else:
            # Update Kalman filter
            self.kf.update(measurement)
            # Get prediction from Kalman filter
            xy_estimate = self.kf.predict()

        return xy_estimate
