class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        arr = []
        
        for num in range(1, n + 1):        
            if (num % 3 == 0 and num % 5 == 0):
                arr.append("FizzBuzz")
            elif(num % 3 == 0):
                arr.append("Fizz")
            elif(num % 5 == 0):
                arr.append("Buzz")
            else:
                arr.append(str(num))
        
        return arr