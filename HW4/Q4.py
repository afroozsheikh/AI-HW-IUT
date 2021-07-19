import numpy as np
import matplotlib.pyplot as plt
import gym
import random

# HYPERPARAMETERS

number_of_states = 5
slip_chance = 0.2
small_reward = 2
large_reward = 10
gamma = 0.9  # Discounting rate


env = gym.make("NChain-v0", slip=slip_chance, n=number_of_states, small=small_reward, large=large_reward)

V = np.zeros(number_of_states)


# Training

print(V)

# Testing

test_steps = 10000
state = env.reset()
cumulative_rewards = 0

for step in range(test_steps):
    next_state = min(state + 1, number_of_states - 1)    
    forward_value = (1 - slip_chance) * V[next_state] + slip_chance * V[0]
    bacward_value = slip_chance * V[next_state] + (1 - slip_chance) * V[0]

    if forward_value > bacward_value:
        action = 0
    else:
        action = 1
    
    new_state, reward, done, info = env.step(action)

    # print(state, action, new_state, reward)

    cumulative_rewards += reward      
    state = new_state
    

print ("Cumulative reward: {}".format(cumulative_rewards))
print ("Average reward: {}".format(cumulative_rewards / test_steps))
