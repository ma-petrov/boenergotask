from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import EquationForm
from .models import Equation

def quadratic_equation(request):
    if request.method == 'POST':
        form = EquationForm(request.POST)
        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            c = form.cleaned_data['c']

            print(a)
            print(b)
            print(c)

            solution = Equation.solve(a, b, c)
            return render(request, 'solution.html', dict(solution=solution))
    else:
        form = EquationForm()

    context = dict(form=form, solutions=Equation.objects.all().order_by('-id')[:20])
    return render(request, 'quadratic_equation.html', context)

def solution(request):
    result = request.GET.get('result')
    context = dict(result=result)
    return render(request, 'quadratic_equation.html', context)
