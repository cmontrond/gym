from threading import Thread
import faulthandler

import gym

faulthandler.enable()


def make_t2 ():
    print(1)


def make_t1 ():
    t = Thread(target=make_t2)
    t.start()


# env = gym.make('MsPacman-v4')
# env = gym.make('CartPole-v0')
env = gym.make('Pendulum-v0')

t = Thread(target=make_t1)
t.start()