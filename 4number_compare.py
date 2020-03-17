def number_compare(a, b):
    """Report on whether a>b, b>a, or b==a
    
        >>> number_compare(1, 1)
        'Numbers are equal'
        
        >>> number_compare(-1, 1)
        'Second is greater'
        
        >>> number_compare(1, -2)
        'First is greater'
    """
    
    greater = "First" if a > b else "Second"

    return "Numbers are equal" if a == b else f"{greater} is greater"

print(number_compare(3,2))