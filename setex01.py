# Example of a set
#  unique elements
# https://www.w3schools.com/python/python_sets.asp
#  https://pythontic.com/containers/set/construction_using_braces
# Disadvantage that cannot be empty
#  https://stackoverflow.com/questions/17373161/use-curly-braces-to-initialize-a-set-in-python
carmakers = { 'Nissan', 'Toyota', 'Ford', 'Mercedes' }
carmakers.add('Kia')
for comp in carmakers:
    print(comp)