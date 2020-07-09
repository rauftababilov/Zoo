from django.contrib import admin
from .models import (
    CreepingAnimal,
    CreepingAccounting,
    FlyingAnimal,
    FlyingAccounting,
    ShaggyAnimal,
    ShaggyAccounting,
    WaterfowlAnimal,
    WaterfowlAccounting
)


@admin.register(CreepingAnimal)
class CreepingAnimalAdmin(admin.ModelAdmin):
    list_display = ('animal_name', 'name', 'patronymic', 'date_birthday')


@admin.register(CreepingAccounting)
class CreepingAccountingAdmin(admin.ModelAdmin):
    @staticmethod
    def get_animal_name(obj):
        return obj.animal.animal_name

    list_display = ('get_animal_name', 'animal', 'growth', 'weight', 'date_created')


@admin.register(FlyingAnimal)
class FlyingAnimalAdmin(admin.ModelAdmin):
    list_display = ('animal_name', 'name', 'date_birthday')


@admin.register(FlyingAccounting)
class FlyingAccountingAdmin(admin.ModelAdmin):
    @staticmethod
    def get_animal_name(obj):
        return obj.animal.animal_name

    list_display = ('get_animal_name', 'animal', 'growth', 'weight', 'date_created')


@admin.register(ShaggyAnimal)
class ShaggyAnimalAdmin(admin.ModelAdmin):
    list_display = ('animal_name', 'name', 'date_birthday', 'count_teeth')


@admin.register(ShaggyAccounting)
class ShaggyAccountingAdmin(admin.ModelAdmin):
    @staticmethod
    def get_animal_name(obj):
        return obj.animal.animal_name
    list_display = ('get_animal_name', 'animal', 'growth', 'weight', 'date_created')


@admin.register(WaterfowlAnimal)
class WaterfowlAnimalAdmin(admin.ModelAdmin):
    list_display = ('animal_name', 'name', 'date_birthday',)


@admin.register(WaterfowlAccounting)
class WaterfowlAccountingAdmin(admin.ModelAdmin):
    @staticmethod
    def get_animal_name(obj):
        return obj.animal.animal_name
    list_display = ('get_animal_name', 'animal', 'growth', 'weight', 'date_created')

