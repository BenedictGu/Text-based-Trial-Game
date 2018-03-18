import os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class Player:
    def __init__(self):
        self.location = None
        self.evidences = []
        self.alive = True
        self.credibility = 100
        self.penalty = -20
        self.showCred = False
        self.skip = False
        self.coins = 0
        self.props = []
    def goDirection(self, direction):
        self.location = self.location.getDestination(direction)
    def pickup(self, evid):
        self.evidences.append(evid)
        evid.loc = self
        self.location.removeEvidence(evid)
        return evid
    def showInventory(self):
        clear()
        print('You have ' + str(self.coins) + ' coins.\n')
        print("You currently have these evidences:")
        j = 1
        for e in self.evidences:
            print(str(j)+".", e.name)
            j += 1
        print()
        print('You have the following props:')
        j = 1
        for p in self.props:
            print(str(j) + ". ", p.name)
        print()
        input("press enter to continue...")
    def consume(self, n):
        self.props[n-1].ability(self)


class Shop:
    def __init__(self, player):
        self.merchandise = [CP]
        self.player = player
    def purchase(self, n):
        clear()
        merch = self.merchandise[n-1]
        if self.player.coins >= merch.COST:
            if len(self.player.props) < 10:
                print('You\'ve just purchased ' + merch.NAME + '! Cost ' + str(merch.COST) + 'coins!')
                self.player.props.append(merch())
                self.player.coins -= merch.COST
            else:
                print('Not enough bag space.')
        else:
            print('Not enough coins')
        input('press enter to continue...')
    def shopping(self):
        shopSucceed = False
        while not shopSucceed:
            clear()
            print("Welcome to the Shop! Purchase anything to your advance:")
            i = 1
            for m in self.merchandise:
                print(str(i) + '. ' + m.NAME + ' ' + '.'*(40-len(m.NAME)) + str(m.COST) + ' coins')
                i += 1
            print()
            choice = input('What do you want to buy? ')
            if choice.isnumeric():
                n = int(choice)
                if n > 0 and n <= len(self.merchandise):
                    self.purchase(n)
                    print('Purchase Successful!')
                else:
                    print('Invalid item!')
            elif choice == 'exit':
                shopSucceed = True
            elif choice == 'help':
                self.print_help()
            else:
                print('Invalid Command!')
    def print_help(self):
        clear()
        print('input <number of labeled before the merchandise> to purchase item.')
        print('input \'exit\' to leave the shop')
        input('press enter to continue...')

class Prop:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost
    def ability(self, p):
        print("This prop can't do anything!")

class CP(Prop):
    NAME = "Credibility Potion"
    COST = 10
    def __init__(self):
        Prop.__init__(self, CP.NAME, CP.COST)

    def ability(self, player):
        player.credibility += min(100, player.credibility + 10)
        clear()
        print("Credibility up 10 percents.")
        input('press enter to continue...')
