def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    # # Approach 1
    # hit_count = 0
    # for i in recommended[:k]:
    #     if i in relevant:
    #         hit_count += 1

    # precision = hit_count/k
    # recall = hit_count/len(relevant)
    # return [precision, recall

    # Approach 2
    hit_count = sum(
        recom in relevant
            for recom in recommended[:k]
    )
    return [hit_count/k, hit_count/len(relevant)]