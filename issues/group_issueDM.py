# group issue # 1864
from builtins import range, zip
from gym import spaces
from gym.spaces import Tuple, MultiDiscrete, Discrete

my_seed = 0

# Test 1
for _ in range(10):
    space = spaces.Discrete(3) # Set with 8 elements {0, 1, 2, ..., 7}
    x = space.sample()
action_space = Tuple([Discrete(5), Discrete(2), Discrete(2)])

action_space.seed(my_seed)

tupled = Tuple([Tuple([Discrete(7) for _ in range(2)])for _ in range(5)])
tuplem = Tuple([MultiDiscrete([2 for _ in range(2)])for _ in range(2)])
tupled.seed(my_seed)
tuplem.seed(my_seed)
for _ in range(5):
    print("action space")
    print(action_space.sample())
    print("tupled")
    print(tupled.sample())
    print("tuplem")
    print(tuplem.sample())

""" print("tupled")
    print(tupled)
    print("tuplem")
    print(tuplem)
    # print(x)"""
print("Test 1:")

a1 = Tuple([Tuple([Discrete(5) for _ in range(2)]) for _ in range(2)])
b1 = Tuple([MultiDiscrete([5 for _ in range(2)]) for _ in range(2)])
print("a1")
print(a1)
print("b1")
print(b1)
a1.seed(my_seed)
b1.seed(my_seed)

a2 = Tuple([MultiDiscrete([10 for _ in range(2)]) for _ in range(2)])
a2.seed(my_seed)

for _ in range(5):
    print("sample starts")
    print(a2.sample())

print("sample ends")
for _ in range(5):
    print(a1.sample(), b1.sample())

# Test 2

print("Test 2:")

a2 = Tuple([Tuple([Discrete(5) for _ in range(2)]) for _ in range(2)])
b2 = Tuple([MultiDiscrete([5 for _ in range(2)]) for _ in range(2)])

for a2_space, b2_space in zip(a2, b2):
    my_seed += 1
    a2_space.seed(my_seed)
    b2_space.seed(my_seed)

for _ in range(5):
    print(a2.sample(), b2.sample())