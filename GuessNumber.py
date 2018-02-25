secret = 42
guess = 0
tries = 0

# for tries in range(2):
    while guess != secret:
        print "Pokusaj broj %d " % (tries + 1)
        guess = raw_input("Type a number: ")
        if guess.isdigit():
            tries += 1
            if int(guess) == secret:
                print "Correct!"
                tries = 0
                print "Number of tries was reset to %d" % tries
                break
            elif int(guess) < secret:
                again = raw_input("Incorrect, your number is too small. Try again (y/n)? ").lower()
                if again == 'n':
                    break
            elif int(guess) > secret:
                again = raw_input("Incorrect, your number is too big. Try again (y/n)? ").lower()
                if again == 'n':
                    break
        else:
            print "This is not a valid number, try again"
