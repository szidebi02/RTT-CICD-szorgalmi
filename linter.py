import sys
from pylint import lint


TRESHOLD = 10
run = lint.Run(["--rcfile=.pylintrc", "main.py"], exit=False)
score = run.linter.stats.global_note


print(f"Score: {score}")

if score < TRESHOLD:
   print(f"Linter failed, Score: {score} < treshold")
   
sys.exit(1)


sys.exit(0)
