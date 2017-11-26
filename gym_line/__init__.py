from gym.envs.registration import register

register(
    id='LineEnv-v0',
    entry_point='gym_line.envs:LineEnv',
)
