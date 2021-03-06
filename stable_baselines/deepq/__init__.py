from stable_baselines.deepq import models  # noqa
from stable_baselines.deepq.build_graph import build_act, build_train  # noqa
from stable_baselines.deepq.simple import DeepQ
from stable_baselines.deepq.replay_buffer import ReplayBuffer, PrioritizedReplayBuffer  # noqa


def wrap_atari_dqn(env):
    """
    wrap the environment in atari wrappers for DeepQ

    :param env: (Gym Environment) the environment
    :return: (Gym Environment) the wrapped environment
    """
    from stable_baselines.common.atari_wrappers import wrap_deepmind
    return wrap_deepmind(env, frame_stack=True, scale=True)
