class TwoSum:
    
    
    #take in an array of numbers and a target value. Looks through the array
    #and finds the indeces of the two numbers that sum to target value.
    def FindIndeces(self, nums, target):
        for i in range(0, len(nums)):
            #if the first number we look at is bigger than the target,
            #don't bother looking at anymore, just move to the next.
            if nums[i] > target:
                continue
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [nums[i], nums[j]]


        return [-1, -1]    



procesor = TwoSum()
x = 0
nums = []
while int(x) > -1:
    x = input('Enter a number to add to the list: ')
    nums.append(int(x))

target = int(input('Enter the target: '))
ans = procesor.FindIndeces(nums, target)

print(f'number 1: {ans[0]} number 2: {ans[1]}')


