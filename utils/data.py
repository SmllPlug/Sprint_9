from pathlib import Path


APP_DIR = Path(__file__).resolve().parent.parent

# Данные для логина
LOGIN_EMAIL = 'aa'
LOGIN_PASSWORD = 'asdasfasfasfsafas'

# Данные для рецепта
RECIPE_NAME = 'Вкусная рыба'
RECIPE_INGREDIENT_NAME = 'рыба'
RECIPE_INGREDIENT_WEIGHT = '250'
RECIPE_TIME = '20'
RECIPE_DESCRIPTION = 'Очень вкусная рыба'

# Путь к файлу
RECIPE_PIC_CATALOG = APP_DIR / 'assets' / 'fish.jpeg'