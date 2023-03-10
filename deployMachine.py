# Database

# Combo Skills (Name, Atk, Def, Agi, HP, Ninja Count, Trigger,  Boost Type)
ComboSkill[0]   = ('Konoha12Ninja', 10, 10, 10, 10, 12, False, 'All'     )
ComboSkill[1]   = ('FiveKage',      12, 12, 12, 12, 5,  False, 'All'     )
ComboSkill[2]   = ('Team7',         0,  0,  0,  0,  3,  True,  'Trigger' )


# Ninja name and Combo Skill registered to each one
ninja[0] = ('Naruto', (Konoha12Ninja), (Team7))
ninja[1] = ('Sasuke', (Konoha12Ninja), (Team7))
ninja[2] = ('Sakura', (Konoha12Ninja), (Team7))

def myNinja(inputNinja):
    # Append user input to myNinja[]
    myNinja = []
    myNinja.append(inputNinja)
    return ?

# Checks whether the combo skill is already in result[]
def doEntryCheck(currentComboSkill) :
    # cycle through result[] to find the corresponding comboSkill
    if comboSkill == result[] :
        return False
    
    elif comboSkill != result[] :
        return True

# Finds which combo skills yield the most stat gain
def findBestComboSkills() :
    # Sum all the stat gain attribute of combo skill object
    # Return the combo skills name

# Checks if the current combo skill has the priority stat the user chose
def priorityCheck(priorityStat) :
    # Find the stat name in the current combo skill
    if priorityStat == currentComboSkill[] :
        return False
    
    elif priorityStat != currentComboSkill[] :
        return True

# Optimizing Function
def optimize(myNinja[], statPrio, mainNinja[]) :
    ninjaCount = 0
    result = []

    while ninjaCount < 15 :
        doEntryCheck()
        findBestComboSkills()
        priorityCheck()

    result.append(potentialNinja[ninjaIndex[name]])
    
    return result

#Printing Result
def finalResult():
    print(result[])
