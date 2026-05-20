def hit_rate_at_k(recommendations, ground_truth, k):
    """
    Compute the hit rate at K.
    """
    # # Basic Approach 
    # hit_count = 0
    # for i, recom in enumerate(recommendations):
    #     if ground_truth[i][0] in recom[:k]:
    #         hit_count +=1

    # return hit_count/len(recommendations)

    # # Optimized Approach 1
    # hit_count = 0
    # for recom, gt in zip(recommendations, ground_truth):
    #     if gt[0] in recom[:k]:
    #         hit_count += 1

    # return hit_count/len(recommendations)

    # Optimized Approach 2
    hit_count = sum(
        gt[0] in recom[:k]
        for recom, gt in zip(recommendations, ground_truth)
    )
    
    return hit_count / len(recommendations)

        
            
            
        