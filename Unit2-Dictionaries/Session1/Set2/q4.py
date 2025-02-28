# Problem 4: Experiment Analysis
# Write a function data_difference() that accepts two dictionaries experiment1 and
# experiment2 and returns a new dictionary that contains only key-value pairs found 
# exclusively in experiment1 but not in experiment2.

def data_difference(experiment1, experiment2):
    exclusive1 = {}
    
    for data1, value in experiment1.items():
        if data1 not in experiment2 or experiment2[data1] != value:
            exclusive1[data1] = value
            
    return exclusive1

exp1_data = {'temperature': 22, 'pressure': 101.3, 'humidity': 45}
exp2_data = {'temperature': 18, 'pressure': 101.3, 'radiation': 0.5}

print(data_difference(exp1_data, exp2_data))