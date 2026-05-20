def top_k_recommendations(scores, rated_indices, k):
    """
    Return indices of top-k unrated items by predicted score.
    """
    # Approach 1
    unrated_items = [
        (idx, score)
        for idx, score in enumerate(scores)
        if idx not in rated_indices
    ]
    # Sort in desc order
    unrated_items.sort(key=lambda x: x[1], reverse=True)

    return [
        idx
        for idx, _ in unrated_items[:k]
    ]
    
        