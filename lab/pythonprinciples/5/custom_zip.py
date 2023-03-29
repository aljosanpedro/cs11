"""
zip returns an iterable of tuples alternating from iter1 to iter2
ex. [(0, 5), (1, 6), (2, 7), (3, 8)]
resulting iter MUST be converted to some iter (ex. list,tuple)

# zipped_list = zip(list1,list2)
# return list(zipped_list)
"""

def main():
    print(zap([1,2,3,4],[5,6,7,8]))

    
def zap(list1,list2):
    zipped_list = []

    if not len(list1) == len(list2):
        return

    for index in range(len(list1)):
        element1,element2 = list1[index],list2[index]
        zipped_elements = (element1,element2)
        
        zipped_list.append(zipped_elements)
    
    return zipped_list

    
main()
