def Profit_max(A):
    n = len(A) - 1
    mid = n//2
    if n == 0:
        return (0, 0)
    else:
        buy, sell,  _, _ = Profit_max_helper(A, 0, n)
    return (buy, sell)

def Profit_max_helper(A, mini, maxi):
    if mini == maxi:
        return(0, 0, A[mini], A[maxi])
    mid = (mini + maxi)//2
    (left_buy, left_sell, left_min_val, left_max_val) = Profit_max_helper(A, mini, mid)
    (right_buy, right_sell, right_min_val, right_max_val) = Profit_max_helper(A, mid + 1, maxi)
    if left_sell - left_buy >= right_sell - right_buy:
        Opt_pair_sub = [left_buy, left_sell]
    else:
        Opt_pair_sub = [right_buy, right_sell]
    if Opt_pair_sub[1] - Opt_pair_sub[0] > right_max_val - left_min_val:
        Optimal_pair = [Opt_pair_sub[0], Opt_pair_sub[1]]
    else:
        Optimal_pair = [left_min_val, right_max_val]
    return [Optimal_pair[0], Optimal_pair[1], min(left_min_val, right_min_val), max(right_max_val, left_max_val)]
print(Profit_max([10, 15, 60, 40, 20, 1, 500, 90, 70]))