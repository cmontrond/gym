# issue #1847

from threading import Thread
import faulthandler

import gym

faulthandler.enable()


def make_t2():
    print(1)


def make_t1():
    th = Thread(target=make_t2)
    th.start()


# env = gym.make('MsPacman-v4')
# env = gym.make('CartPole-v0')

t = Thread(target=make_t1)
t.start()
