import sys

def joinArray(arr_1,arr_2):
    n = len(arr_1)
    arr1 = sys.argv[1][1:n-1]
    arr1 = arr1.split(',')
    if arr1[0] == '':
        arr1 = []
    else:
        arr1 = list(map(int,arr1))

    n = len(arr_2)
    arr2 = sys.argv[2][1:n-1]
    arr2 = arr2.split(',')
    if arr2[0] == '':
        arr2 = []
    else:
        arr2 = list(map(int,arr2))
    arr1.sort()
    arr2.sort()
    joinedArr = arr1 + arr2
    joinedArr.sort()
    return joinedArr

if __name__ == '__main__':
    if len(sys.argv)<3 or len(sys.argv)>3:
        print("Function needs exactly two arrays as input")
    else:
        arr_1 = sys.argv[1]
        arr_2 = sys.argv[2]
        print(joinArray(arr_1,arr_2))