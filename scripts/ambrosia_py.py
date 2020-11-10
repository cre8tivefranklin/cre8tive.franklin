#class with food and nutrients

def food():
    class rec_alg:
        def __init__(self, n1):
            self.n1 = n1
            
    nutrients = rec_alg(['citrus','sodium','carotene','magnesium','potassium','protein','carbohydrates'])
    print(" Here's a list of nutrients \n ")
    for n in nutrients.n1:
        print(n)

    nutri_choice = input("\n What's your choice of nutrition? \n")
    nutrients.n1[0] = ['orange','lemon','lime \n']
    nutrients.n1[3] = ['carrots']
    if nutri_choice == 'citrus':
        for n in nutrients.n1[0]:
            print(n, " It's a very rich source of citrus which is also good for your immune system")
            food()
    elif nutri_choice == 'carotene':
        for n in nutrients.n1[3]:
            print(n)
            food()
    else:
        print('Please select an option')
        food()
    print('Feel free to pick more options, just type food()')
                
        

food()
