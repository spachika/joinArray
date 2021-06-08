from joinArray import joinArray
if len(sys.argv)<3 or len(sys.argv)>3:
        print("Function needs exactly two arrays as input")
    else:
        arr_1 = sys.argv[1]
        arr_2 = sys.argv[2]
        print(joinArray(arr_1,arr_2))