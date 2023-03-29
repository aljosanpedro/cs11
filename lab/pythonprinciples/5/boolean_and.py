def main():
    print(triple_and(True,True,True))
    
    
def triple_and(bool1,bool2,bool3):
    are_all_true = False
    
    if (bool1 and bool2 and bool3) is True:
        are_all_true = True
    
    return are_all_true
    

main()
