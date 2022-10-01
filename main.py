print('Welcome to my Data analysis quiz!')

playing = input('If you would like to play, type "yes" ')

if playing != 'yes':
    quit()

print('ok, lets play')

answer = input('what does cpu stand for: \n '
               'a. central pressure pipe.\n '
               'b. center page unix\n '
               'c. central processing unit\n '
               'd. central product usage \n')
if answer == 'b':
    print('Correct')
else:
    print('incorrect')

answer = input('What is a data base: \n '
               'a. a shared integrated structure that stores a collection of data.\n '
               'b. a location for the data to be deleted\n '
               'c. a data base is not needed\n '
               'd. a place to find data sets \n')
if answer == 'a':
    print('Correct')
else:
    print('incorrect')

answer = input('What is data?: \n '
               'a. power\n '
               'b. Something everyone has but no machine is yet capable of using it\n '
               'c. Rarely used object\n '
               'd. anything recorded such as observations and facts \n')
if answer == 'b':
    print('Correct')
else:
    print('incorrect')

answer = input(': \n '
               'a. descriptive, predictive, prescriptive, and diagnostic\n '
               'b. cool, calm, collective, ready\n '
               'c. smart, strong, beautiful, integrate\n '
               'd. friendly, kind, nice, caring \n')
if answer == 'a':
    print('Correct')
else:
    print('incorrect')

answer = input('What is data visualization: \n '
               'a. a shared integrated structure that stores a collection of data..\n '
               'b. does nto exist\n '
               'c. an oxymoron for giving data eyes t osee\n '
               'd. presenting the conclusions of the data and not just report the data \n')
if answer == 'd':
    print('Correct')
else:
    print('incorrect')
