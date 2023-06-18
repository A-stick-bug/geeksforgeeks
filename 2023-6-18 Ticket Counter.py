# https://practice.geeksforgeeks.org/problems/ticket-counter-2731/1

def distributeTicket(N : int, K : int) -> int:
    nums = range(N)
    start, end = 0, N-1
    while end > start:
        for i in range(K):
            if end <= start:
                return nums[start]+1
            start += 1

        for i in range(K):
            if end <= start:
                return nums[start]+1
            end -= 1
    return nums[start]+1

print(distributeTicket(5,1))