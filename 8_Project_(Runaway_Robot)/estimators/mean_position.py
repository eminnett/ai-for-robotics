from math import *

class mean_position_estimator:
    def predict(self, history, measurement):
        x, y = measurement

        if len(history) > 0:
            x_p, y_p = history[-1]

            dx_s = [(x - x_p)]
            dy_s = [(y - y_p)]

            avg_theta = 0
            thetas = []
            distances = [sqrt(dx_s[0]**2 + dy_s[0]**2)]
            if len(history) > 1:
                history.append(measurement)

                for i in range(len(history) - 1):
                    x_p,  y_p  = history[-i-1]
                    x_pp, y_pp = history[-i-2]
                    dx_s.append((x_p - x_pp))
                    dy_s.append((y_p - y_pp))

                avg_dx = sum(dx_s) / len(dx_s)
                avg_dy = sum(dy_s) / len(dy_s)

                for j in range(len(dx_s) - 1):
                    dx = dx_s[j]
                    dy = dy_s[j]
                    dx2 = dx_s[j+1]
                    dy2 = dy_s[j+1]
                    dot_product = dx*dx2 + dy*dy2
                    dist1 = sqrt(dx**2 + dy**2)
                    dist2 = sqrt(dx2**2 + dy2**2)
                    distances.append(dist2)
                    normalised_dot_product = dot_product / (dist1*dist2)
                    if normalised_dot_product < 1 and normalised_dot_product > -1:
                        thetas.append(acos(normalised_dot_product))

            if len(thetas) > 0:
                avg_theta = sum(thetas) / len(thetas)

            avg_dist = sum(distances) / len(distances)
            print('Avg d: {}: Avg theta: {}'.format(avg_dist, avg_theta))
            alpha = atan2(dy_s[0],dx_s[0])
            angle = alpha + avg_theta
            xy_estimate = (x + avg_dist * cos(angle), y + avg_dist * sin(angle))
        else:
            xy_estimate = measurement

        return xy_estimate
