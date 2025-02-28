# Problem 3: Breathing Room
# As part of your job as an astronaut, you need to perform routine safety checks. 
# You are given a dictionary oxygen_levels which maps room names to current oxygen 
# levels and two integers min_val and max_val specifying the acceptable range of oxygen levels. 
# Return a list of room names whose values are outside the range defined by 
# min_val and max_val (inclusive).

def check_oxygen_levels(oxygen_levels, min_val, max_val):
    abnormal_oxygen = []
    
    for room, level in oxygen_levels.items():
        if level < min_val or level > max_val:
            abnormal_oxygen.append(room)
            
    return abnormal_oxygen
    

oxygen_levels = {
    "Command Module": 21,
    "Habitation Module": 20,
    "Laboratory Module": 19,
    "Airlock": 22,
    "Storage Bay": 18
}

min_val = 19
max_val = 22

print(check_oxygen_levels(oxygen_levels, min_val, max_val))