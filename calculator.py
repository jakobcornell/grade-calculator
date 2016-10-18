import sys
import parsing

course = parsing.parse_course(sys.stdin)
score = course.score()

if score is None:
	print("This course cannot be scored. (Does it have assignments?)", file = sys.stderr)
	sys.exit(1)
else:
	print(course.score())
