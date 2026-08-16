**Annex C**

**Code Quality Assessment Worksheet**

**Section: 9-Samat                            Score:____**

**C# / Name: #4, #5, #6                       Date: 08/15/2026**


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

_________________________________________________________________

_________________________________________________________________

_________________________________________________________________

Checklist to guide your answer:

| PseudoCode 1 | Pseudocode 2 |
|---|---|
| [ ] Does the algorithm use one loop or two nested loops? | [ ] Does the algorithm use one loop or two nested loops? |
| [ ] Does the algorithm repeat work unnecessarily? | [ ] Does the algorithm repeat work unnecessarily? |
| [ ] Which algorithm finishes in fewer steps? | [ ] Which algorithm finishes in fewer steps? |

2. Readability

Which algorithm is easier to understand at first glance? What makes it clearer?

It’s easier for me to understand the flow of Pseudocode 1 because the code is rationally concise and adequate for simply looking for the maximum number. Pseudocode 2 however makes use of multiple indentations and for loops which seems to overcomplicate and overengineer the solution.

Checklist to guide your answer:

| PseudoCode 1 | Pseudocode 2 |
|---|---|
| [ ] Are variable names meaningful (e.g., max vs. bigger)? | [ ] Are variable names meaningful (e.g., max vs. bigger)? |
| [ ] Is the logic simple or complicated? | [ ] Is the logic simple or complicated? |
| [ ] Are there fewer lines of code? | [ ] Are there fewer lines of code? |

3. Maintainability
   
If you had to add a new feature (like finding both max and min), which algorithm would be easier to update? Why?

The algorithm of Pseudocode 1 would be easier to update as it is less cluttered and there are fewer lines of code that you need to consider when changing the flow of the program. Whereas in Pseudocode 2, the usage of multiple lines, loops, and if-statements require you to reorganize everything upon a new addition.

Checklist to guide your answer:

| PseudoCode 1 | Pseudocode 2 |
|---|---|
| [ ] Is the structure straightforward? | [ ] Is the structure straightforward? |
| [ ] Would adding new steps break the code easily? | [ ] Would adding new steps break the code easily? |
| [ ] Is there less chance of errors when updating? | [ ] Is there less chance of errors when updating? |

4. Testability
   
Which algorithm is easier to test with different inputs? Why?

_________________________________________________________________

_________________________________________________________________

_________________________________________________________________

Checklist to guide your answer:

| PseudoCode 1 | Pseudocode 2 |
|---|---|
| [ ] Can you test with small lists easily? | [ ] Can you test with small lists easily? |
| [ ] Does the algorithm have fewer conditions to check? | [ ] Does the algorithm have fewer conditions to check? |
| [ ] Is the output predictable and clear? | [ ] Is the output predictable and clear? |

5. Security
   
Imagine the input list comes from a user. What should the algorithm check to avoid errors or misuse?

_________________________________________________________________

_________________________________________________________________

_________________________________________________________________

Checklist to guide your answer:

| PseudoCode 1 | Pseudocode 2 |
|---|---|
| [ ] Does the algorithm check if the list is empty? | [ ] Does the algorithm check if the list is empty? |
| [ ] Does it handle invalid inputs (like letters instead of numbers)? | [ ] Does it handle invalid inputs (like letters instead of       numbers)? |
| [ ] Does it avoid crashing when inputs are unusual? | [ ] Does it avoid crashing when inputs are unusual? |

6. Final Answer
Based on your answers from 1 to 5, which one is the better algorithm that you will use to solve the problem of finding the highest number? Why? Summarize your answer

_________________________________________________________________

_________________________________________________________________

_________________________________________________________________
