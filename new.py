import sys
import json

in_file = open(sys.argv[1]) if len(sys.argv) > 1 else sys.stdin

with in_file as data:
  categories = json.load(data)

for category in categories:
  category['include'] = False
  for assignment in category['assignments']:
    if assignment['possible'] > 0:
      assignment['include'] = True
      assignment['score'] = assignment['earned'] / assignment['possible']
    else:
      assignment['include'] = False
  category['assignments'].sort(key = lambda assignment: assignment['score'])
  i = 0
  while category['drop'] > 0 and i < len(category['assignments']):
    if category['assignments'][i]['include']:
      category['assignments'][i]['include'] = False
      category['drop'] -= 1
    i += 1
  for assignment in category['assignments']:
    if assignment['include']:
      category['include'] = True
      break

full_weight = sum([category['weight'] for category in categories if category['include']])
print(categories)
"""
scored_categories = [category for (category, scores) in gradebook.items() if len(scores) > 0 and sum([score[1] for score in scores]) > 0]
if len(scored_categories) == 0:
  raise Exception("No scored categories found.")
full_weight = sum([weights[category] for category in scored_categories])
grade = 0
for category in scored_categories:
  grade += sum([score[0] for score in gradebook[category]]) / sum([score[1] for score in gradebook[category]]) * weights[category] / full_weight
print(grade)
"""
