# Write a program to update your mean and variance
# when given the mean and variance of your belief
# and the mean and variance of your measurement.
# This program will update the parameters of your
# belief function.

def update(mean1, var1, mean2, var2):
    new_mean = (mean1*var2 + mean2*var1) / (var1 + var2)
    new_var = 1. / (1. / var1 + 1. / var2)
    return [new_mean, new_var]

print update(10.,8.,13., 2.)
