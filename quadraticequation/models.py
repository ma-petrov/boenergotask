from math import sqrt, modf
from django.db import models

from .utils import Bunch

class Equation(models.Model):
    """
    Model represents history of solved equations
    """

    a = models.FloatField()
    b = models.FloatField()
    c = models.FloatField()

    roots_num = models.PositiveIntegerField()
    root_1 = models.FloatField(null=True)
    root_2 = models.FloatField(null=True)

    @classmethod
    def solve(cls, a, b, c):
        """
        Function solves equation
        """

        roots_num, root_1, root_2 = 0, None, None

        if a != 0:
            discriminant = b**2 - 4*a*c
            if discriminant == 0:
                roots_num = 1
                root_1 = round(-(b/(2*a)), 10)
            elif discriminant > 0:
                roots_num = 2
                root_1 = round((-b - sqrt(discriminant))/(2*a), 10)
                root_2 = round((-b + sqrt(discriminant))/(2*a), 10)
        else:
            roots_num = 1
            if b != 0:
                root_1 = -c/b
            elif c == 0:
                roots_num = 4

        cls.objects.create(a=a, b=b, c=c, roots_num=roots_num, root_1=root_1, root_2=root_2)
        return cls.objects.last()

    def render_equation(self):
        def render_num(x):
            if modf(x)[0] == 0:
                return str(int(abs(x)))
            else:
                return str(abs(x))

        if self.a < 0:
            sign_a = '- '
            a = f'{render_num(self.a)} * x^2 '
        elif self.a > 0:
            sign_a = ''
            a = f'{render_num(self.a)} * x^2 '
        else:
            sign_a = ''
            a = ''

        if self.b < 0:
            sign_b = '- '
            b = f'{render_num(self.b)} * x '
        elif self.b > 0:
            if self.a != 0:
                sign_b = '+ '
            else:
                sign_b = ''
            b = f'{render_num(self.b)} * x '
        else:
            sign_b = ''
            b = ''

        if self.c < 0:
            sign_c = '- '
            c = f'{render_num(self.c)} '
        elif self.c > 0:
            if self.a != 0 or self.b != 0:
                sign_c = '+ '
            else:
                sign_c = ''
            c = f'{render_num(self.c)} '
        else:
            sign_c = ''
            c = ''

        if self.a != 0 or self.b != 0 or self.c != 0:
            noght = ''
        else:
            noght = '0 * x^2 + 0*x '

        return f'{sign_a}{a}{sign_b}{b}{sign_c}{c}{noght}= 0'

    def render_solution(self):
        def render_num(x):
            if modf(x)[0] == 0:
                return str(int(x))
            else:
                return str(round(x, 5))

        if self.roots_num == 0:
            return 'Нет корней'
        elif self.roots_num == 1:
            return f'Один корень: {render_num(self.root_1)}'
        elif self.roots_num == 2:
            return f'Два корня: {render_num(self.root_1)}, {render_num(self.root_2)}'
        elif self.roots_num == 4:
            return 'Бесконечное кол-во корней'
        else:
            return 'Некорректные данные'
