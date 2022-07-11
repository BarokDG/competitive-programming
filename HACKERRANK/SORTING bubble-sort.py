def countSwaps(a):
    numberOfSwaps = 0
    
    for n in range(len(a)):
        for x in range(len(a)- 1):
            if a[x] > a[x+1]:
                a[x], a[x+1] = a[x+1], a[x]
                numberOfSwaps += 1
    
    print(f"Array is sorted in {numberOfSwaps} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")