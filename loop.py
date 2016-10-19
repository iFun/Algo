
def binarySearch (sorted,target,left,right):
    

    mid = (right - left)/2 + left
    print(sorted[mid])

    if sorted[mid] == target:
        return True
    elif sorted[mid] < target and left < right:
        return binarySearch(sorted,target, mid+1, right)
    elif sorted[mid] > target and left < right:
        return binarySearch(sorted,target, left, mid-1)

    return False

haha = range(1,100000001)
if binarySearch(haha,1000,0,len(haha)-1):
    print('found it')
else:
    print('did not found the number ')