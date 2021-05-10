
# make sure to execute this cell so that your function is defined
# you must re-run this cell any time you make a change to this function

def student_func(x):
    # write your code here
    # be sure to include a `return` statement so that
    # your function returns the appropriate object.
    three=x%3
    five=x%5

    if three==0 and five==0 :
        return('threefive')
    elif three==0 and five>0 :
        return('three')
    elif three>0 and five==0 :
        return('five')
    else :
        return(x)

    pass


# Execute this cell to grade your work
from bwsi_grader.python.three_five import grader
grader(student_func)