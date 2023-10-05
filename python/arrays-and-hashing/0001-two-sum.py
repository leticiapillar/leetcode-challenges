def twoSum(nums: [int], target: int) -> [int]:
    for i1,n1 in enumerate(nums):
        for i2,n2 in enumerate(nums):
            if i2 > i1 and target == (n1+n2):
                return [i1,i2]
    return [-1,-1]

def twoSum_better(nums: [int], target: int) -> [int]:
    mapNums = {}
    for i,n in enumerate(nums):
        diff = target - n
        if diff in mapNums:
            return [mapNums[diff],i]
        mapNums[n] = i


def main():

    nums = [2,7,11,15]
    target = 9
    # Output: [0,1]
    print(f"Nums = {nums}, target = {target}, output {twoSum(nums, target)}")
    print(f"Better solution, Nums = {nums}, target = {target}, output {twoSum_better(nums, target)}")


    nums = [3,2,4]
    target = 6
    #Output: [1,2]
    print(f"Nums = {nums}, target = {target}, output {twoSum(nums, target)}")
    print(f"Better solution, Nums = {nums}, target = {target}, output {twoSum_better(nums, target)}")

    nums = [3,3]
    target = 6
    #Output: [0,1]    
    print(f"Nums = {nums}, target = {target}, output {twoSum(nums, target)}")
    print(f"Better solution, Nums = {nums}, target = {target}, output {twoSum_better(nums, target)}")


if __name__ == "__main__":
    main()

