# Grade Calculator

Calculate your grade in a course by specifying weighted grading categories and entering assignment scores.

## Input format

The calculator uses JSON for serializing course information. An input file might look like this:

	{
		"name": "math",
		"categories": [
			{
				"name": "homework",
				"weight": 0.5,
				"weighting": true,
				"assignments": [
					{
						"name": "opossum project",
						"earned": 42.5,
						"possible": 50,
						"weight": 1
					}, ...
				]
			}, ...
		]
	}

Each input file must describe exactly one course.

### Course fields

* `name`: an identifier for the course (optional)
* `categories`: categories associated with the course

### Category fields

* `name`: an identifier for the category (optional)
* `weight`: the weight of scores in the category relative to other category weights
* `weighting`: whether assignments in this category may specify weights relative to one another (optional; default: `false`)

	For categories that don't use weighting, scores are determined by the totals of points earned and possible rather than a weighted sum of assignment scores (effectively weighting assignments by their possible point values). Not using weighting makes it possible for "extra credit" assignments (with `0` possible points) to be scored.
* `assignments`: assignments associated with the category

### Assignment fields

* `name`: an identifier for the assignment (optional)
* `earned`: the number of points earned for the assignment
* `possible`: the number of points possible for the assignment
* `weight`: the weight of the assignment relative to others in its category (optional; default: `1.0`)

	This field only takes effect if the assignment's category uses weighting.

All point values and weights must be nonnegative.

## Grade calculation

Calculations are based on weighted averages, with the overall (course) score being a weighted average of category scores, which are in turn averages of their assignments' scores. Assignment scores can be weighted within a category, but in most cases it is appropriate for them to be unweighted.

Assignments in categories with weightings enabled will only count if their possible point values are nonzero. Similarly, a category will only count if it has at least one scoring assignment, and (if weighting is disabled for the category) if at least one assignment has a nonzero possible point value. Also, a score will only be reported for a course if it has at least one scorable category. Weightings for assignments and categories are renormalized to exclude unscorable items when scores are calculated.

Apart from being nonnegative, there are no restrictions on weights for assignments and categories. For instance, users may elect to use percentage values like `75` and `40` or fractional values like `0.75` and `0.4`, or another system entirely. All that matters is the relative sizes of weights within a category or course.

## Usage

Assuming a course file `data.json` exists and Python 3.4 or later is installed, place the source files in a common directory and run the program as follows:

	python3 calculator.py < data.json

The program will print the overall score for the course as a fraction out of 1.

## Future features

* graphical interface
