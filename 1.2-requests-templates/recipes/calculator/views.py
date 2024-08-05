from django.shortcuts import render
from copy import deepcopy

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
def calculate_view(request, recipe_name):
    # Проверка существования рецепта
    if recipe_name not in DATA:
        return render(request, 'calculator/404.html', status=404)

    # Клонирование данных рецепта
    recipe = deepcopy(DATA[recipe_name])
    servings = request.GET.get('servings', 1)

    try:
        servings = int(servings)
        if servings <= 0:
            raise ValueError
    except ValueError:
        return render(request, 'calculator/400.html', status=400)

    # Умножение ингредиентов на количество порций
    for ingredient, amount in recipe.items():
        recipe[ingredient] = amount * servings

    context = {
        'recipe_name': recipe_name,
        'recipe': recipe
    }
return render(request, 'calculator/dishes.html', context)


def home_view(request):
    all_recipes = list(DATA.keys())
    context = {'all_recipes': all_recipes}
    return render(request, 'calculator/index.html', context)