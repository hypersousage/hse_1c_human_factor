default_vals = {
    'accel': 2.6,  # m/s^2
    'decel': 7.5, # m/s^2
    'sigma': 0.5, # (sigma in [0, 1])
    'minGap': 2.5,  # m 
    'collisionMinGapFactor': 1.0,
    'laneChangeModel': "LC2013",
    'carFollowingModel': "Krauss",
    'latAlignment': "center",
    'minGapLat': 0.6,
    'maxSpeedLat': 1.0,
    'speedFactor': 1.0,
    'actionStepLength': 0.0,
    'jmCrossingGap': 10.0,
    'jmIgnoreKeepClearTime': -1.0,
    'jmDriveAfterRedTime': -1.0,
    'jmDriveAfterYellowTime': -1.0,
    'jmIgnoreFoeProb': 0.0,
    'jmIgnoreFoeSpeed': 0.0,
    'jmTimegapMinor': 1.0,
    'impatience': 0.0,
}

coeffs = {
    'accel': {
        'age': 1,
        'stress': 1
    },
    'collisionMinGapFactor': {
        'stress': 1,
        'age': 1
    }
}

config = {
    'age': 25,
    'stress': 0.5
}

param_to_getter = {
    'accel': 'get_accel',
    'decel': 'get_decel',
    'sigma': 'get_sigma',
    'minGap': 'get_minGap',
    'speedFactor': 'get_speedFactor',
    # 'actionStepLength': 'get_actionStepLength',
    'jmCrossingGap': 'get_jmCrossingGap',
}
