
def swap(arr, f, t):
  temp = arr[f]
  arr[f] = arr[t]
  arr[t] = temp

def permute(arr, start):
  if start == len(arr)-1:
    print arr
  for i in range(start, len(arr)):
    swap(arr, start, i)
    permute(arr, start+1)
    swap(arr, start, i)
