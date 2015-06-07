import webbrowser
webbrowser.open("http://www.codeskulptor.org/#user40_RrB5gcTvcf0aDLs.py")

# Rock-paper-scissors-lizard-Spock
# In our first mini-project, we will build a Python function rpsls(name) that takes
#     as input the string name, which is one of "rock", "paper", "scissors", "lizard",
#     or "Spock". The function then simulates playing a round of
#     Rock-paper-scissors-lizard-Spock by generating its own random choice from
#     these alternatives and then determining the winner using a simple rule that
#     we will next describe.
#
# While Rock-paper-scissor-lizard-Spock has a set of ten rules that logically
#     determine who wins a round of RPSLS, coding up these rules would require a
#     large number (5x5=25) of if/elif/else clauses in your mini-project code
# In this expanded list, each choice wins against the preceding two choices and
# loses against the following two choices (if rock and scissors are thought of as
# being adjacent using modular arithmetic)
