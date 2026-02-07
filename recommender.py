def build_transition_table(sequences):
    transition = {}
    
    for seq in sequences.values():
        for i in range((len(seq)) - 1):
            current = seq[i]
            next_event = seq[i+1]
            
            if current not in transition:
                transition[current] = {}
                
            if next_event not in transition[current]:
                transition[current][next_event] = 1
            else:
                transition[current][next_event] += 1
                
    return transition

def build_probability_table(transitions):
    probabilities = {}
    
    for current, next_dict in transitions.items():
        total = sum(next_dict.values())
        
        probabilities[current] = {}
        
        for next_event, count in next_dict.items():
            probabilities[current][next_event] = count / total
            
    return probabilities

def recommend_next(transitions, event):
    if event not in transitions:
        return None
    
    return max(transitions[event], key=transitions[event].get)