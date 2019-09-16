
def recipe_algorithm():
    
    def flavor_input():
        #use combinatorics to find combinations of all flavors
        flavor = ['salty','sweet','bitter','zesty','tart','spicy','juicy','bland',
            'plain','peppery']
        print('Here is a list of different flavors')
        print(flavor)
        print('Input your favorite one at a time')
        prompt_flavor = input()
        if prompt_flavor == flavor[0] or flavor [1] or flavor[2] or flavor[3] or flavor[4] or flavor[5] or flavor[6] or flavor[7] or flavor[8]:
            print("So " + prompt_flavor )
        else:
            print('type one of the options please!')
        
        prompt_texture = input('What kind of texture do you prefer?\n')
        texture = ['chewy','tender','flaky','hard','soft','moist','dry']
        
        prompt_nutrition = input('What kind of nutrition do you need\n?')        
        nutrition = ['protein','sodium','magnesium','potassium','sugar','citrus']
        

        #the array for various protein types
        nutrtion[0] = ['gluten','whey','soy']

        #the arrays of different veggies and their families
        veggie_family = ['alliums','brassica']
        veggie_family[0] = ['chives','garlic','leeks','onions','shallots']
        veggie_family[1] = ['cauliflower','broccoli','brussel sprouts','cabbage','kale','kohlrabi','rutabaga','turnips',
		'mustard greens']

        
        #if prompt_flavor == flavor[0]:
            #print('So you like salty food?')
        
    flavor_input()

recipe_algorithm()
