from random import choices
from django.db import models
from django.db.models import Count, F
from django.core.exceptions import ObjectDoesNotExist

class Color(models.Model):
    name = models.CharField(max_length=100)
    max_items = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.name}, max: {self.max_items}'

    @classmethod
    def get_max_items(cls):
        colors = cls.objects.values('name', 'max_items')
        return 'Предметы: ' + ', '.join([f'{c["name"]} - {c["max_items"]}' for c in colors])

class Item(models.Model):
    item_id = models.PositiveIntegerField()
    color = models.ForeignKey(Color, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.item_id}, color: ({self.color})'

    @classmethod
    def get_item_stat(cls):
        items = cls.objects.select_related('color').values('color__name').annotate(cnt=Count('item_id'))
        if items:
            return 'Найденные предметы: ' + ', '.join([f'{item["color__name"]} - {item["cnt"]}' for item in items])
        else:
            return 'Пока нет найденных предметов'
        
    @classmethod
    def guess_color(cls, item_id):
        if item_id >= 1 and item_id <= 100:
            if not cls.objects.filter(item_id__exact=item_id):

                max_items = {color['id']: color['max_items'] for color in Color.objects.values('id', 'max_items')}
                
                items = {k: 0 for k in max_items.keys()}
                for item in cls.objects.values('color').annotate(cnt=Count('item_id')):
                    items.update({item['color']: item['cnt']})

                colors_available = dict()
                for k in max_items.keys():
                    colors_available.update({k: max_items[k] - items[k]})
                
                total = sum([v for v in colors_available.values()])
                weights = [v/total for v in colors_available.values()]
                color_id = choices(population=list(colors_available.keys()), weights=weights)[0]

                cls.objects.create(item_id=item_id, color=Color(id=color_id))
            
            return cls.objects.select_related('color').values('color__name').get(item_id=item_id)['color__name']

        else:
            return 'Неверный номер предмета'

