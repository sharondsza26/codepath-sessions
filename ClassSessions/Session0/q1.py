# Problem 1: Manage Performance Stage Changes
# At a cultural festival, multiple performances are scheduled on a single stage. However, due to last-minute changes, some performances need to be rescheduled or canceled. The festival organizers use a stack to manage these changes efficiently.

# You are given a list changes of strings where each string represents a change action. The actions can be:

# "Schedule X": Schedule a performance with ID X on the stage.
# "Cancel": Cancel the most recently scheduled performance that hasn't been canceled yet.
# "Reschedule": Reschedule the most recently canceled performance to be the next on stage.
# Return a list of performance IDs that remain scheduled on the stage after all changes have been applied.

# from collections import Stack
def manage_stage_changes(changes):
    schedule_stack = []
    to_reschedule = ""
    
    for action in changes:
        if action == "Cancel":
            to_reschedule = schedule_stack.pop()
            
        elif action == "Reschedule":
            schedule_stack.append(to_reschedule)
            
        else:
            performance = action.split()
            
            # [Schedule, A]
            schedule_stack.append(performance[1])
            
    return schedule_stack
    
    

print(manage_stage_changes(["Schedule A", "Schedule B", "Cancel", "Schedule C", "Reschedule", "Schedule D"]))  




print(manage_stage_changes(["Schedule A", "Cancel", "Schedule B", "Cancel", "Reschedule", "Cancel"])) 
print(manage_stage_changes(["Schedule X", "Schedule Y", "Cancel", "Cancel", "Schedule Z"])) 


# ["A", "C", "B", "D"]
# []
# ["Z"]