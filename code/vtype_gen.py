from Personality import personality_generator

param_to_getter = {
    'accel': 'get_accel',
    'decel': 'get_decel',
    'sigma': 'get_sigma',
    'minGap': 'get_minGap',
    'speedFactor': 'get_speedFactor',
    # 'actionStepLength': 'get_actionStepLength',
    'jmCrossingGap': 'get_jmCrossingGap',
}

abs_val_methods = [
    
]

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

def gen_lines_personal(n_lines: int, generator) -> str:
    params = {}
    for pname, method_name in param_to_getter.items():
        method = getattr(generator, method_name)
        if (method_name in abs_val_methods):
            params[pname] = method(True)
        else:
            params[pname] = default_vals[pname] * (1 + method())
    print(params)
    out_str = ''
    for i in range(n_lines):
        cur_str = f'    <vType id="car{i}" vClass="passenger"'
        for pname, value in params.items():
            cur_str += f' {pname}="{value}"'
        cur_str += '/>\n'
        out_str += cur_str

    return out_str

def gen_lines_common(n_lines: int, factors: dict) -> str:
    generator = HumanFactor(factors.values())
    params = {}
    for pname, method_name in param_to_getter:
        method = getattr(generator, method_name)
        if (method_name in abs_val_methods):
            params[pname] = method(True)
        else:
            params[pname] =  (1 + method())

    out_str = ''
    for i in range(n_lines):
        cur_str = f'<vType id="car{i}" vClass="passenger"'
        for pname, value in params:
            cur_str += f' {pname}="{value}"'
        cur_str += '\n'
        out_str += cur_str

    return out_str
