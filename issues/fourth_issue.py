# Issue 1698
import gym
env = gym.make('DemonAttack-ram-v0')  # works
print(env)
env = gym.make('Defender-ram-v0') # doesn't work (it hangs)
print(env)
