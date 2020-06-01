from TwoSum import TwoSumWorker


procesor = TwoSumWorker()
x = 0
nums = []
while int(x) > -1:
    x = input('Enter a number to add to the list: ')
    nums.append(int(x))

target = int(input('Enter the target: '))
ans = procesor.FindIndeces(nums, target)

print(f'number 1: {ans[0]} number 2: {ans[1]}')