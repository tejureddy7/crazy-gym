import gym
import crazy_gym
env = gym.make('CrazyFlieBase-v0')
<<<<<<< HEAD

for episode in range(10): 
    obs = env.reset()
    for step in range(50):
        action = env.action_space.sample() # take a random action
        env.step(action)
        state, reward, done, _ = env.step(action)
    
=======
>>>>>>> edf03d25b3b5d110fcd59a6871c610cb93cec29d
