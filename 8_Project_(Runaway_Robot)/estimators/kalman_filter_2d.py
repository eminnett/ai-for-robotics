from matrix import *

class kalman_filter_2d:

    def __init__(self, initial_position):
        self.measurement_uncertainty = 0.1
        self.initialise(initial_position)

    def initialise(self, initial_position):
        self.x = matrix([[initial_position[0]], [initial_position[1]], [0.], [0.]]) # initial state (location and velocity)
        self.P = matrix([[0.,0.,0.,0.],[0.,0.,0.,0.],[0.,0.,1000., 0.],[0.,0.,0.,1000.]]) # initial uncertainty: 0 for positions x and y, 1000 for the two velocities

    def rewrite_history(self, history):
        initial_position = history.pop()
        self.initialise(initial_position)

        for position in history:
            self.update(position)
            self.predict()

    def predict(s):
        dt = 1
        u = matrix([[0.], [0.], [0.], [0.]]) # external motion
        F = matrix([[1., 0., dt, 0.], [0., 1., 0., dt], [0., 0., 1., 0.], [0., 0., 0., 1.]]) # next state function: generalize the 2d version to 4d

        s.x = (F * s.x) + u
        s.P = F * s.P * F.transpose()

        # print(s.x)

        pos1 = s.x.value[0][0]
        pos2 = s.x.value[1][0]
        return (pos1, pos2)

    def update(s, measurement):
        H = matrix([[1.,0.,0.,0.], [0.,1.,0.,0.]]) # measurement function: reflect the fact that we observe x and y but not the two velocities
        R = matrix([[s.measurement_uncertainty,0.],[0.,s.measurement_uncertainty]]) # measurement uncertainty: use 2x2 matrix with 0.1 as main diagonal
        I = matrix([[1.,0.,0.,0.],[0.,1.,0.,0.],[0.,0.,1.,0.],[0.,0.,0.,1.]]) # 4d identity matrix

        Z = matrix([list(measurement)])
        y = Z.transpose() - (H * s.x)
        S = H * s.P * H.transpose() + R
        K = s.P * H.transpose() * S.inverse()

        s.x = s.x + (K * y)
        s.P = (I - (K * H)) * s.P
