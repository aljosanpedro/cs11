def validate(code):
    if "def" not in code:
        return "missing def"
    
    if ":" not in code:
        return "missing :"
    
    if "(" not in code or ")" not in code:
        return "missing paren"
    
    if "(" + ")" in code:
        return "missing param"
    
    if "    " not in code:
        return "missing indent"
    
    if "validate" not in code:
        return "wrong name"
    
    if "return" not in code:
        return "missing return"
        
    return True

"""
def validate(code):
    criteria_to_error = {
        "def"      : "missing def",
        ':'        : "missing :",
        '(' + ')'  : "missing param",
        "   "      : "missing indent",
        "validate" : "wrong name",
        "return"   : "missing return",
    }
    
    for criterion in criteria_to_error:
        if criterion not in code:
            error = criteria_to_error[criterion]
            return error
            
    if '(' not in code or ')' not in code:
        return "missing paren"
            
    return True
"""