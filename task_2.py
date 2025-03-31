import re
from typing import Callable, Generator


def generator_numbers(text: str) -> Generator[float, None, None]:

    pattern = r'\b(\d+\.\d+|\d+)\b'
    
  
    for match in re.finditer(pattern, text):
      
        matched_num = match.group(1)
        
     
        yield float(matched_num)


def sum_profit(text: str, func: Callable) -> float:

    # Use the generator to get all numbers and sum them
    total = sum(func(text))
    return total



if __name__ == "__main__":
    text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")
    print("Знайдені числа:")
    for number in generator_numbers(text):
        print(number)