# Envoroment
x in space [-50, 50]

reward = -math.abs(x) - math.pow(.5 * action, 2)


# Installation

```
cd gym-line
pip install -e .
```

# Import
```
import gym_line
import gym
env = gym.make('LineEnv-v0')

```
