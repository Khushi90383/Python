nums =[ 1,2,3,4,4,5,6]

for i in nums:
   for j in nums:
       if nums[i]==nums[j]:
           break

print(f'Duplicate value found {i}')