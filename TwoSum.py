class TwoSum:
    
    
    #take in an array of numbers and a target value. Looks through the array
    #and finds the indeces of the two numbers that sum to target value.
    def FindIndeces(self, nums, target):
        for i in range(0, len(nums)):
            #if the first number we look at is bigger than the target,
            #don't bother looking at anymore, just move to the next.
            if nums[i] > target:
                continue
            print(i)
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [nums[i], nums[j]]


        return [-1, -1]    



x = TwoSum()
ans = x.FindIndeces([1,2,3, 7], 5)

print(f'number 1: {ans[0]} number 2: {ans[1]}')


