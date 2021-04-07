def student_func(x):
    x = x.replace(" ", "")
    x = x.lower()
    if ( len(x) % 2 == 1 ):
        idx = len(x) // 2
        str1 = x[:idx]
        str2 = x[idx+1:]
        str2 = str2[::-1]
        if ( str1 == str2 ):
            return True
        else:
            return False
    else:
        idx = len(x) // 2
        str1 = x[:idx]
        str2 = x[idx:]
        str2 = str2[::-1]
        if ( str1 == str2 ):
            return True
        else:
            return False
        

# print(student_func("a"))
# print(student_func("RaCeCaR"))
# print(student_func("apple"))

from bwsi_grader.python.palindrome import grader
grader(student_func)

