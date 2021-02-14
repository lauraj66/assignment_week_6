#define the function
def conversion_funtion () :
    try:
    #prompt user for miles driven
        miles = float(input('How many miles did you drive? : '))
        kilometers = float(miles*1.609)
        print('You have driven', miles,'miles, which is', kilometers,'kilometers!')    
    #except user may not use numbers
    except (ValueError) :
        print('Please enter miles as a number.')
#call the function
conversion_funtion ()