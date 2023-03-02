items = []

print('welcome to game')
name = input('what is your name? ')

health = 10

left_or_right = input('firt choice... Left or right (left/right)? ')
if left_or_right == 'left':
    ans = input('reachd a lake, swim across or go around (across/around)? ')
    if ans == 'around':
        print('you went around and reached the other side of the lake ')
    elif ans == 'across':
        print('you managed to get across, but you were bit by a fish and lost 5 health.')
        health -= 5

    ans = input('you notice a house and a river. which do you go to? (river/house)? ')
    if ans == 'house':
        print('you go to the house and were greeted by the owner... the owner hit you and you lost 5 health ')
        health -= 5

        if health <= 0:
            print('you now have 0 health and have lost the game ')
        else:
            print('you have survived')

        weapon = input('now you must pick up sword weapon (take)')
        if weapon == 'take':
            items.append(weapon)
            print ('now you must carry on and go to the forrest')
      

    else:
        print('you fell in water and lost.')

else:
    print('you fell and lost')




