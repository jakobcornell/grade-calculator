from structures import DataError, Assignment, Category, Course
import json

def parse_course(infile):
	crs = json.load(infile)
	course = Course(
		name = crs['name'] if 'name' in crs else None
	)
	for cat in crs['categories']:
		category = Category(
			weight = cat['weight'],
			name = cat['name'] if 'name' in cat else None,
			weighting = cat['weighting'] if 'weighting' in cat else None
		)
		for assn in cat['assignments']:
			assignment = Assignment(
				earned = assn['earned'],
				possible = assn['possible'],
				name = assn['name'] if 'name' in assn else None,
				weight = assn['weight'] if 'weight' in assn else 1
			)
			category.assignments.append(assignment)
		course.categories.append(category)
	return course