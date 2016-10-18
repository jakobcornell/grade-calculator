import sys
import parsing

course = parsing.parse_course(sys.stdin)

print(course.score())
