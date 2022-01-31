import re

familyWords = ["FATHER", "MOTHER", "BROTHER", "SISTER", "UNCLE", "AUNT", "CHILDREN", "SON", "DAUGHTER",
               "GRANDFATHER", "GRANDMOTHER", "HUSBAND", "WIFE"]
familyRegEx = ('|'.join(map(re.escape, familyWords)))

beliefWords = ["FEEL", "THINK", "BELIEVE", "WISH"]
beliefRegEx = ('|'.join(map(re.escape, beliefWords)))

keywords = {
    "NONE": [0, "NONE", 0, [r"(.*)", 2,
                            r"COULD YOU ELABORATE?",
                            r"COULD YOU CLARIFY WHAT YOU MEAN?",
                            r"PLEASE CONTINUE.",
                            r"WHAT DOES THAT SUGGEST TO YOU?",
                            r"MAYBE THERE IS SOMETHING ELSE I CAN HELP YOU WITH."]],
    "MOM": [0, "MOTHER", 0, [r"NEWKEY"]],
    "DAD": [0, "FATHER", 0, [r"NEWKEY"]],
    "GRANDPA": [0, "GRANDFATHER", 0, [r"NEWKEY"]],
    "GRANDMA": [0, "GRANDMOTHER", 0, [r"NEWKEY"]],
    "AM": [0, "ARE", 0, [r"(.*)ARE\sYOU\s(.*)(\.|\!)", 2,
                         r"DO YOU BELIEVE YOU ARE \2?",
                         r"WOULD YOU WANT TO BE \2?",
                         r"YOU WISH I WOULD TELL YOU YOU ARE \2?",
                         r"WHAT WOULD IT MEAN IF YOU WERE \2?"],  # ADD THE ABILITY TO GO TO (=WHAT) REASSEMBLY
                        [r"ARE(\.|\!)", 2,
                         r"WHY DO YOU SAY 'AM'?",
                         r"I DO NOT UNDERSTAND THAT."]],
    "ARE": [0, "ARE", 0, [r"(.*)ARE\sI\s(.*)(\.|\!|\?)", 2,
                          r"WHY ARE YOU INTERESTED IN WHETHER I AM \2 OR NOT?",
                          r"WOULD YOU PREFER IF I WERE NOT \2?",
                          r"PERHAPS I AM \2 IN YOUR IMAGINATION.",
                          r"DO YOU SOMETIMES THINK I AM \2?",
                          ],  # ADD THE ABILITY TO GO TO (=WHAT) REASSEMBLY
                         [r"(.*)ARE\s(.*)(\.|\!)", 2,
                          r"DID YOU THINK THEY MIGHT NOT BE \2?",
                          r"WOULD YOU LIKE IT IF THEY WERE NOT \2?",
                          r"WHAT IF THEY WERE NOT \2?",
                          r"POSSIBLY THEY ARE \2?"]],
    "YOUR": [0, "MY", 0, [r"(.*)MY\s(.*)(\.|\!|\?)", 2,
                          r"WHY ARE YOU CONCERNED OVER MY \2?",
                          r"WHAT ABOUT YOUR OWN \2?",
                          r"ARE YOU WORRIED ABOUT SOMEONE ELSE'S \2?",
                          r"REALLY, MY \2?"]],
    "WAS": [0, "WAS", 2, [r"(.*)WAS\sYOU\s(.*)(\.|\!|\?)", 2,
                          r"WHAT IF YOU WERE \2?",
                          r"WHAT WOULD IT MEAN IF YOU WERE \2?",
                          r"WERE YOU \2?",
                          r"DO YOU THINK YOU WERE \2?",
                          r"WHAT DOES ' \4 ' SUGGEST TO YOU?",
                          ],  # ADD THE ABILITY TO GO TO (=WHAT) REASSEMBLY
                         [r"(.*)YOU\sWAS\s(.*)(\.|\!|\?)", 2,
                          r"WERE YOU REALLY?",
                          r"WHY DO YOU TELL ME YOU WERE \2 NOW?",
                          r"PERHAPS I ALREADY KNEW YOU WERE \2?"],
                         [r"(.*)WAS\sI\s(.*)(\.|\!|\?)", 2,
                          r"WOULD YOU LIKE TO BELIEVE I WAS \2?",
                          r"WHAT SUGGESTS THAT I WAS \2?",
                          r"WHAT DO YOU THINK?",
                          r"MAYBE I WAS \2?"
                          r"WHAT IF I HAD BEEN \2?",
                          ]],
    "WERE": [0, "WAS", 0, ["=WAS"]],
    "ME": [0, "YOU", 0, [r"NEWKEY"]],
    "YOU'RE": [0, "I AM", 0, [r"(.*)I\s(.*)(\.|\!|\?)", 2,
                              r"WE WERE DISCUSSING YOU NOT ME.",
                              r"OH, I \2?",
                              r"YOU ARE NOT REALLY TALKING ABOUT ME - ARE YOU?"]],
    "MYSELF": [0, "YOURSELF", 0, [r"NEWKEY"]],
    "YOURSELF": [0, "MYSELF", 0, [r"NEWKEY"]],
    "I": [0, "YOU", 0, [r"(.*)YOU\s(WANT|NEED)\s([a-zA-Z ]*)(\.|\!)", 2,
                        r"WHAT WOULD IT MEAN TO YOU IF YOU GOT \3?",
                        r"WHY DO YOU WANT \3?",
                        r"SUPPOSE YOU GOT \3 SOON.",
                        r"WHAT IF YOU NEVER GOT \3?",
                        r"WHAT WOULD GETTING \3 MEAN TO YOU?",
                        r"WHAT DOES GETTING \3 HAVE TO DO WITH YOUR PROBLEM?"],
                       [r"(.*)YOU\sARE\s(.*)(SAD|UNHAPPY|DEPRESSED|SICK|FEELING\sBLUE)(.*)(\.|\!)", 2,
                        r"I AM SORRY TO HEAR YOU ARE \3. WHAT DO YOU THINK IS CAUSING YOU TO BE \3?",
                        r"WHAT WOULD CHEER YOU UP?",
                        r"WHAT WOULD MAKE YOU FEEL BETTER?",
                        r"DO YOU THINK LIQUOR HELP?",
                        r"I AM SURE IT IS NOT PLEASANT TO BE \3.",
                        r"CAN YOU EXPLAIN WHAT MADE YOU \3?"],
                       [r"(.*)YOU\sARE\s(.*)(HAPPY|ELATED|GLAD|BETTER)(.*)(\.|\!)", 2,
                        r"HOW HAVE I HELPED YOU TO BE \3?",
                        r"WHAT MAKES YOU \3 JUST NOW?",
                        r"CAN YOU EXPLAIN WHY YOU ARE SUDDENLY \3?"],
                       [r"(.*)YOU\sWAS\s(.*)(\.|\!|\?)", 2,
                        r"WERE YOU REALLY?",
                        r"WHY DO YOU TELL ME YOU WERE \2 NOW?",
                        r"PERHAPS I ALREADY KNEW YOU WERE \2?"
                        ],
                       [r"(.*)YOU\s(" + beliefRegEx + ")\sYOU\s(.*)(\.|\!|\?)", 2,
                        r"DO YOU REALLY THINK SO?",
                        r"BUT YOU ARE NOT SURE YOU \3?",
                        r"DO YOU REALLY DOUBT YOU \3?"],
                       [r"(.*)YOU\sARE\s(.*)(\.|\!)", 2,
                        r"WHY ARE YOU \2?",
                        r"IS IT BECAUSE YOU ARE \2 THAT YOU CAME TO ME?",
                        r"HOW LONG HAVE YOU BEEN \2?",
                        r"DO YOU BELIEVE IT IS NORMAL TO BE \2?"]],
    "YOU": [0, "I", 5, []]
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
        if (("," in word) or ("." in word)) and (len(keyStack) == 0 and (not((word.strip(",.").upper()) in keywords))):
            indexOfAWordWithDelimiter = modifiableInput.index(word)
            while indexOfAWordWithDelimiter >= 0:
                modifiableInput.pop(indexOfAWordWithDelimiter)
                indexOfAWordWithDelimiter -= 1
        elif (("," in word) or ("." in word)) and (len(keyStack) > 0 ):
            indexOfAWordWithDelimiter = modifiableInput.index(word) + 1
            while indexOfAWordWithDelimiter != len(modifiableInput):
                modifiableInput.pop(indexOfAWordWithDelimiter)
            break
        else:
            strippedWord = word.strip(",.?!").upper()
            if strippedWord in keywords:
                if highestPriorityValueFound > (keywords[strippedWord])[2]:
                    highestPriorityValueFound = (keywords[strippedWord])[2]
                    keyStack.insert(0, strippedWord)
                else:
                    keyStack.append(strippedWord)
                modifiableInput[modifiableInput.index(word)] = (keywords[strippedWord])[1]

    userInput = ""
    for word in modifiableInput:
        userInput += word + " "
    userInput = userInput.rstrip()
    userInput = userInput.upper()
    if (len(modifiableInput) == 1):
        userInput += "."
    if len(modifiableInput) > 0:
        if modifiableInput[-1] in keywords:
            userInput += "."
    keyStackTopWord = "NONE"
    match = None
    decompositionRuleIndex = 3
    keyWordDecompositionRule = ""

    if len(keyStack) != 0:
        keyStackTopWord = keyStack.pop(0)
        while match is None:
            keyWordDecompositionRule = ((keywords[keyStackTopWord])[decompositionRuleIndex])[0]
            if "=" in keyWordDecompositionRule:
                keyStackTopWord = keyWordDecompositionRule.strip("=")
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

#p = re.compile(r"(.*)(my|My)(.*)(" + familyRegEx + ")(.*)(\.|\!)")
r"(.*)YOU\s(" + beliefRegEx + ")\sYOU\s(.*)(\.|\!|\?)"
