nums = list(map(int, input().split()))
target = int(input())

if target not in nums:
    print(-1)
else:
    l = 0
    r = len(nums)-1
    mid = len(nums)//2

    while(nums[mid] != target and l<r):
        if target>nums[mid]:
            l = mid + 1
        else:
            l = mid - 1
        mid = (l+r)//2

    print(mid)
        
