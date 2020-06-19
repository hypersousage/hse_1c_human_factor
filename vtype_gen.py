from hse_1c_human_factor.factors import HumanFactor
from random import choice
import json

param_to_getter = {
    'accel': 'get_accel',
    'decel': 'get_decel',
    'sigma': 'get_sigma',
    'minGap': 'get_minGap',
    #'actionStepLength': 'get_actionStepLength',
    'jmCrossingGap': 'get_jmCrossingGap',
    'collisionMinGapFactor' : 'get_collisionMinGapFactor',
    'minGapLat': 'get_minGapLat',
    'maxSpeedLat': 'get_maxSpeedLat',
    'jmIgnoreFoeProb': 'get_jmIgnoreFoeProb',
    #'jmIgnoreFoeSpeed': 'get_jmIgnoreFoeSpeed',
    'impatience': 'get_impatience'
}

abs_val_methods = {
    'get_accel',
    'get_decel',
    'get_sigma',
    'get_minGap',
    'get_jmCrossingGap',
    'get_minGapLat',
    'get_maxSpeedLat'
}

cur_file = "factors.json"

def gen_lines_multiple_group(n_lines: int, factors: str)->str:
    if factors:
        data = json.loads(factors)
    else:
        file = open(cur_file, "r")
        data = json.load(file)
        file.close()

    out_str = ''
    for i in range(n_lines):
        cur_factors = dict()
        for fname, values in data.items():
            if len(values) != 0:
                cur_factors[fname] = choice(values)
        
        generator = HumanFactor.HumanFactor(cur_factors)
        cur_factors = dict()
        for fname, values in data.items():
            if len(values) != 0:
                cur_factors[fname] = choice(values)
        
        generator = HumanFactor.HumanFactor(cur_factors)
        params = {}
        for pname, method_name in param_to_getter.items():
            method = getattr(generator, method_name)
            if (method_name in abs_val_methods):
                params[pname] = method(True)
            else:
                params[pname] =  method()
        
        cur_str = f'    <vType id="car{i}" vClass="passenger"'
        for pname, value in params.items():
            cur_str += f' {pname}="{value}"'
        cur_str += '/>\n'
        out_str += cur_str

    return out_str


def gen_lines_common(n_lines: int)->str:
    file = open(cur_file, "r")
    data = json.load(file)
    file.close()
    
    out_str = ''
    for i in range(n_lines):
        cur_factors = dict()
        for fname, values in data.items():
            if len(values) != 0:
                cur_factors[fname] = choice(values)
        
        generator = HumanFactor.HumanFactor(cur_factors)
        params = {}
        for pname, method_name in param_to_getter.items():
            method = getattr(generator, method_name)
            if (method_name in abs_val_methods):
                params[pname] = method(True)
            else:
                params[pname] =  method()
        
        cur_str = f'    <vType id="car{i}" vClass="passenger"'
        for pname, value in params.items():
            cur_str += f' {pname}="{value}"'
        cur_str += '/>\n'
        out_str += cur_str

    return out_str
