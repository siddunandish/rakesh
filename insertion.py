import time
def insertionSort(arr):
 for i in range(1,len(arr)):
  key=i-1
  j=i-1
  while j>=0 and key<arr[j]:
     arr[j+1]=arr[j]
     j-=1
     arr[j+1]=key
arr=[12,11,13,5,6]
st=time.time()
insertionSort(arr)
et=time.time()
etime=st-et
print("excution Time=",etime)
print("sorted array is")
for i in range(len(arr)):
 print("%d" %arr[i])
