# https://practice.geeksforgeeks.org/problems/queue-operations/1

def insert(q, k):
    q.append(k)

def findFrequency(q, k):
    return q.count(k)