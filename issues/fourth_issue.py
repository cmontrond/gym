# Issue 1698 Tried with several envs but the problem is with the envs starting with defender, they are hanging the
# jupyter notebook. Finally worked after installing atari_py in the version 0.1.x
# pip install ... downgrade 0.1.X



import gym
env = gym.make('DemonAttack-ram-v0')  # works
print(env)
env = gym.make('Defender-ram-v0') # doesn't work (it hangs)
print(env)
