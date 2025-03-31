def caching_fibonacci():

    cache = {}
    
    def fibonacci(n):

        if n <= 0:
            return 0
        if n == 1:
            return 1
        
 
        if n in cache:
            return cache[n]
        

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]
    
    return fibonacci

if __name__ == "__main__":

    fib = caching_fibonacci()
    

    print(fib(10))  # Should output 55
    print(fib(15))  # Should output 610
    
    import time

    start_time = time.time()
    result = fib(35)
    end_time = time.time()
    
    print(f"fib(35) = {result}")
    print(f"Time taken: {end_time - start_time:.6f} seconds")
    
    # Calculate it again to demonstrate caching
    start_time = time.time()
    result = fib(35)
    end_time = time.time()
    
    print(f"fib(35) = {result} (cached)")
    print(f"Time taken: {end_time - start_time:.6f} seconds")