#Running time complexity: O(n^2) | Space complexity: O(n^2)
# from unittest import result


def fourNumberSum(array, targetSum):
    result = []
    allPairSums = {}
    for i in range(1,len(array)-1):
        for j in range(i+1,len(array)):
            currentSum = array[i] + array[j]
            difference = targetSum - currentSum
            if difference in allPairSums:
                for pair in allPairSums[difference]:
                    result.append(pair + [array[i],array[j]] )
        for k in range(0,i):
            currentSum = array[i]+array[k]
            if currentSum not in allPairSums:
                allPairSums[currentSum] = [[array[k],array[i]]]
            else:
                allPairSums[currentSum].append([array[k],array[i]])
    return result

result = fourNumberSum([3,7,9,11,8,6],32)
print(result)