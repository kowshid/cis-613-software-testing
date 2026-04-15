## Assignment Instructions

For the attached triangle function, create test suites using the following methods (Make sure to look in the book to see
which have already been identified for you in the 4th or 5th edition. The 4th edition is available to you online through
the GVSU library.):

- Normal Boundary Value Analysis Testing (each variable's bounds are 1..200, inclusive)
- Weak Normal Equivalence Class Testing
- Decision Table-Based Testing
- Your test cases from the 'Unit Testing Frameworks' assignment. If, for some reason, you are not able to use the same
  language as you used previously, document that in your assignment.

Report the _code coverage_ (from ElcEmma for Java and coverage.py for Python) and _mutation score_ for each test suite.
Please be sure to include the number of mutants killed and total mutants.

Based on the results, answer the following questions:

- How does each method do at killing mutants? Why?
- Would other variants of these same methods (e.g., Strong Robust Equivalence Class Testing) perform better at killing
  mutants? Justify your answer via identification of test cases that do or do not improve mutation score and list the
  mutation score.

Identify at least one mutation not killed by any of the previous methods and **either**:

- Create a test to kill the mutation and discuss if the test adds value to the test suite, or
- Explain, given the remaining mutations that are alive, why this is not possible (**Note**: this should mean all
  remaining mutations can not be killed).

### Notes for Java:

**Note 1**: PITest must be set to 'All Mutations' during the analysis above.

You are free to use whatever IDE you like (or no IDE), however, a known working set includes:

- Eclipse 2021-06 R (find it here: https://www.eclipse.org/downloads/packages/release/2021-06/r via the "Eclipse IDE for
Java Developers" choice)
- EclEmma (Included in Eclipse)
- JUnit 5 (Included in Eclipse)
- Pitclipse 2.2.0: Install via Eclipse in ‘Help -> Eclipse Marketplace’ then search for "pitclipse".

**Note 2**: The JUnit test and class must be public and use org.junit.* package imports in order to work with PITest.
See the example test file attached. JUnit Java files should end in test (e.g., TriangleTest for the Triangle class) in
order to ensure they are ignored by PITest.

**Note 3**: Please turn in *.java files for the JUnit tests, and a *.doc, *.docx, or *.pdf for the answers to the
questions and screenshots of mutation results.

### Notes for Python:

**Note 1**: You are free to use whatever versions you like, however the following is known to work on Windows:

- Ensure you have python and pip at the command line (python 3.10 was tested).
- Install mutmut 2.5.0 via the command: pip install mutmut==2.5.0
- Put your triangle.py file in a /src/ folder and your tests (e.g., test_triangle.py) in a /tests/ folder. This is one
  method to ensure mutmut will not mutate your tests.
- Create a setup.cfg file with the following values:

```
[mutmut]
runner=[Path to Python]\\python.exe -m unittest [Path to src and tests folders]/tests/test_triangle.py
paths_to_mutate=[Path to src and tests folders]\\src\\
tests_dir=[Path to src and tests folders]\\tests\\
```

- Be sure to update [Path to Python] and [Path to src and tests folders]. My setup.cfg file looks like:

```
[mutmut]
runner=C:\\Users\\byron\\PycharmProjects\\triangle_mutation\\venv\\Scripts\\python.exe -m unittest C:/Users/byron/PycharmProjects/triangle_mutation/tests/test_triangle.py
paths_to_mutate=C:\\Users\\byron\\PycharmProjects\\triangle_mutation\\src\\
tests_dir=C:\\Users\\byron\\PycharmProjects\\triangle_mutation\\tests\\
```
- Run the following commands:
  - Run "mutmut run" to run your tests with mutations on the source code.
  - Run "mutmut results" to view a summary of your results.
  - Run "mutmut html" to generate an HTML report.

**Note 2**: The setup.cfg file you create, your src folder (containing triangle.py) and your tests folder (containing
test_triangle.py) should all be in the same folder.

**Note 3**: Please turn in *.py files for the Python tests, and a *.doc, *.docx, or *.pdf for the answers to the
questions and screenshots of mutation results.