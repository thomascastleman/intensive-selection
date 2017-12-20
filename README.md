# intensive-selection
*Solution to matching students to intensives based on grade-level biases and individual priorities*

Created by Thomas Castleman and Johnny Lindbergh

## PROBLEM DEFINITION

This algorithm is designed to match students to their preferred intensive, a variant of the <a href="https://en.wikipedia.org/wiki/Stable_marriage_problem" target="_blank">*stable matching problem*</a>. This specific instance is also quite similar to the *Hospitals and Residents Problem*, in which residents must be matched to medical institutions based on both their preferences and those of the institutions themselves.

Certain properties of each student and offering factor into the matching results:
Each student has:
- an age
- a grade
- a list of offerings, ordered by preference

In addition, each offering:
- has a maximum capacity
- **MAY** have either a minimum age or grade

Given these properties, the matching must meet a set of **hard constraints**, but is also tuned to fit **soft constraints** once these are taken care of.

The hard constraints are as follows:
- no student may be matched to an offering with which they would be violating an age or grade restriction
- no offering may be subscribed over its maximum capacity

The soft constraints, which are used afterwards to refine the solution, involve the student’s:
- rating of the offering they are matched with
- age
- grade

Each of these factors may be weighted and scaled to meet the needs of the user, depending on what they consider to bear the greatest importance. 

## ALGORITHM SUMMARY

The solution uses a combination of a <a href="https://en.wikipedia.org/wiki/Backtracking">backtracking technique</a> and the <a href="https://en.wikipedia.org/wiki/2-opt" target="_blank">2-opt local search algorithm</a> for optimization.

Backtracking is used to solve the initial constraint satisfaction problem of creating a matching that does not violate any hard constraints, since the capacity constraints are relaxed enough that it is feasible to use this approach without running into issues of time complexity. 

2-opt is then used to refine this solution and optimize it based on a cost function, which factors in not only the student's rating of the paired intensive but also their grade and age. The weight (aka influence) of each of these factors is tunable through the adjustment of a set of coefficients, which determine how each value contributes to the overall cost of a pairing. 

## RESULTS

<p align="center">
<img src="http://tcastleman.com/imgs/choice_results.png">
</p>

Thus far, matchings with **upwards of 70% of students with their first choice** are feasible, and constructed within seconds. Sample results from a 400 student, 20 offering matching are displayed above.

## EVALUATION

To determine the success of the algorithm, a method to evaluate the effectiveness of a solution was created. Once a matching has been found, this function gathers statistics about the solution such as:

- Percentage of students who received each choice
- Percentage of students per grade who received their first choice
- Percentage full each offering has been subscribed

and logs them to the console. There is also an option for these stats to be plotted for a nice visual representation. 

<p align="center">
<img src="http://tcastleman.com/imgs/eval.png">
</p>

## TEST DATA

In order to test the algorithm and debug, it was necessary to quickly generate reasonable test data, given quantities of students and offerings. To accomplish this, data was produced where:

- student grade is distributed evenly
- age correlates with grade, with some deviation
- rank is composed of choices which are **NOT** uniformly distributed (certain offerings are naturally more popular than others)
- offering max capacities are slightly larger than the ratio of students to offerings
- age or grade restrictions are rare

## USAGE

To run, use the command
```
python -m src.main
```

#### Further reading:

<a href="http://www.dcs.gla.ac.uk/publications/PAPERS/8632/hr.pdf" target="_blank">Hospitals and Residents Problem Description</a>
