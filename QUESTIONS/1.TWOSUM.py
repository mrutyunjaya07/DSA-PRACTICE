# class Solution:
#     #function definition
#     def twoSum(self, nums: list[int], target: int) -> list[int]: #returns list of integers
#         num_map = {}  #dictionary to store numbers and their indices
#         for i, num in enumerate(nums): #loop through the list with index
#             complement = target - num
#             if complement in num_map:
#                 return [num_map[complement], i] #return indices if complement found
#             num_map[num] = i #store number and its index
#         return []  #return empty list if no solution found
    
    
    
# # Example usage:
# solution = Solution() #create an instance of the Solution class
# result = solution.twoSum([2, 7, 11, 15], 9) #call the twoSum method
# print(result)  # Output: [0, 1]



# # enumerate function --> index and value while iterating through the list with fixed order


# 1ST line - n
# 	2nd line - space separated integer
# 	3rd line - target
# 	output - indices(0 based) or -1 if not found


def twosum(n, arr, target):
	seen={ }

	for i in range(n):
		complement = target - arr[i]
		if complement in seen:
			return seen[complement], i
		seen[arr[i]] = i

	return -1


n=int(input().strip())
arr=list(map(int, input().strip("[]").split(",")))
target= int(input().strip())
print(arr)

result = twosum(n, arr, target)
print(result)
if result == -1:
	print(-1)
else:
	print(result[0], result[1])