# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/579/week-1-january-1st-january-7th/3589/


def canFormArray(arr, pieces):
    position_dict = {}
    for idx, num in enumerate(arr):
        position_dict[num] = idx
    
    for p in pieces:
        for idx, num in enumerate(p):
            if num not in position_dict:
                return False 
            if idx == 0:
                continue
            if position_dict[p[idx]] - position_dict[p[idx-1]] != 1:
                return False
    return True