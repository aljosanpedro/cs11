def main():
    print(flatten([[1,2],[3,4]]))


def flatten(L):
    flat = []
    
    for i in range(len(L)):
        for j in range(len(L[i])):
            flat.append(L[i][j])
    
    return flat


main()