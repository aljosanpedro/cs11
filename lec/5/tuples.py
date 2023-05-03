from list_methods import A, words, s1

# normally, tuples should be declared w/ more than 1 elem
# BUT! you can make tuples with 1 elem, just add a comma at the end

tup = ("t",)
print(type(tup)) # class tuple

# can actually "replace" stuff in a tuple, BUT by making a new tuple

A = tuple(A)

A = (2,) + A[1:] # new tuple (1 elem, w/ commma), THEN added the rest of the tuple EXCEPT first
print(A)

