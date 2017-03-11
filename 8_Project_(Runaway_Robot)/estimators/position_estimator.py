from mean_position import estimate_position_from_means

class position_estimator:

    def __init__(self, strategy='mean_position'):
        self.history = []
        self.estimator = self.estimators()[strategy]

    def estimators(self):
        return {
            'mean_position': estimate_position_from_means
        }

    def next_position(self, measurement):
        xy_estimate = self.estimator(self.history, measurement)
        self.history.append(measurement)
        return xy_estimate
