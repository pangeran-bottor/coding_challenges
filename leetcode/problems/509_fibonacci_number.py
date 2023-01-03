class Solution:
    def fib(self, n: int) -> int:
        cache = {0: 0, 1: 1}
        
        def recur_fib(num):
            if num in cache:
                return cache[num]

            res = recur_fib(num-1) + recur_fib(num-2)
            cache[num] = res
            return res

        return recur_fib(n)
