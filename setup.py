from distutils.core import setup

setup(
    name='NI Engine',
    version='1.0beta2',
    url='https://github.com/CoryGroup/ni-engine/',
    author='Thomas Alexander and Chris Granade',
    author_email='t4alexan@uwaterloo.ca',
    package_dir={'': 'src'},
    packages=[
        'ni_engine',
        'ni_engine.config',
        'ni_engine.controllers',
        'ni_engine.controllers.abstract_controllers',
        'ni_engine.controllers.kepco',
        'ni_engine.controllers.faulhaber',
        'ni_engine.controllers.labjack',
        'ni_engine.controllers.newport',
        'ni_engine.controllers.newport.axis_positions',
        'ni_engine.controllers.test',
        'ni_engine.hardware',
        'ni_engine.hardware.faulhaber',
        'ni_engine.hardware.newport',
        'ni_engine.hardware.nidaq',
        'ni_engine.hardware.srs',
        'ni_engine.hardware.test',
        'ni_engine.hardware.labjack',
        'ni_engine.sensors',
        'ni_engine.sensors.abstract_sensors',
        'ni_engine.sensors.nidaq',
        'ni_engine.sensors.labjack',
        'ni_engine.sensors.srs',
        'ni_engine.sensors.test',
        'ni_engine.storage',
        'ni_engine.storage.physical_storage',
        'ni_engine.tools',
    ],
    package_data={'ni_engine.config': ['available_config.yml']}
)
