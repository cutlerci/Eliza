import re

keywords = {
    "I": [0, "YOU", 0, [r"(.*)YOU\sARE\s([a-zA-Z ]*)(\.|\!)", 2,
                        r"WHY ARE YOU \2?",
                        r"IS IT BECAUSE YOU ARE \2 THAT YOU CAME TO ME?",
                        r"HOW LONG HAVE YOU BEEN \2?",
                        r"DO YOU BELIEVE IT IS NORMAL TO BE \2?"], [r"(.*)YOU\s(WANT|NEED)\s([a-zA-Z ]*)(\.|\!)", 2,
                                                                    r"WHAT WOULD IT MEAN TO YOU IF YOU GOT \3?",
                                                                    r"WHY DO YOU WANT \3?",
                                                                    r"SUPPOSE YOU GOT \3 SOON.",
                                                                    r"WHAT IF YOU NEVER GOT \3?",
                                                                    r"WHAT WOULD GETTING \3 MEAN TO YOU?",
                                                                r"WHAT DOES GETTING \3 HAVE TO DO WITH YOUR PROBLEM?"]],
    "NONE": [0, "NONE", 0, [r"(.*)", 2,
                            r"COULD YOU ELABORATE?",
                            r"I WOULD LOVE TO KNOW MORE.",
                            r"COULD YOU CLARIFY WHAT YOU MEAN?",
                            r"I DO NOT QUITE UNDERSTAND YOU FULLY.",
                            r"PLEASE CONTINUE.",
                            r"WHAT DOES THAT SUGGEST TO YOU?",
                            r"DO YOU FEEL STRONGLY ABOUT DISCUSSING SUCH THINGS?"]]
}
print("\n   Welcome to"
      "\n                    ______   ___      ____    ______    _______ "
      "\n                   |  ____|  | |      |  |   |___   |  | |   | |"
      "\n      ______       | |__     | |      |  |      /  /   | |___| |       ______ "
      "\n     |______|      |  __|    | |      |  |     /  /    |  ___  |      |______|"
      "\n                   | |____   | |___   |  |    /  /__   | |   | |"
      "\n                   |______|  |_____|  |__|   /______|  |_|   |_|"
      "\n\n   Eliza is a mock Rogerian psychotherapist."
      "\n   The original program was described by Joesph Weizenbaum in 1966."
      "\n   This implementation by Charles Cutler 2022.\n\n"
      "[ELIZA]: HELLO, MY NAME IS ELIZA. I WILL BE YOUR PSYCHOTHERAPIST. WHAT IS YOUR NAME?")

userName = (input("[...]: ")).upper()

parsedInput = []
keyStack = []
memoryStack = []
highestPriorityValueFound = 999
print("[ELIZA]: IT IS NICE TO MEET YOU " + userName + ". PLEASE TELL ME, WHAT IS WRONG?")

while True:
    userInput = input("[" + userName + "]: ")
    if userInput == "Thank you Eliza.":
        break

    parsedInput = userInput.split(" ")
    modifiableInput = parsedInput.copy()

    for word in parsedInput:
        if (("," in word) or ("." in word)) and (len(keyStack) == 0):
            indexOfAWordWithDelimiter = modifiableInput.index(word)
            while indexOfAWordWithDelimiter >= 0:
                modifiableInput.pop(indexOfAWordWithDelimiter)
                indexOfAWordWithDelimiter -= 1
        elif (("," in word) or ("." in word)) and (len(keyStack) >= 0):
            indexOfAWordWithDelimiter = modifiableInput.index(word) + 1
            while indexOfAWordWithDelimiter != len(modifiableInput):
                modifiableInput.pop(indexOfAWordWithDelimiter)
            break
        else:
            if word in keywords:
                if highestPriorityValueFound > (keywords[word])[2]:
                    highestPriorityValueFound = (keywords[word])[2]
                    keyStack.insert(0, word)
                else:
                    keyStack.append(word)
                modifiableInput[modifiableInput.index(word)] = (keywords[word])[1]

    userInput = ""
    for word in modifiableInput:
        userInput += word + " "
    userInput = userInput.rstrip()
    userInput = userInput.upper()

    keyStackTopWord = "NONE"
    match = None
    decompositionRuleIndex = 3
    keyWordDecompositionRule = ""

    if len(keyStack) != 0:
        keyStackTopWord = keyStack.pop(0)
        while match is None:
            keyWordDecompositionRule = ((keywords[keyStackTopWord])[decompositionRuleIndex])[0]
            match = re.search(keyWordDecompositionRule, userInput)
            if match is None:
                if decompositionRuleIndex + 1 < len(keywords[keyStackTopWord]):
                    decompositionRuleIndex += 1
                else:
                    decompositionRuleIndex = 3
                    if len(keyStack)-1 >= 0:
                        keyStackTopWord = keyStack.pop(0)
                    else:
                        keyStackTopWord = "NONE"
                        break

    if len(keyStack) == 0 and keyStackTopWord == "NONE":
        if len(memoryStack) == 0:
            print("[ELIZA]: " + ((keywords["NONE"])[3])[((keywords["NONE"])[3])[1]])
            if ((keywords["NONE"])[3])[1] + 1 < len(((keywords["NONE"])[3])):
                ((keywords["NONE"])[3])[1] += 1
            else:
                ((keywords["NONE"])[3])[1] = 2
        else:
            print("MEMORY RESPONSE NEEDED")

    else:
        keyWordReassemblyRule = ((keywords[keyStackTopWord])[decompositionRuleIndex])[((keywords[keyStackTopWord])[decompositionRuleIndex])[1]]
        if ((keywords[keyStackTopWord])[decompositionRuleIndex])[1] + 1 < len((keywords[keyStackTopWord])[decompositionRuleIndex]):
            ((keywords[keyStackTopWord])[decompositionRuleIndex])[1] += 1
        else:
            ((keywords[keyStackTopWord])[decompositionRuleIndex])[1] = 2
        print("[ELIZA]: " + re.sub(keyWordDecompositionRule, keyWordReassemblyRule, userInput))

    keyStack = []
    highestPriorityValueFound = 999
print("[ELIZA]: YOU ARE VERY WELCOME, " + userName + ". I HOPE I WAS ABLE TO HELP YOU.")
