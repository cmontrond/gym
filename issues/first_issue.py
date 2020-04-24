from builtins import range
import numpy as np
from gym.spaces import Box
from gym import envs, make

""" First issue #1844"""

# env = make('CartPole-v0')
env = make('DemonAttack-ram-v0') # works
print(env)
# env = gym.make('Defender-ram-v0') # doesn't work (it hangs)
# print(env)
"""for i_episode in range(10):
    observation = env.reset()
    for t in range(5):
        env.render()
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        action_space = Box(np.array([-1,-1]), np.array([+1,+1]), dtype=np.float32)
        # action_space = Box(np.float32(np.array([-1, -1])), np.float32(np.array([+1, +1])), dtype=np.float32)
        print(action_space)
        observation_space = Box(low=0, high=255, shape=(297, 528, 3), dtype=np.uint8)
        print(observation_space)
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break
env.close()"""
