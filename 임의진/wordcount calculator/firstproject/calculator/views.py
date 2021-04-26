from django.shortcuts import render

# Create your views here.

def main(request) :
    return render(request, 'calculator/main.html')

def calculator(request) :
    expression=request.GET['expression']
    result = eval(expression)
    return render(request, 'calculator/calculator.html', {'result' : result})