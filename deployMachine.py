# Database
# Global Variables
ninja       = list
comboSkill  = list
result      = list
mainNinja   = list
myNinja     = list
# Combo Skills (Name, Atk, Def, Agi, HP, Ninja Count, Trigger,  Boost Type)
comboSkill[0] = ['Konoha12Ninja', 10, 10, 10, 10, 12, False, 'All'     ]
comboSkill[1] = ['FiveKage',      12, 12, 12, 12, 5,  False, 'All'     ]
comboSkill[2] = ['Team7',         0,  0,  0,  0,  3,  True,  'Trigger' ]

# Ninja name and Combo Skill registered to each one
ninja[0] = ['Naruto', comboSkill[0], comboSkill[2]]
ninja[1] = ['Sasuke', comboSkill[0], comboSkill[2]]
ninja[2] = ['Sakura', comboSkill[0], comboSkill[2]]
ninja[3] = ['Gaara',  comboSkill[1]]
ninja[4] = ['Hinata', comboSkill[2]]

def addNinja(inputNinja):
    for i in len(ninja) :
        if inputNinja == ninja[i[0]] :
            myNinja.append(inputNinja)
            print(ninja[i[0]]+' added successfully')
            i += 1
        else :
            print('Ninja not found')
            break

def addMainNinja(inputMainNinja):
    for i in len(ninja) :
        if inputMainNinja == ninja[i[0]] :
            mainNinja.append(inputMainNinja)
            i += 1
        else :
            break

def getComboSkill(mainNinja) :
    searchString = []
    for i in mainNinja :
        for j in range(mainNinja[i[1]], mainNinja[i[max]]) :
            if mainNinja[i[j]] == comboSkill[j]:
                searchString.append()
                j += 1
        i += 1

# Checks whether the combo skill is already in result[]
def doEntryCheck(currentComboSkill) :
    # Cycle through result[] to find the corresponding comboSkill
    if currentComboSkill == result[] :
        return False
    
    else :
        return True
# Finds which combo skills yield the most stat gain
def findBestComboSkills() :
    if doEntryCheck() :
        return
    # Sum all the stat gain attribute of combo skill object
    # Return the combo skills name
    else : 
        return

# Checks if the current combo skill has the priority stat the user chose
def priorityCheck(priorityStat) :
    # Find the stat name in the current combo skill
    if priorityStat == currentComboSkill[] :
        return False
    
    elif priorityStat != currentComboSkill[] :
        return True

# Optimizing Function
def optimize(myNinja, statPrio, mainNinja) :

    while len(result) <= 15 :
        doEntryCheck()
        findBestComboSkills()
        priorityCheck()
        # BONUS: check if there's other combo skills with prioritised stat, if len(result) < 15
        result.append(potentialNinja[ninjaIndex[name]])
    
    return result

# Printing Result
def finalResult():
    print(result[])


