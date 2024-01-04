from statistics import mean
from collections import defaultdict


def solution(a:list[int]) -> list[int]:

    #maintain a dictionary k:v mean:[indices]

    # if key not in dict:
    #     dict[key] = [value]

    meanToindex = defaultdict(list)

    for index, arr in enumerate(a):
        arr_mean = mean(arr)

        meanToindex[arr_mean].append(index)

    # sortedValues = []

    # for m in meanToindex:
    #     sortedValues.append(sorted(meanToindex[m]))

    # return sortedValues
        
    return [sorted(meanToindex[m]) for m in meanToindex]
