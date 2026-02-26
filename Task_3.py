def solve_bayesian_coins():
    
    p_heads = [0.8, 0.9, 0.1, 0.2, 0.3]
    
    coin_probs = [0.2, 0.2, 0.2, 0.2, 0.2]
    
    outcomes = ['H', 'T', 'H', 'H', 'H', 'T', 'T', 'H', 'H']
    
    results = []

    for outcome in outcomes:

        updated_weights = []
        
        for i in range(len(p_heads)):
            
            likelihood = p_heads[i] if outcome == 'H' else (1 - p_heads[i])
            
            updated_weights.append(coin_probs[i] * likelihood)
            
        total_p_outcome = sum(updated_weights)
        
        coin_probs = [w / total_p_outcome for w in updated_weights]
        
        p_next_h = sum(p_heads[i] * coin_probs[i] for i in range(len(p_heads)))
        results.append(round(p_next_h, 2))

    return results

print(solve_bayesian_coins())