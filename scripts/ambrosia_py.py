
def food_data():
    #the following variables are arrays of different flavors textures and
    #nutrients in food
    #flavor[0] is the subset of 0 in the flavor array containing the words
    #to describe acerbic flavors
    
    flavor =['salty', 'sweet', 'sour', 'bitter', 'umami']
    flavor[0] = ['beets', 'celery', 'carrots', 'spinach', 'chard', 'meat']
    
    texture  = ['crisp','tender','soft']
    
    nutrients = ['sodium','potassium','magnesium','protein','sugar']

    #some indices in the arrays above are assigned arrays of values
    #nutrients[3] is an array of the different types of proteins that
    #exist in food
    nutrients[3] = ['whey','gluten','soy']
    

    def food_int():    
        flav_int = input('What kind of flavor do you enjoy?\n')
        if flav_int == 'salty':
            print('I recommend the following veggies\n', *flavor[0], '\nEach of these are rich in sodium')
            flav_choice = input('Whcih do think you''d enjoy most?\n')
            if flav_choice == 'beets' or 'carrots':
                print('Nice! \n', 'You should try making a salad out of this!')
        elif flav_int == flavor[6]:
                print('aromatic chickden is my recomdation')        
    food_int()

food_data()
