import matplotlib.pyplot as plt


class PID:
    dt = 0.0
    max = 0.0
    min = 0.0
    kp = 0.0
    kd = 0.0
    ki = 0.0
    err = 0.0
    int = 0.0

    def __init__(self, dt, max, min, kp, kd, ki):
        self.dt = dt
        self.max = max
        self.min = min
        self.kp = kp
        self.kd = kd
        self.ki = ki

    def run(self, set, act):
        error = set - act

        P = self.kp * error

        self.int += error * self.dt
        I = self.ki * self.int

        D = self.kd * (error - self.err) / self.dt

        output = P + I + D

        if output > self.max:
            output = self.max
        elif output < self.min:
            output = self.min

        self.err = error
        return output


def main(regler, val, goal, iterations, flet=False):
    val_list = []
    inc_list = []
    for i in range(iterations):
        inc = regler.run(goal, val)
        # print("val:", "{:7.3f}".format(val), " inc:", "{:7.3f}".format(inc))
        val_list.append(val)
        inc_list.append(inc)
        val += inc

    if flet == False:
        plt.plot(val_list)
        plt.plot(inc_list)
        plt.show()
    else:
        return val_list, inc_list


def flet_api(start, in_goal, iterations, dt, max, min, kp, ki, kd):
    pid = PID(dt, max, min, kp, kd, ki)
    val, inc = main(pid, start, in_goal, iterations, True)
    return val, inc


if __name__ == "__main__":

    pid = PID(0.1, 100, -100, 0.1, 0.01, 0.5)
    main(pid, 20, 0, 100)
