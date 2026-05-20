def hit_rate_at_k(recommendations, ground_truth, k):
    """
    Compute the hit rate at K.
    """
    # Write code 
    hit_count = 0
    for i, recom in enumerate(recommendations):
        if ground_truth[i][0] in recom[:k]:
            hit_count +=1

    return hit_count/len(recommendations)

        
            
            
        