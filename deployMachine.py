#database

#Combo Skills (Name, Atk, Def, Agi, HP, Ninja Count, Trigger,  Boost Type)
ComboSkill[0]   = ('Konoha12Ninja', 10, 10, 10, 10, 12, False, 'All'     )
ComboSkill[1]   = ('FiveKage',      12, 12, 12, 12, 5,  False, 'All'     )
ComboSkill[2]   = ('Team7',         0,  0,  0,  0,  3,  True,  'Trigger' )


#Ninja name and Combo Skill registered to each one
ninja[0] = ('Naruto', (Konoha12Ninja), (Team7))
ninja[1] = ('Sasuke', (Konoha12Ninja), (Team7))
ninja[2] = ('Sakura', (Konoha12Ninja), (Team7))

def myNinja(inputNinja):
    #append user input to myNinja[]
    return

#Determining Priority Stat
def statPrio(inputPrio):
    inputPrio == ComboSkill[prio]
    return statPrio

#Optimizing Function
def optimize(myNinja[], statPrio, mainNinja[]):
    ninjaCount = 0
    result = []

    while ninjaCount < 15 :
        doEntryCheck()
        findBestComboSkills()
        priorityCheck()

    return result

#Printing Result
def finalResult():
    print(result[0-14])
