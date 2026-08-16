**Annex C**

**Code Quality Assessment Worksheet**

**Section: 9-Samat              |              Score:____**

**C# / Name: #4, #5, #6         |              Date: 08/15/2026**


**Instructions:**

The problem: Finding the highest (Maximum) number from a given list of numbers.

**Pseudocode 1**

{

  Algorithm FindMax1(numbers)

    max ← numbers[0]
       For i from 1 to length(numbers)-1

          If numbers[i] > max Then

             max ← numbers[i]

          EndIf

       EndFor

       Return max
  EndAlgorithm
  
  }

**Pseudocode 2**

{

Algorithm FindMax2(numbers)

     For i from 0 to length(numbers)-1bigger ← true

        For j from 0 to length(numbers)-1

           If numbers[j] > numbers[i] Then

              bigger ← false

           EndIf

        EndFor

        If bigger = true Then

           Return numbers[i]

        EndIf

     EndFor
  
EndAlgorithm

}

**Questions with Checklists**

1. Efficiency
   
Which algorithm is faster when the list of numbers is very large? Why?

Pseudocode 1 is much more efficient with a larger dataset, since it only goes through the list once. On the other hand, Pseudocode 2 compares each number with every other number, so it has to do many more comparisons as the list gets bigger.
Checklist to guide your answer:

| PseudoCode 1 | Pseudocode 2 |
|---|---|
| Does the algorithm use one loop or two nested loops? [One loop] | Does the algorithm use one loop or two nested loops? [Two loops]|
| Does the algorithm repeat work unnecessarily? [No] | Does the algorithm repeat work unnecessarily? [Yes]|
| Which algorithm finishes in fewer steps? [Algorithm 1] | Which algorithm finishes in fewer steps? [Algorithm 1] |

2. Readability

Which algorithm is easier to understand at first glance? What makes it clearer?

It’s easier for me to understand the flow of Pseudocode 1 because the code is rationally concise and adequate for simply looking for the maximum number. Pseudocode 2 however makes use of multiple indentations and for loops which seems to overcomplicate and overengineer the solution.

Checklist to guide your answer:

| PseudoCode 1 | Pseudocode 2 |
|---|---|
| Are variable names meaningful (e.g., max vs. bigger)? [Yes] | Are variable names meaningful (e.g., max vs. bigger)? [No] |
| Is the logic simple or complicated? [Simple] | [ ] Is the logic simple or complicated? [Complicated] |
| Are there fewer lines of code? [Yes] | Are there fewer lines of code? [No] |

3. Maintainability
   
If you had to add a new feature (like finding both max and min), which algorithm would be easier to update? Why?

The algorithm of Pseudocode 1 would be easier to update as it is less cluttered and there are fewer lines of code that you need to consider when changing the flow of the program. Whereas in Pseudocode 2, the usage of multiple lines, loops, and if-statements require you to reorganize everything upon a new addition.

Checklist to guide your answer:

| PseudoCode 1 | Pseudocode 2 |
|---|---|
| Is the structure straightforward? [Yes] | Is the structure straightforward? [No] |
| Would adding new steps break the code easily? [No] | Would adding new steps break the code easily? [Yes] |
| Is there less chance of errors when updating? [Yes] | Is there less chance of errors when updating? [No] |

4. Testability
   
Which algorithm is easier to test with different inputs? Why?

PseudoCode 1 is easier to test because it has a simpler process for finding the largest number. You can try different lists, such as lists with positive numbers, negative numbers, or repeated numbers, and easily check whether the answer is correct. PseudoCode 2 is harder to test because it compares every number with all the other numbers, creating many more comparisons to check. Both algorithms have predictable outputs, but PseudoCode 1 has fewer conditions and is easier to understand and verify.
Checklist to guide your answer:

| PseudoCode 1 | Pseudocode 2 |
|---|---|
| Can you test with small lists easily? [Yes] | Can you test with small lists easily? [No] |
| Does the algorithm have fewer conditions to check? [Yes] | Does the algorithm have fewer conditions to check? [No] |
| Is the output predictable and clear? [Yes] | Is the output predictable and clear? [No] |

5. Security
   
Imagine the input list comes from a user. What should the algorithm check to avoid errors or misuse?

The algorithm should check for inputs that are letters or special characters as they do not comply with the required data type (floats and/or integers).

Checklist to guide your answer:

| PseudoCode 1 | Pseudocode 2 |
|---|---|
| Does the algorithm check if the list is empty? [No] | Does the algorithm check if the list is empty? [No] |
| Does it handle invalid inputs (like letters instead of numbers)? [No] | Does it handle invalid inputs (like letters instead of       numbers)? [No] |
| Does it avoid crashing when inputs are unusual? [No] | Does it avoid crashing when inputs are unusual? [No] |

6. Final Answer
Based on your answers from 1 to 5, which one is the better algorithm that you will use to solve the problem of finding the highest number? Why? Summarize your answer

_________________________________________________________________

_________________________________________________________________

_________________________________________________________________
