class Role(object):

    def __init__(self, health, magic, choice):
        self.health = health
        self.magic = magic
        self.choice = choice

class Warrior(Role):
    weapon = 'shield'
    title = 'The Brave'

    def __init__(self):
        super(Warrior, self).__init__(200, 50,  0)


class Priest(Role):
    weapon = 'staff'
    title = 'The Healing'

    def __init__(self):
        super(Priest, self).__init__(100, 200, 0)

class Rouge(Role):
    weapon = 'daggers'
    title = 'The Quick'

    def __init__(self):
        super(Rouge, self).__init__(150, 30, 0)

class Hunter(Role):
    weapon = 'bow'
    title = 'The Swift'

    def __init__(self):
        super(Hunter, self).__init__(125, 100, 0)


def role_selection():

    warrior = Warrior()
    priest = Priest()
    rouge = Rouge()
    hunter = Hunter()

    roles = [warrior, priest, rouge, hunter]

    print "What class is best for you?"
    prot = raw_input("Do you like protecting your friends? (y/n) => ")
    if prot.lower() == 'y':
        warrior.choice += 1
        priest.choice += 2

    max_choice = 0

    for role in roles:
        if role.choice > max_choice:
            max_choice = role.choice

    return [r for r in roles if r.choice == max_choice][0]

    # elif prot == 'no' or prot == 'No':
    #     Rouge.choice += 1
    # else:
    #     print "Fine, don't answer."
    #     Hunter.choice += 2

    # print "Do you like being a leader?"
    # lead = raw_input()
    # if lead == 'yes' or lead == 'Yes':
    #     Warrior.choice += 1
    # elif lead == 'no' or lead == 'No':
    #     Hunter.choice += 1
    # else:
    #     print "Fine, don't answer."

    # print "Do you like being in the backgRound?"
    # back = raw_input()
    # if back == 'yes' or back == 'Yes':
    #     Rouge.choice += 1
    #     Hunter.choice += 2
    # elif back == 'no' or back == 'No':
    #     Priest.choice += 1
    # else:
    #     print "Fine, don't answer."

    # print "Do you like dealing damage up close?"
    # close = raw_input()
    # if close == 'yes' or close == 'Yes':
    #     Rouge.choice += 1
    #     Warrior.choice += 1
    # elif close == 'no' or close == 'No':
    #     Hunter.choice += 1
    #     Priest.choice += 1
    # else:
    #     print "Fine, don't answer."


    # print "Far away?"
    # distance = raw_input()
    # if distance == 'yes' or distance == 'Yes':
    #     Hunter.choice += 2
    #     Priest.choice += 1
    # elif distance == 'no' or distance == 'No':
    #     Rouge.choice += 1
    #     Warrior.choice += 1
    # else:
    #     print "Fine, don't answer."
    #     Warrior.choice += 1

    # print "Do you like working alone?"
    # alone = raw_input()
    # if alone == 'yes' or alone == 'Yes':
    #     Rouge.choice += 2
    #     Hunter.choice += 1
    #     Warrior.choice -= 1
    # elif alone == 'no' or alone == 'No':
    #     Priest.choice += 2
    # else:
    #     print "Fine, don't answer."
        
    # print "Do you like wearing heavy, medium or light armor?"
    # armor = raw_input()
    # if armor == 'heavy' or armor == 'Heavy':
    #     Warrior.choice += 3
    # elif armor == 'medium' or armor == 'Medium':
    #     Rouge.choice += 3
    #     Hunter.choice += 3
    # else:
    #     Priest.choice += 3

    # print "Do you like swords, magic or bows?"
    # weapon = raw_input()
    # if weapon == 'swords' or weapon == 'Swords' or weapon == 'sword' or weapon == 'Sword':
    #     Warrior.choice += 2
    #     Rouge.choice += 2
    # elif weapon == 'magic' or weapon == 'Magic':
    #     Priest.choice += 2
    # else:
    #     Hunter.choice += 2

    # # Going to implement later
    # #print "What is your favorite color?"
    # #color = raw_input()

    # role = {'Warrior': Warrior.choice, 'Priest': Priest.choice, 'Hunter': Hunter, 'Rouge': Rouge}

    # character =  max(role.iteritems(), key=operator.itemgetter(1))[0]

    # character = character.capitalize() 

    # print "Your class is " + character

    # print "What would you like to name your class?"
    # name = raw_input().capitalize()

    # print "\n" +  name + " the " + character.title

#print Role['Warrior']
#print Role['Rouge']
#print Role['Priest']
#print Role['Hunter']
