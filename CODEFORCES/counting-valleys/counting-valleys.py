def countingValleys(steps, path):
    # Write your code here
    valleys_traversed = 0
    net_steps = 0
    
    for step in path:
        if step == 'U':
            net_steps += 1
        else:
            net_steps -= 1
            
        if net_steps == 0 and step == 'U':
            valleys_traversed += 1
            
    return valleys_traversed