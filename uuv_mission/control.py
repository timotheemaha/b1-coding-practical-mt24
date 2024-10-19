class PDController:
    def __init__(self, kp: float, kd: float):
        self.kp = kp
        self.kd = kd
        self.previous_error = 0 

    def compute_curr_input(self, curr_error: float) -> float:
        """
        u[t] = KP * e[t] + KD * (e[t] - e[t-1])
        """
        difference = curr_error - self.previous_error
        curr_input = self.kp * curr_error + self.kd * difference
        self.previous_error = curr_error
        return curr_input
