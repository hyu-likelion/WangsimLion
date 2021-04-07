# make sure to execute this cell so that your function is defined
# you must re-run this cell any time you make a change to this function

def student_func(x):
    # `x` is a string
    # this function should return either `True` or `False`
    
    # write your code here
    # be sure to include a `return` statement so that
    # your function returns the appropriate object.
    a=x.replace(' ','')
    a=a.lower()
    return(a==a[::-1])




from bwsi_grader.python.palindrome import grader
grader(student_func)    