import gym
import crazy_gym
env = gym.make('CrazyFlieBase-v0')

for episode in range(10): 
    obs = env.reset()
    for step in range(50):
        action = env.action_space.sample() # take a random action
        env.step(action)
        state, reward, done, _ = env.step(action)
    
