
def recipe_algorithm():
    
    def flavor_input():
        #the flavor variable is assigned an array of different flavors
        flavor = ['salty','sweet','bitter','zesty','tart','spicy','juicy','bland',
            'plain','peppery']
        print('Here is a list of different flavors')
        print(flavor)
        print('Which flavor(s) do you enjoy most?\n input one by one')
        prompt_flavor = input()
        if prompt_flavor == flavor[0]:
            print('Salty? I see...')
        if prompt_flavor == flavor[1]:
            print('Sweet? SWEET!')
        
        
        prompt_texture = input('What kind of texture do you prefer?\n')
        texture = ['chewy','tender','flaky','hard','soft','moist','dry']
        
        prompt_nutrition = input('What kind of nutrition do you need?\n')        
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
