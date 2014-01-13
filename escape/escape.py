"""
Escape

Initial code take from:
    http://pymotw.com/2/readline/index.html#module-readline
"""
import readline

readline.parse_and_bind('tab: complete')

print("Welcome to Escape! Your goal is "
      "to escape your prison cell. Good luck!")

while True:
    line = raw_input("Prompt ('quit' to quit): ")
    if line == "quit":
        break
    print("ENTERED: '{0}'".format(line))
