def main():
    print(param_count())
    
    
"""
*args: pass any number of parameters
**kwargs: also pass any number of parameters, but in format "var = value"

note: "args" and "kwargs" are conventions
"""

def param_count(*args):
    return len(args)
    
    
main()
