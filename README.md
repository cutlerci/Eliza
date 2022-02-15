![VCU Logo](https://ocpe.vcu.edu/media/ocpe/images/logos/bm_CollEng_CompSci_RF2_hz_4c.png)

# Cutlerci-CMSC416-Project 1
My name is Charles Ian Cutler, CIC, currently enrolled in the College of Engineering at Virginia Commonwealth Univeristy. 
This repository is for a project in Virginia Commonwealth University course CMSC 416, Introduction Natural Language Processing, Spring 2022.
## Repository Files
1) eliza.py -- The program itself.
2) CIC_pseudocode_Design_Process.pdf -- A PDF of my hand drawn pseudo code I used to ultimately develop my project.
## ELIZA Description
 The following program is for the first programming assignment in the course
 CMSC 416, Intro to Natural Language Processing, at Virginia Commonwealth University

This program was created with the intention to fulfil 3 goals. The first goal was to get familiar with using Python 3 as well as to get familiar with utilizing regular expressions for natural language processing. The second goal was to be able to successfully make transformations on input natural language sentences to create output phrases that are appropriate responses to the input. The third goal was to combine the first two goals and create a program that could engage in dialogue with the user. Specifically, to play the role of a psychotherapist name Eliza who can hold a conversation with the user about the user's personal problems.

The program is called eliza.py, and it should run from the command line with no arguments. Once the program is running the user should be prompted to enter their name by Eliza. The user should type their name in and press the return key to enter it into the program. It is important to note that any name formatting is acceptable however the user should NOT use punctuation while entering their name. This will not cause a fault however it might look odd to the user to see their name adorned with a punctuation mark for the remainder of the program lifecycle.

After the user enters their name the user should be prompted with a welcome message as well as a question asking about "What is wrong?". The user is welcome to use compound sentences as well as multiple sentence as input. However, it IS IMPERATIVE that the user use proper English grammatical structure. This includes proper punctuation especially.

The following is an example of a program run, note that JILLIAN is an example user and ELIZA is the program.

<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>

    Welcome to
                     ______   ___      ____    ______    _______
                    |  ____|  | |      |  |   |___   |  | |   | |
       ______       | |__     | |      |  |      /  /   | |___| |       ______
      |______|      |  __|    | |      |  |     /  /    |  ___  |      |______|
                    | |____   | |___   |  |    /  /__   | |   | |
                    |______|  |_____|  |__|   /______|  |_|   |_|

    Eliza is a mock Rogerian psychotherapist.
    The original program was described by Joesph Weizenbaum in 1966.
    This implementation by Charles Cutler 2022.

    [ELIZA]: HELLO, MY NAME IS ELIZA. I WILL BE YOUR PSYCHOTHERAPIST. WHAT IS YOUR NAME?
    [...]: Jillian
    [ELIZA]: IT IS NICE TO MEET YOU JILLIAN. PLEASE TELL ME, WHAT IS WRONG?
    [JILLIAN]: I hate my classes.
    [ELIZA]: COULD YOU ELABORATE?
    [JILLIAN]: My classes are super boring.
    [ELIZA]: DID YOU THINK THEY MIGHT NOT BE SUPER BORING?
    [JILLIAN]: I knew they would be boring.
    [ELIZA]: COULD YOU CLARIFY WHAT YOU MEAN?
    [JILLIAN]: I am not in love with the subject matter.
    [ELIZA]: WHY ARE YOU NOT IN LOVE WITH THE SUBJECT MATTER?
    [JILLIAN]: Because I have no intention in going into business.
    [ELIZA]: PLEASE CONTINUE.
    [JILLIAN]: I am limited in selection for majors. Most of the other majors suck.
    [ELIZA]: IS IT BECAUSE YOU ARE LIMITED IN SELECTION FOR MAJORS THAT YOU CAME TO ME?
    [JILLIAN]: Perhaps.
    [ELIZA]: WHAT DOES THAT SUGGEST TO YOU?
    [JILLIAN]: I believe I need professional help.
    [ELIZA]: WHAT WOULD IT MEAN TO YOU IF YOU GOT PROFESSIONAL HELP?
    [JILLIAN]: It would mean a lot to me.
    [ELIZA]: MAYBE THERE IS SOMETHING ELSE I CAN HELP YOU WITH.
    [JILLIAN]: I feel I am crazy.
    [ELIZA]: DO YOU REALLY THINK SO?
    [JILLIAN]: I believe I am.
    [ELIZA]: COULD YOU ELABORATE?
    [JILLIAN]: My mother is crazy.
    [ELIZA]: COULD YOU CLARIFY WHAT YOU MEAN?
    [JILLIAN]: What about your family? Are they crazy?
    [ELIZA]: WHY ARE YOU CONCERNED OVER MY FAMILY?
    [JILLIAN]: I want to make sure they are not crazy.
    [ELIZA]: WHY DO YOU WANT TO MAKE SURE THEY ARE NOT CRAZY?
    [JILLIAN]: I am worried about them. You sound a bit crazy to me.
    [ELIZA]: HOW LONG HAVE YOU BEEN WORRIED ABOUT THEM?
    [JILLIAN]: About three minutes now.
    [ELIZA]: PLEASE CONTINUE.
    [JILLIAN]: Thank you Eliza.
    [ELIZA]: YOU ARE VERY WELCOME, JILLIAN. I HOPE I WAS ABLE TO HELP YOU.
    
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>

The program works by first parsing in the user's input sentence(s). It separates out extraneous sentences and identifies keywords. Keywords are transformed based on word replacement rules. After the input has been parsed and the keywords transformed the words are reconstructed into a single phrase. This phrase is then used by the program to find a suitable disassembly rule for the sentence. The rule is selected by finding a suitable keyword. When a rule is found the program then moves on to select a reassembly rule to generate a response. If there are no keywords then either a generic response or a response based on previous responses is generated.

I used resources provided by Dr. Bridget McInnes of Virgina Commonwealth University to understand how to use regular expressions in python 3.

Additionally, I used the website "GEEKS FOR GEEKS", https://www.geeksforgeeks.org/ to further my understanding of loops, if statements, and regular expressions.

No code was copied from either source.

This code is property of CHARLES I CUTLER, student at Virginia Commonwealth University.

