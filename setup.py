from setuptools import setup

setup(name='gym_pybullet_drones',
    version='0.5.0',
    install_requires=['gym', 'pybullet', 'stable_baselines3', 'ray[rllib]']
)
