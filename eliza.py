# Name: Charles Ian Cutler
# Date: 02/08/2022
# Class: CMSC 416 Introduction to Natural Language Processing
# The following program is for the first programming assignment in the course
# CMSC 416, Intro to Natural Language Processing, at Virginia Commonwealth University
#
# This program was created with the intention to fulfil 3 goals. The first goal was to get
# familiar with using Python 3 as well as to get familiar with utilizing regular expressions
# for natural language processing. The second goal was to be able to successfully make
# transformations on input natural language sentences to create output phrases that
# are appropriate responses to the input. The third goal was to combine the first
# two goals and create a program that could engage in dialogue with the user.
# Specifically, to play the role of a psychotherapist name Eliza who can hold a
# conversation with the user about the user's personal problems.
#
# The program is called eliza.py, and it should run from the command line with no arguments.
# Once the program is running the user should be prompted to enter their name by Eliza.
# The user should type their name in and press the return key to enter it into the program.
# It is important to note that any name formatting is acceptable however the user should
# NOT use punctuation while entering their name. This will not cause a fault however it
# might look odd to the user to see their name adorned with a punctuation mark for the remainder of
# the program lifecycle.
#
# After the user enters their name the user should be prompted with a welcome message
# as well as a question asking about "What is wrong?". The user is welcome to use compound
# sentences as well as multiple sentence as input. However, it IS IMPERATIVE that the
# user use proper English grammatical structure. This includes proper punctuation especially.
#
# The following is an example of a program run, note that JILLIAN is an example user and ELIZA
# is the program.
# <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
#
#    Welcome to
#                     ______   ___      ____    ______    _______
#                    |  ____|  | |      |  |   |___   |  | |   | |
#       ______       | |__     | |      |  |      /  /   | |___| |       ______
#      |______|      |  __|    | |      |  |     /  /    |  ___  |      |______|
#                    | |____   | |___   |  |    /  /__   | |   | |
#                    |______|  |_____|  |__|   /______|  |_|   |_|
#
#    Eliza is a mock Rogerian psychotherapist.
#    The original program was described by Joesph Weizenbaum in 1966.
#    This implementation by Charles Cutler 2022.
#
# [ELIZA]: HELLO, MY NAME IS ELIZA. I WILL BE YOUR PSYCHOTHERAPIST. WHAT IS YOUR NAME?
# [...]: Jillian
# [ELIZA]: IT IS NICE TO MEET YOU JILLIAN. PLEASE TELL ME, WHAT IS WRONG?
# [JILLIAN]: I hate my classes.
# [ELIZA]: COULD YOU ELABORATE?
# [JILLIAN]: My classes are super boring.
# [ELIZA]: DID YOU THINK THEY MIGHT NOT BE SUPER BORING?
# [JILLIAN]: I knew they would be boring.
# [ELIZA]: COULD YOU CLARIFY WHAT YOU MEAN?
# [JILLIAN]: I am not in love with the subject matter.
# [ELIZA]: WHY ARE YOU NOT IN LOVE WITH THE SUBJECT MATTER?
# [JILLIAN]: Because I have no intention in going into business.
# [ELIZA]: PLEASE CONTINUE.
# [JILLIAN]: I am limited in selection for majors. Most of the other majors suck.
# [ELIZA]: IS IT BECAUSE YOU ARE LIMITED IN SELECTION FOR MAJORS THAT YOU CAME TO ME?
# [JILLIAN]: Perhaps.
# [ELIZA]: WHAT DOES THAT SUGGEST TO YOU?
# [JILLIAN]: I believe I need professional help.
# [ELIZA]: WHAT WOULD IT MEAN TO YOU IF YOU GOT PROFESSIONAL HELP?
# [JILLIAN]: It would mean a lot to me.
# [ELIZA]: MAYBE THERE IS SOMETHING ELSE I CAN HELP YOU WITH.
# [JILLIAN]: I feel I am crazy.
# [ELIZA]: DO YOU REALLY THINK SO?
# [JILLIAN]: I believe I am.
# [ELIZA]: COULD YOU ELABORATE?
# [JILLIAN]: My mother is crazy.
# [ELIZA]: COULD YOU CLARIFY WHAT YOU MEAN?
# [JILLIAN]: What about your family? Are they crazy?
# [ELIZA]: WHY ARE YOU CONCERNED OVER MY FAMILY?
# [JILLIAN]: I want to make sure they are not crazy.
# [ELIZA]: WHY DO YOU WANT TO MAKE SURE THEY ARE NOT CRAZY?
# [JILLIAN]: I am worried about them. You sound a bit crazy to me.
# [ELIZA]: HOW LONG HAVE YOU BEEN WORRIED ABOUT THEM?
# [JILLIAN]: About three minutes now.
# [ELIZA]: PLEASE CONTINUE.
# [JILLIAN]: Thank you Eliza.
# [ELIZA]: YOU ARE VERY WELCOME, JILLIAN. I HOPE I WAS ABLE TO HELP YOU.
# <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
#
# The program works by first parsing in the user's input sentence(s).
# It separates out extraneous sentences and identifies keywords.
# Keywords are transformed based on word replacement rules.
# After the input has been parsed and the keywords transformed the words are reconstructed into a single phrase.
# This phrase is then used by the program to find a suitable disassembly rule for the sentence.
# The rule is selected by finding a suitable keyword. When a rule is found the program then moves on to
# select a reassembly rule to generate a response.
# If there are no keywords then either a generic response or a response based on previous responses is generated.
#
# I used resources provided by Dr. Bridget McInnes of Virgina Commonwealth University to understand how to use
# regular expressions in python 3.
#
# Additionally, I used the website "GEEKS FOR GEEKS", https://www.geeksforgeeks.org/ to further my understanding of
# loops, if statements, and regular expressions.
#
# No code was copied from either source.
#
# This code is property of CHARLES I CUTLER,
# student at Virginia Commonwealth University.

import re

# familyRegEx creates a string that is the combination of a list of family words
# seperated by the pipe operator. Its purpose is to be used when every any "family" word is needed in a later RegEx

familyWords = ["FATHER", "MOTHER", "BROTHER", "SISTER", "UNCLE", "AUNT", "CHILDREN", "SON", "DAUGHTER",
               "GRANDFATHER", "GRANDMOTHER", "HUSBAND", "WIFE", "FAMILY"]
familyRegEx = ('|'.join(map(re.escape, familyWords)))

# beliefRegEx does the same thing as familyRegEx except it uses a list of "belief" words instead of "family" words.

beliefWords = ["FEEL", "THINK", "BELIEVE", "WISH"]
beliefRegEx = ('|'.join(map(re.escape, beliefWords)))

# memoryTransformations is a list of lists where the inner lists are sets of disassembly and
# reassembly rules for words that utilize the memory response feature.
# The outer list exists to hold the inner lists in a way that is traversable.

memoryTransformations = [[r"(.*)YOUR(.*)(\.|\!|\?)", r"DOES THAT HAVE ANYTHING TO DO WITH THE FACT \1YOUR\2?"],
                         [r"(.*)YOUR(.*)(" + familyRegEx + ")\s(.*)(\.|!|\?)", r"DOES THAT HAVE ANYTHING TO DO WITH THE FACT YOUR \3 \4?"]]

# keywords is a dictionary structure implemented to hold the keywords to be identified
# as well as various other information to be used.
# An example of a keyword structure would be as follows:
#
# KEYWORD: [ MEMORY FEATURE FLAG VALUE, DIRECT WORD TRANSFORMATION, KEYWORD PRIORITY, [DISASSEMBLY/REASSEMBLY RULES] ]
#
# Where MEMORY FEATURE FLAG VALUE:
#       is 0 for NO, usage of memory feature and -1 is for YES, usage of memory function.
# Where DIRECT WORD TRANSFORMATION:
#       is the word that keywords should be replaced with while the input sentence is parsed.
# Where KEYWORD PRIORITY:
#       is roughly how important the keyword is in the sentence. This allows for an identification of the most
#       appropriate keyword to find a disassembly and reassembly rule from.
# and Where [DISASSEMBLY/REASSEMBLY RULES] is structured as follows:
#       [SENTENCE DISASSEMBLY RULE REPRESENTED AS A REGULAR EXPRESSION , INDEX VALUE OF NEXT REASSEMBLY RULE TO USE,
#        REASSEMBLY RULE 1,
#        REASSEMBLY RULE 2,
#        REASSEMBLY RULE 3]

keywords = {
    # This is the special key word for when a generic response is needed.
    # It matches anything and substitutes a simple phrase or question to respond.
    "NONE": [0, "NONE", 0, [r"(.*)", 2,
                            r"COULD YOU ELABORATE?",
                            r"INTERESTING...",
                            r"COULD YOU CLARIFY WHAT YOU MEAN?",
                            r"WHAT DOES THAT SUGGEST TO YOU?",
                            r"MAYBE THERE IS SOMETHING ELSE I CAN HELP YOU WITH."]],
    # These are to convert colloquial family slang in to proper family titles for later use in other disassembly rules.
    # NEWKEY is used so in case this is the top keyword, the program knows to go to the next keyword from the stack.
    "MOM": [0, "MOTHER", 0, [r"NEWKEY"]],
    "DAD": [0, "FATHER", 0, [r"NEWKEY"]],
    "GRANDPA": [0, "GRANDFATHER", 0, [r"NEWKEY"]],
    "GRANDMA": [0, "GRANDMOTHER", 0, [r"NEWKEY"]],
    # AM was selected as it is a form of the verb meaning to be. It is often used to describe oneself or one's problems.
    # The first rule is looking for a form of an "AM I" sentence which is converted to "ARE YOU".
    # These are usually found when a person is wondering if they are something. Example might be "AM I CRAZY?"
    # I am converting these into sentences because often people explaining their problems use either AM I or I AM.
    # (I AM statements are found later under the keyword "I")
    "AM": [0, "ARE", 0, [r"(.*)ARE\sYOU\s(.*)(\.|\!)", 2,
                         r"DO YOU BELIEVE YOU ARE \2?",
                         r"WOULD YOU WANT TO BE \2?",
                         r"YOU WISH I WOULD TELL YOU YOU ARE \2?",
                         r"WHAT WOULD IT MEAN IF YOU WERE \2?"]],
    # "ARE" was selected as it is a form of the verb meaning to be. It is often used to ask question to another person.
    # The first rule is looking for a form of an "ARE YOU" sentence which is converted to "ARE I".
    #   These would be questions posed to ELIZA about ELIZA.
    # The second rule is looking for a form of an "ARE" sentence which remains "ARE"
    #   These would be statements about the state of existence of some object. Example, "Bullies are mean".
    # I picked it so that I could handle questions the user asks ELIZA about ELIZA and statements about objects.
    "ARE": [0, "ARE", 0, [r"(.*)ARE\sI\s(.*)(\.|\!|\?)", 2,
                          r"WHY ARE YOU INTERESTED IN WHETHER I AM \2 OR NOT?",
                          r"WOULD YOU PREFER IF I WERE NOT \2?",
                          r"PERHAPS I AM \2 IN YOUR IMAGINATION.",
                          r"DO YOU SOMETIMES THINK I AM \2?",
                          ],
                         [r"(.*)ARE\s(.*)(\.|\!)", 2,
                          r"DID YOU THINK THEY MIGHT NOT BE \2?",
                          r"WOULD YOU LIKE IT IF THEY WERE NOT \2?",
                          r"WHAT IF THEY WERE NOT \2?",
                          r"POSSIBLY THEY ARE \2?"]],
    # "YOUR" was selected as it is a second tense pronoun that the user may use to address something ELIZA "owns".
    # The idea behind this word was to address when the user may try and ask ELIZA about things "she" owns or does.
    # These responses generated by the rules look for the transformed key word and output a response.
    # This response take the item the user is concerned about and substitutes it into a response.
    "YOUR": [0, "MY", 0, [r"(.*)MY\s(.*)(\.|\!|\?)", 2,
                          r"WHY ARE YOU CONCERNED OVER MY \2?",
                          r"WHAT ABOUT YOUR OWN \2?",
                          r"ARE YOU WORRIED ABOUT SOMEONE ELSE'S \2?",
                          r"REALLY, MY \2?"]],
    # The word "WAS" was included to address times the user may ask if the were wrong to do some action.
    # Example, Was I wrong to point it out. Eliza would respond,  WHAT IF YOU WERE WRONG TO POINT IT OUT?".
    # It also handles cases where the user talks about something they were doing as well as something
    # the user perceives ELIZA was doing.
    # This first rule looks for a "WAS I" phrase transformed to "WAS YOU".
    # The second rule looks for a "I WAS" phrase transformed to " YOU WAS"
    # The final rule looks for a "WERE YOU" phrase transformed to "WAS YOU"
    "WAS": [0, "WAS", -2, [r"(.*)WAS\sYOU\s(.*)(\.|\!|\?)", 2,
                           r"WHAT IF YOU WERE \2?",
                           r"WHAT WOULD IT MEAN IF YOU WERE \2?",
                           r"WERE YOU \2?",
                           r"DO YOU THINK YOU WERE \2?",
                           r"WHAT DOES ' \4 ' SUGGEST TO YOU?",
                          ],
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
    # The word "WERE" was chosen to address questions the user might have in the pest tense of are.
    # The word functions the same as WAS and is transformed equivalently.
    "WERE": [0, "WAS", 0, ["=WAS"]],
    "ME": [0, "YOU", 0, [r"NEWKEY"]],
    # The contraction "YOU'RE" transformed to "I AM " was selected to again help ELIZA recognize
    # and deflect conversation away from itself and back towards the user.
    # when it is identified ELIZA generates a response to return conversation back to the user
    # centered area it can handle
    "YOU'RE": [0, "I AM", 0, [r"(.*)I\s(.*)(\.|\!|\?)", 2,
                              r"WE WERE DISCUSSING YOU NOT ME.",
                              r"OH, I \2?",
                              r"YOU ARE NOT REALLY TALKING ABOUT ME - ARE YOU?"]],
    # These two words were selected as words that needed appropriate translation into the correct tense.
    "MYSELF": [0, "YOURSELF", 0, [r"NEWKEY"]],
    "YOURSELF": [0, "MYSELF", 0, [r"NEWKEY"]],
    # "I" was selected as the "heavy-weight" champion of minimal context. The set of rules for the word "I"
    # allows ELIZA to respond to all sorts of user inputs when the user refers to them self and their situation.
    # The rules inc;ude ways to capture phrases that contain:
    #       "I WANT/NEED"
    #       "I AM SAD" (OR OTHER WORDS THAT MEAN SAD)
    #       "I AM HAPPY" (OR OTHER WORDS THAT MEAN HAPPY
    #       "I BELIEVE I" (AND OTHER BELIEF WORDS)
    #       "I WAS"
    #       "I FEEL"
    #       "I AM" (generic "I am" phrases)
    #       "I CAN'T/CANNOT"
    #       "I DON'T KNOW ANYTHING"
    #       "I DON'T"
    #       " I ... YOU"
    # These rules encompass much of what the user may express about themselves.
    "I": [0, "YOU", 0, [r"(.*)YOU\s(WANT|NEED)\s(.*)(\.|\!)", 2,
                        r"WHAT WOULD IT MEAN TO YOU IF YOU GOT \3?",
                        r"WHY DO YOU WANT \3?",
                        r"SUPPOSE YOU GOT \3 SOON.",
                        r"WHAT IF YOU NEVER GOT \3?",
                        r"WHAT WOULD GETTING \3 MEAN TO YOU?",
                        r"WHAT DOES GETTING \3 HAVE TO DO WITH YOUR PROBLEM?"],
                       [r"(,*)YOU\sHAVE\s(RECEIVED|EARNED|GOT)(.*)(\.|\?|!)", 2,
                        r"WHY?"],
                       [r"(.*)YOU\s(HAVE|GOT)(.*)(\.|\?|!)", 2,
                        r"WHY DO YOU HAVE \3?"],
                       [r"(.*)YOU\sHAD(.*)(\.|\?|!)", 2,
                        r"WHY DID YOU HAVE\2?"],
                       [r"(.*)YOU\sARE\s(.*)(SAD|UNHAPPY|DEPRESSED|SICK|FEELING\sBLUE)(.*)(\.|\!)", 2,
                        r"I AM SORRY TO HEAR YOU ARE \3. WHAT DO YOU THINK IS CAUSING YOU TO BE \3?",
                        r"WHAT WOULD CHEER YOU UP?",
                        r"WHAT WOULD MAKE YOU FEEL BETTER?",
                        r"DO YOU THINK LIQUOR HELP?",
                        r"I AM SURE IT IS NOT PLEASANT TO BE \3.",
                        r"CAN YOU EXPLAIN WHAT MADE YOU \3?"],
                       [r"(.*)YOU\sARE\s(.*)(HAPPY|ELATED|GLAD|BETTER)(.*)(\.|\!)", 2,
                        r"HAVE I HELPED YOU TO BE \3?",
                        r"WHAT MAKES YOU \3 NOW?",
                        r"CAN YOU EXPLAIN WHY YOU ARE \3?"],
                       [r"(.*)YOU\s(" + beliefRegEx + ")\sYOU\s(.*)(\.|!|\?)", 2,
                        r"DO YOU REALLY THINK SO?",
                        r"BUT YOU ARE NOT SURE YOU \3?",
                        r"DO YOU REALLY DOUBT YOU \3?"],
                       [r"(.*)YOU\sWAS\s(.*)(\.|\!|\?)", 2,
                        r"WERE YOU REALLY?",
                        r"WHY DO YOU TELL ME YOU WERE \2 NOW?",
                        r"PERHAPS I ALREADY KNEW YOU WERE \2?"
                        ],
                       [r"(.*)YOU\sFEEL\s(.*)(\.|!|\?)", 2,
                        r"TELL ME MORE ABOUT SUCH FEELINGS.",
                        r"DO YOU OFTEN FEEL \2?",
                        r"WHAT DOES FEELING \2 REMIND YOU OF?"],
                       [r"(.*)YOU\sARE\s(.*)(\.|\!)", 2,
                        r"WHY ARE YOU \2?",
                        r"IS IT BECAUSE YOU ARE \2 THAT YOU CAME TO ME?",
                        r"HOW LONG HAVE YOU BEEN \2?",
                        r"DO YOU BELIEVE IT IS NORMAL TO BE \2?"],
                       [r"(.*)YOU\s(CAN'T|CANNOT)(.*)(\.|\!|\?)", 2,
                        r"HOW DO YOU KNOW YOU CANNOT\3?",
                        r"HAVE YOU TRIED?",
                        r"PERHAPS YOU COULD\3 NOW?",
                        r"DO YOU REALLY WANT TO BE ABLE TO\3"],
                       [r"(.*)YOU\sDON'T\sKNOW\sANYTHING(.*)(\.|\!\?)", 2,
                        r"I AM SURE YOU KNOW SOMETHING. WHAT COMES TO MIND?"],
                       [r"(.*)YOU\sDON'T\s(.*)(\.|\!\?)", 2,
                        r"DON'T YOU REALLY \2?",
                        r"WHY DON'T YOU \2?",
                        r"DO YOU WISH TO BE ABLE TO\2?",
                        r"DOES THAT TROUBLE YOU?"],
                       [r"(.*)YOU\s(.*)\sI\s(.*)(\.|!|\?)", 2,
                        r"DO YOU \2 ANYONE ELSE?",
                        r"PERHAPS IN YOUR DREAMS WE \2 EACH OTHER.",
                        r"DO YOU WISH TO \2 ME?",
                        r"YOU SEEM TO NEED TO \2 ME."]],
    # The word "YOU" was selected to allow for ELIZA to respond to questions about ELIZA's personal being.
    # The "YOU ARE" phrases are transformed to "I ARE" phrases catch qstatements about what ELIZA may be.
    # The "YOU ... ME" phrases are transformed to "I ... YOU"
    # phrases to catch statements about something ELIZA "feels" about the user. Such as "DO YOU LIKE ME?"
    "YOU": [0, "I", 0, [r"(.*)I\sARE(.*)(\.|\?|!)", 2,
                        r"WHAT MAKES YOU THINK I AM\2?",
                        r"DOES IT MAKE YOU HAPPY TO THINK I AM\2?",
                        r"DO YOU SOMETIMES WISH YOU WERE\2?",
                        ],
                       [r"(.*)I\s(.*)\sYOU(\.|\?|!)", 2,
                        r"WHY DO YOU THINK I \2 YOU?",
                        r"WHAT MAKES YOU THINK I \2 YOU?",
                        r"SUPPOSE I DID \2 YOU - WHAT WOULD IT MEAN?",
                        r"DOES SOMEONE ELSE BELIEVE I \2 YOU?"]],
    # The word "MY" was selected to account for times the user refers to something of their own.
    # This might be an object or their family and the rules account for both.
    # The first rule accounts for the user family and something that member may have done.
    # The second rule accounts for the other things a user may refer to as their own.
    "MY": [-1, "YOUR", -2, [r"(.*)YOUR(.*)(" + familyRegEx + ")\s(.*)(\.|!|\?)", 2,
                            r"TELL ME MORE ABOUT YOUR FAMILY.",
                            r"WHO ELSE IN YOUR FAMILY \4?",
                            r"YOUR \3?",
                            r"WHAT ELSE COMES TO MIND WHEN YOU THINK OF YOUR \3?"],
                          [r"(.*)YOUR(.*)(\.|\!|\?)", 2,
                           r"YOUR\2?",
                           r"WHY DO YOU SAY YOUR\2?",
                           r"DOES THAT SUGGEST ANYTHING TO YOU?",
                           r"IS IT IMPORTANT TO YOU THAT YOUR\2?"]],
    # The words "HOW", "WHEN", and "WHAT" were chosen because the user may ask questions which require
    # real world knowledge to answer. ELIZA uses these rules to answer in such a way where no understanding is needed.
    # The "=WHAT" means that for that word it uses the same set of disassembly and reassembly rules as the word after
    # the equals sign. In this the word "WHAT".
    # The rule simply takes in any sentence that has been identified with a question word and responds with a question.
    # These responses work great for questions that ELIZA does not have a different keyword that works for the input.
    "HOW": [0, "HOW", 0, ["=WHAT"]],
    "WHEN": [0, "WHEN", 0, ["=WHAT"]],
    "WHAT": [0, "WHAT", 0, [r"(.*)(\.|\!|\?)", 2,
                            r"WHY DO YOU ASK?",
                            r"WHAT DO YOU THINK?",
                            r"DOES THAT QUESTION INTEREST YOU?",
                            r"WHAT IS IT YOU REALLY WANT TO KNOW?",
                            r"ARE SUCH QUESTIONS ON YOUR MIND OFTEN?",
                            r"HAVE YOU ASKED ANYONE ELSE?"]],
    "WHY": [0, "WHY", 0, [r"(.*)WHY\sDON'T\sI(.*)[.?!]", 2,
                          r"DO YOU BELIEVE I DO NOT\2?",
                          r"PERHAPS I WILL\2?",
                          r"WHY DO YOU ASK?",
                          r"WHAT DO YOU THINK?",
                          r"DOES THAT QUESTION INTEREST YOU?",
                          r"WHAT IS IT YOU REALLY WANT TO KNOW?",
                          r"ARE SUCH QUESTIONS ON YOUR MIND OFTEN?",
                          r"HAVE YOU ASKED ANYONE ELSE?"],
                         [r"(.*)WHY\sCAN'T\sYOU(.*)[.?!]", 2,
                          r"DO YOU THINK YOU SHOULD BE ABLE TO\2?",
                          r"DO YOU WANT TO BE ABLE TO\2?",
                          r"WHY DO YOU ASK?",
                          r"WHAT DO YOU THINK?",
                          r"DOES THAT QUESTION INTEREST YOU?",
                          r"WHAT IS IT YOU REALLY WANT TO KNOW?",
                          r"ARE SUCH QUESTIONS ON YOUR MIND OFTEN?",
                          r"HAVE YOU ASKED ANYONE ELSE?"]],
    # The words "ALIKE", "SIMILAR", "SAME" and "SYN" (Short for Synonym, which sort of means similar) were
    # chosen because the user may speak in relations ships.
    # Example. My classes are similar to learning how to ride a bike
    # In this case, and cases like it, ELIZA should be able to recognize and
    # ask for a deeper "understanding" of the relationship between the items.
    # Once again the "=SYN" just allows for me to simplify the amount of data being stored. Words with "=SYN"
    # use the rules for the word "SYN"
    # The rule for them simply takes in the sentence that has been identified with a "similarity" word
    # and substitutes in a question.
    "ALIKE": [0, "ALIKE", -10, ["=SYN"]],
    "SIMILAR": [0, "SIMILAR", -10, ["=SYN"]],
    "SAME": [0, "SAME", -10, ["=SYN"]],
    "SYN": [0, "SYN", -10, [r"(.*)(\.|\!|\?)", 2,
                            r"IN WHAT WAY?",
                            r"WHAT DOES THAT SIMILARITY SUGGEST?",
                            r"WHAT DO YOU THINK IS THE CONNECTION?",
                            r"COULD THERE REALLY BE SOME CONNECTION?",
                            r"HOW?"]],
    # The words "YES" and "NO" were picked to respond to the simple
    # yes and no responses the user may in put in response to other ELIZA questions.
    # The rules look for the words at the beginning of sentences and substitute in an appropriate phrase.
    "NO": [0, "NO", -10, [r"NO(.*)[.!?]", 2,
                          r"WHY NOT?"]],
    "YES": [0, "YES", -10, [r"YES(.*)[.?!]", 2,
                            r"YOU SEEM QUITE SURE IN YOUR RESPONSE. WHY?",
                            r"I SEE. WHAT ELSE?",
                            r"YES, I UNDERSTAND! TELL ME MORE."]],
    # The words "EVERYONE", "EVERYBODY", "NOBODY", and "NOONE" were selected for similar as to the words "ALIKE", etc.
    # The user may use ambiguous langauge to avoid name someone specific.
    # These words are used to provoke a more detailed response from the user.
    # The rules work the same for the words with the "=EVERYONE" as the did for the above words with "=SYN"
    # The "EVERYONE" rule looks for an instance of the ambiguous langauge and prompts the user to be more specific.
    "EVERYONE": [0, "EVERYONE", -2, [r"(.*)(EVERYONE|EVERYBODY|NOBODY|NO\sONE)\s(.*)(\.|\?|!)", 2,
                                     r"WHO, MAY I ASK?",
                                     r"REALLY, \2?",
                                     r"CAN YOU THINK OF ANYONE IN PARTICULAR?",
                                     r"WHO, FOR EXAMPLE?"]],
    "EVERYBODY": [0, "EVERYBODY", -2, ["=EVERYONE"]],
    "NOBODY": [0, "NOBODY", -2, ["=EVERYONE"]],
    "NOONE": [0, "NOONE", -2, ["=EVERYONE"]],
    # "BECAUSE" was selected to  have ELIZA respond to statements the user poses
    # as reasoning or justification of the user's situation.
    # The rules prompt a further consideration by the user into
    # the real meaning behind their problems.
    "BECAUSE": [0, "BECAUSE", -2, [r"(.*)[.?!]", 2,
                                   r"IS THAT THE REAL REASON?",
                                   r"DOES THAT REASON EXPLAIN ANYTHING ELSE?",
                                   r"WHAT OTHER REASONS MIGHT THERE BE?"]],
    # This word "KILL" is set as the highest priority in case the user considering murder or suicide.
    "KILL": [0, "KILL", -100, [r"(.*)YOU(.*)KILL\sI(.*)[.?!]", 2,
                               r"WOULD KILLING ME SOLVE YOUR PROBLEMS?"],
                              [r"(.*)KILL\sYOURSELF(.*)[.?!]", 2,
                               r"YOUR LIFE IS VERY IMPORTANT. PLEASE CALL THE SUICIDE HOTLINE AT: 800-273-8255. "]]
    }

# Print Logo and Welcome Message
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

# Take in the User's name as input and store
userName = (input("[...]: ")).upper()

parsedInput = []
modifiableInput = []
keyStack = []
memoryStack = []
highestPriorityValueFound = 9999
indexOfAWordWithDelimiter = 0

print("[ELIZA]: IT IS NICE TO MEET YOU " + userName + ". PLEASE TELL ME, WHAT IS WRONG?")

# The following loop is the driver loop of the program. It loops until the end phrase is typed by the user.
# The end loop phrase is case-sensitive and very specific to allow for regular usage of the words.
# The end loop phrase is, "Thank you Eliza.", let the user note the period following the word Eliza.
while True:
    userInput = input("[" + userName + "]: ")
    if userInput == "Thank you Eliza.":
        break

    parsedInput = userInput.split(" ")
    modifiableInput = parsedInput.copy()
# This section of the code is used for the parsing of the input phrase.
    # This for loop is used to parse the user input for keywords as well as filter out extraneous information.
    # It works as follows:
    # 1st) It checks whether the current word from the input phrase contains a punctuation mark.
    #       If the word has a punctuation mark, the program has yet to find any keywords, and
    #       the word itself is not a keyword, then the program strips the word and
    #       everything prior to it out of the modifiable version of the input phrase
    #
    #       If the above criteria are not met, then the program evaluates the next if statement.
    #       If the word has a punctuation mark, and we have already found a useful key word prior
    #       to the word with punctuation, then we strip off everything after the word from the
    #       modifiable version of the input phrase.
    #
    #       Otherwise, the program will simply check if the word is a keyword.
    #       If it is not, it moves to the next word in the input phrase.
    #       If it is a keyword, then the program strips off any punctuation characters, makes the word uppercase,
    #       and evaluates the priority of the keyword.
    #           If the keyword has a priority higher than, which means a value closer to 0, then it takes the place
    #           of the most important word.
    #           Then key word is updated in the modifiable version of the input phrase by the direct replacement word.
    for word in parsedInput:
        punctuationMatch = re.search(r"[.?,!]", word)
        if punctuationMatch and len(keyStack) == 0 and (not((word.strip(",.!?").upper()) in keywords)):
            indexOfAWordWithDelimiter = modifiableInput.index(word)
            while indexOfAWordWithDelimiter >= 0:
                modifiableInput.pop(indexOfAWordWithDelimiter)
                indexOfAWordWithDelimiter -= 1
        elif punctuationMatch and len(keyStack) > 0 and (not((word.strip(",.!?").upper()) in keywords)):
            indexOfAWordWithDelimiter = modifiableInput.index(word) + 1
            while indexOfAWordWithDelimiter != len(modifiableInput):
                modifiableInput.pop(indexOfAWordWithDelimiter)
            modifiableInput[modifiableInput.index(word)] = word.strip(",.!?").upper() + "."
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

# This section of the code reconstructs the parsed and modified version of the input phrase into a single string.
    userInput = ""
    for word in modifiableInput:
        userInput += word + " "
    userInput = userInput.rstrip()  # Removes trailing space
    userInput = userInput.upper()  # Makes the whole string Uppercase
    # These are needed in case the last word is a key word or if the only word is a key word.
    # This is because a punctuation mark is needed for regex to work
    if len(modifiableInput) == 1:
        userInput += "."
    elif len(modifiableInput) > 0:
        if modifiableInput[-1] in keywords:
            userInput += "."

# This section of the code is used for deconstruction, reassembly, and response generation by the program
    keyStackTopWord = "NONE"
    match = None
    decompositionRuleIndex = 3
    keyWordDecompositionRule = ""

    # The following if statement attempts to find an appropriate disassembly rule for the input phrase.
    # The program removes the top of the keywords stack, which first is always the most important word.
    # The program then retrieves the first disassembly rule and attempts to match it to the input phrase.
    #
    # If it is a match we break the loop and continue.
    #
    # Otherwise, the program checks whether to go to the next disassembly rule for the same keyword or,
    # if there are no more rules for that word, it resets the initial conditions and pops the next
    # keyword from the stack.
    #
    # If no keywords are left and no suitable disassembly rule has been found then the program sets
    # the keyword to a special keyword and continues
    if len(keyStack) != 0:
        keyStackTopWord = keyStack.pop(0)
        while match is None:
            keyWordDecompositionRule = ((keywords[keyStackTopWord])[decompositionRuleIndex])[0]
            # It is worth mentioning that this special statement, considers when a disassembly rule
            # references the rules of another keyword. Such as the word "How", whose responses would be the
            # same as the word "What". This allows me, the programmer, to save space.
            if "=" in keyWordDecompositionRule:
                keyStackTopWord = keyWordDecompositionRule.strip("=")
                decompositionRuleIndex = 3
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
    # The following if statement is for the case where there are no suitable keywords to generate a response from.
    # When there are no keywords left in the stack and the last word evaluate has been set as "NONE", then
    # Either a generic response or memory response is generated. The choice solely depends on whether there are
    # any memory responses to pull from or not.
    if len(keyStack) == 0 and keyStackTopWord == "NONE":
        if len(memoryStack) == 0:
            print("[ELIZA]: " + ((keywords["NONE"])[3])[((keywords["NONE"])[3])[1]])
            if ((keywords["NONE"])[3])[1] + 1 < len(((keywords["NONE"])[3])):
                ((keywords["NONE"])[3])[1] += 1
            else:
                ((keywords["NONE"])[3])[1] = 2
        else:
            print("[ELIZA]: " + memoryStack.pop(0))
    # The following else statement is where a response based on a key word is generated.
    # First a reassembly rule is selected by the program. This is based on which ever reassembly rule was used last
    # for the corresponding word and disassembly phrase. The one picked is the next one in the sequence.
    # Then a response is printed.
    #
    # Following the response. The program handles the use of the memory feature. If a keyword uses the memory feature,
    # the necessary response is generated and saved for later use.
    #
    # The program resets the keyStack and priority values for the next input by the user.
    # Lastly, the program prints a personalized message saying goodbye prior to terminating.
    else:
        keyWordReassemblyRule = ((keywords[keyStackTopWord])[decompositionRuleIndex])[((keywords[keyStackTopWord])[decompositionRuleIndex])[1]]
        if ((keywords[keyStackTopWord])[decompositionRuleIndex])[1] + 1 < len((keywords[keyStackTopWord])[decompositionRuleIndex]):
            ((keywords[keyStackTopWord])[decompositionRuleIndex])[1] += 1
        else:
            ((keywords[keyStackTopWord])[decompositionRuleIndex])[1] = 2
        print("[ELIZA]: " + re.sub(keyWordDecompositionRule, keyWordReassemblyRule, userInput))
        if (keywords[keyStackTopWord])[0] < 0:
            for rules in memoryTransformations:
                if rules[0] == keyWordDecompositionRule:
                    memoryStack.append(re.sub(keyWordDecompositionRule, rules[1], userInput))
                    break
    keyStack = []
    highestPriorityValueFound = 9999
print("[ELIZA]: YOU ARE VERY WELCOME, " + userName + ". I HOPE I WAS ABLE TO HELP YOU.")
