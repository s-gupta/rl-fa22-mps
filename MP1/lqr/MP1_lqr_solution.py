import numpy as np

def get_system(env):
    if env.unwrapped.spec.id == 'PendulumInvert-v1':
        system = PendulumBalance(dt=0.05)
    if env.unwrapped.spec.id == 'PendulumBalance-v1':
        system = PendulumBalance(dt=0.05)
    if env.unwrapped.spec.id == 'DoubleIntegrator-v1':
        system = DoubleIntegrator(dt=0.05)
    return system

class LQRControl(object):
    def __init__(self, env, state=None):
        self.system = get_system(env)
        A, B, Q, R = self.system.get_system()
        self.lqr = LQRSolver(A, B, Q, R, 200)
        self.lqr.solve()
        self.step = 0

    def act(self, state):
        u = self.lqr.get_control(state, self.step)
        self.step += 1
        return u

class LQRSolver(object):
    def __init__(self, A, B, Q, R, T):
        self.A, self.B, self.Q, self.R = A, B, Q, R
        self.T = T

    def solve(self):
        # TODO: Implement the solver here
        pass

    def get_control(self, x, i):
        # TODO: Implement the controller here and return u
        pass

class DoubleIntegrator(object):
    def __init__(self, dt):
        self.dt = dt
    
    def get_system(self):
        # TODO: Return A, B, Q , R for this system
        return None

class PendulumBalance(object):
    def __init__(self, dt):
        self.dt = dt
    
    def get_system(self):
        # TODO: Return A, B, Q, R for this system
        return None