f = open('ingredients_1.csv', 'r').read().splitlines()
rows = [x.split(',') for x in f[1:len(f)]]
multipliers = [x[1:len(x)] for x in rows]
ingredients = [x[0] for x in rows]
measures = [x.replace(' ', '') for x in f[0].split(',')[1:len(f[0])]]

convert = {}
for i, ingredient in enumerate(ingredients):
  convert[ingredient] = {}
  for j, measure in enumerate(measures):
    convert[ingredient][measure] = float(multipliers[i][j])

ingredient = input("What ingredient do you want to convert to grams?\n")
while (not ingredient in convert):
  print("Not an ingredient... Try Again")
  ingredient = input("What ingredient do you want to convert to grams?\n")

measure = input('Are you converting, cup(s), tbsp, tsp, oz or lb?\n')
while (not measure in convert[ingredient]):
  print("Not a measure... Try Again")
  measure = input('Are you converting, cup(s), tbsp, tsp, oz or lb?\n')

amount = input('How many ' + measure + ' are you converting?\n')

print(float(amount) * float(convert[ingredient][measure]))
