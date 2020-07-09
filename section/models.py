from django.db import models


class AbstractAnimalModel(models.Model):
    """Абстрактный класс животного"""
    date_created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания',
        help_text='Введите дату создания',
        editable=False,
        null=True,
    )

    name = models.CharField(
        max_length=40,
        verbose_name='Название животного'
    )

    animal_name = models.CharField(
        max_length=40,
        verbose_name='Имя',
        null=True
    )

    date_birthday = models.DateField(
        auto_created=True,
        verbose_name='Дата рождения'
    )

    class Meta:
        abstract = True


class AbstractAccountingModel(models.Model):
    """Абстрактный класс учета"""


    growth = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        verbose_name='Рост',
        help_text='Измеряется в см.'
    )
    weight = models.DecimalField(
        max_digits=20,
        decimal_places=3,
        verbose_name='Вес',
        help_text='Измеряется в кг.'
    )
    date_created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания',
        editable=False,
        null=True,
    )

    class Meta:
        abstract = True


class ShaggyAnimal(AbstractAnimalModel):
    """Мохнатые зверушки"""

    count_teeth = models.IntegerField(verbose_name='Количество зубов')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Мохнатый зверь'
        verbose_name_plural = 'Мохнатые зверушки'


class ShaggyAccounting(AbstractAccountingModel):
    """Учет мохнатых"""

    animal = models.ForeignKey(ShaggyAnimal, on_delete=models.CASCADE, verbose_name='Животное')

    def __str__(self):
        return f"{self.animal.animal_name} | {self.animal} | {self.growth}см. | {self.weight}кг."

    class Meta:
        verbose_name = 'Учет мохнатых'
        verbose_name_plural = 'Учет мохнатых'


class WaterfowlAnimal(AbstractAnimalModel):
    """Водоплавающие"""

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Водоплавающий зверь'
        verbose_name_plural = 'Водоплавающие звери'


class WaterfowlAccounting(AbstractAccountingModel):
    """Учет водоплавающих"""
    animal = models.ForeignKey(WaterfowlAnimal, on_delete=models.CASCADE, verbose_name='Животное')

    def __str__(self):
        return f"{self.animal.animal_name} | {self.animal} | {self.growth}см. | {self.weight}кг."

    class Meta:
        verbose_name = 'Учет водоплавающих'
        verbose_name_plural = 'Учет водоплавающих'


class FlyingAnimal(AbstractAnimalModel):
    """Летающие"""

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Летающий зверь'
        verbose_name_plural = 'Летающие звери'


class FlyingAccounting(AbstractAccountingModel):
    """Учет летающих"""
    animal = models.ForeignKey(FlyingAnimal, on_delete=models.CASCADE, verbose_name='Животное')

    def __str__(self):
        return f"{self.animal.animal_name} | {self.animal} | {self.growth}см. | {self.weight}кг."

    class Meta:
        verbose_name = 'Учет летающих'
        verbose_name_plural = 'Учет летающих'


class CreepingAnimal(AbstractAnimalModel):
    """Ползучий"""

    patronymic = models.CharField(max_length=60, verbose_name='Отчество')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ползучий зверь'
        verbose_name_plural = 'Ползучие звери'


class CreepingAccounting(AbstractAccountingModel):
    """Учет Ползучих"""
    animal = models.ForeignKey(CreepingAnimal, on_delete=models.CASCADE, verbose_name='Животное')

    def __str__(self):
        return f"{self.animal.animal_name} | {self.animal} | {self.growth}см. | {self.weight}кг."

    class Meta:
        verbose_name = 'Учет ползучих'
        verbose_name_plural = 'Учет ползучих'
