count = 1
while count < 4:
        print('looping')
        count += 1


count = 1

#print only odd numbers
while count < 10:
        if count % 2 == 0:
            count += 1
            #break    #one the statement is met, it will exit
            continue #one the statement is met, it will continue back
                     #and not execute the statement after
        print(f"We're counting odd numbers: {count}")
        count += 1