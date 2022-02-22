f = open('ingredients_1.1.csv', 'r').read().splitlines()
rows = [x.split(',') for x in f[1:len(f)]]
multipliers = [x[1:len(x)] for x in rows]
ingredients = [x[0] for x in rows]
measures = [x.replace(' ', '') for x in f[0].split(',')[1:len(f[0])]]
calories = [x[-1] for x in rows]


cups = ['cup', 'cups', 'cup(s)', 'c']
tbsp = ['tbsp', 'tbspn', 'tbsps', 'tablespoon', 'tablespoons', 'tbspoon', 'tbspoons', 'tbs']
tsp = ['tsp', 'tspn', 'tsps', 'teaspoon', 'teaspoons', 'tspoon', 'tspoons']
oz = ['oz', 'ozs', 'ounce', 'ounces']
lb = ['lb', 'lbs', 'pound', 'pounds']

convert = {}
for i, ingredient in enumerate(ingredients):
  convert[ingredient] = {}
  for j, measure in enumerate(measures):
    convert[ingredient][measure] = float(multipliers[i][j])
print('Hello! Please read carefully and enter the ingredient you wish to convert to grams. \nif it returns an error'
      ' please try again!\nNOTE: If you are measuring eggs, all measurements refer to 1 egg')
end = 0
recipe_list = {}
calorie_count = 0

while end == 0:
  ingredient = input("What ingredient do you want to convert to grams?\n")
  if ingredient == 'print':
    print(recipe_list)
    print('the ingredient(s) / recipe contain ' + str(calorie_count) + ' calories!')
    break
  while not ingredient.lower() in convert:
    print("Not an ingredient... Try Again")
    ingredient = input("What ingredient do you want to convert to grams?\n")

  measure = input('Are you converting, cup(s), tbsp, tsp, oz or lb?\n')
  amount = input('How many ' + measure + ' are you converting?\n')

  if measure.lower() in cups:
    print(float(amount) * float(convert[ingredient.lower()]['cup(s)']))
    recipe_list[ingredient] = (float(amount) * float(convert[ingredient.lower()]['cup(s)']))
    calorie_count += ((float(amount) * float(convert[ingredient.lower()]['cup(s)'])) / 100) * \
    float(convert[ingredient]['calories/100g'])
  if measure.lower() in tbsp:
    print(float(amount) * float(convert[ingredient.lower()]['tbsp']))
    recipe_list[ingredient] = (float(amount) * float(convert[ingredient.lower()]['tbsp']))
    calorie_count += ((float(amount) * float(convert[ingredient.lower()]['tbsp'])) / 100) * \
    float(convert[ingredient.lower()]['calories/100g'])
  if measure.lower() in tsp:
    print(float(amount) * float(convert[ingredient.lower()]['tsp']))
    recipe_list[ingredient] = (float(amount) * float(convert[ingredient.lower()]['tsp']))
    calorie_count += ((float(amount) * float(convert[ingredient.lower()]['tsp'])) / 100) * \
    float(convert[ingredient.lower()]['calories/100g'])
  if measure.lower() in oz:
    print(float(amount) * float(convert[ingredient.lower()]['oz']))
    recipe_list[ingredient] = (float(amount) * float(convert[ingredient.lower()]['oz']))
    calorie_count += ((float(amount) * float(convert[ingredient.lower()]['oz'])) / 100) * \
    float(convert[ingredient.lower()]['calories/100g'])
  if measure.lower() in lb:
    print(float(amount) * float(convert[ingredient.lower()]['lb']))
    recipe_list[ingredient] = (float(amount) * float(convert[ingredient.lower()]['lb']))
    calorie_count += ((float(amount) * float(convert[ingredient.lower()]['lb'])) / 100) * \
    float(convert[ingredient.lower()]['calories/100g'])
