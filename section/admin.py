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
    list_display = ('name', 'patronymic', 'date_birthday')


@admin.register(CreepingAccounting)
class CreepingAccountingAdmin(admin.ModelAdmin):
    list_display = ('animal', 'growth', 'weight', 'date_created')


@admin.register(FlyingAnimal)
class FlyingAnimalAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_birthday')


@admin.register(FlyingAccounting)
class FlyingAccountingAdmin(admin.ModelAdmin):
    list_display = ('animal', 'growth', 'weight', 'date_created')


@admin.register(ShaggyAnimal)
class ShaggyAnimalAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_birthday', 'count_teeth')


@admin.register(ShaggyAccounting)
class ShaggyAccountingAdmin(admin.ModelAdmin):
    list_display = ('animal', 'growth', 'weight', 'date_created')


@admin.register(WaterfowlAnimal)
class WaterfowlAnimalAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_birthday',)


@admin.register(WaterfowlAccounting)
class WaterfowlAccountingAdmin(admin.ModelAdmin):
    list_display = ('animal', 'growth', 'weight', 'date_created')

