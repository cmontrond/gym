# Issue 1770 didn't want window to appear, needed only the coordinates. Issue was solved by adding params to the method
# input.

import gym



env = gym.make("CartPole-v0")
env.reset()
img = env.render(mode='rgb_array')  # Returns None
print(img)
# img = env.render(mode='rgb_array')
# Opens annoying window, but gives me the array that I want
print("shape...................")
print(img.shape)