from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'main.html')

def calculator(request):
    input_ = request.GET['input']
    result = eval(input_)
    return render(request, 'calculator.html',{'result': result} )