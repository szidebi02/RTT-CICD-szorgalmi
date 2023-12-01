import sys
from pylint import lint


TRESHOLD = 10
run = lint.Run(["--rcfile=.pylintrc", "main.py"], exit=False)
score = run.linter.stats.global_note


print(f"Score: {score}")


#ez nem kell ahhoz hogy lefusson a linter, csak ha nem éri el a ponthatárt, így is megjeleníti
if score < TRESHOLD:
   print(f"Linter failed, Score: {score} < treshold")
