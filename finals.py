

print("==============================================")
print("          PYTHON LEARNING TUTORIAL")
print("==============================================")
print("Welcome to my Python Learning Tutorial!")


def show_lesson(title, explanation, example, output):

    print("\n==============================================")
    print("             " + title.upper())
    print("==============================================")

    print("\nLESSON EXPLANATION:")
    print(explanation)

    print("\nCODE EXAMPLE:")
    print(example)

    print("\nEXPECTED OUTPUT:")
    print(output)

    input("\nPress Enter to continue...")


def take_quiz(questions, module_name):

    score = 0

    print("\n==============================================")
    print("             " + module_name.upper() + " QUIZ")
    print("==============================================")

    for number, question in enumerate(questions, start=1):

        print("\n" + str(number) + ". " + question[0])

        for option in question[1]:
            print(option)

        answer = input("Your answer (A, B, or C): ").strip().upper()

        while answer not in ["A", "B", "C"]:
            print("Please enter only A, B, or C.")
            answer = input("Your answer: ").strip().upper()

        if answer == question[2]:
            print("Correct! Well done!")
            score += 1
        else:
            print("Incorrect!")
            print("Correct answer: " + question[2])

    print("\n==============================================")
    print("                 QUIZ RESULTS")
    print("==============================================")

    print("Module:", module_name)
    print("Your Score:", score, "/", len(questions))

    if score == len(questions):
        print("Excellent! Perfect score!")
    elif score >= len(questions) / 2:
        print("Good job! Keep practicing!")
    else:
        print("Nice try! Review the lessons and try again.")

    input("\nPress Enter to continue...")


modules = [

    {
        "title": "Introduction to Programming",

        "lessons": [

            (
                "What is Programming?",
                """Programming is the process of writing instructions
that tell a computer what to do.

Computers cannot understand human instructions
directly. Programmers use programming languages
to communicate with computers.

Programming is used to create applications,
websites, games, and computer systems.""",

                'print("Hello, World!")',

                "Hello, World!"
            ),

            (
                "What is a Programming Language?",
                """A programming language is a language used
to create instructions for a computer.

It allows programmers to communicate with
computers and develop different programs.

Examples include Python, Java, C++, and JavaScript.""",

                'print("I am learning Python")',

                "I am learning Python"
            ),

            (
                "What is Python?",
                """Python is a high-level programming language
that is known for being simple and easy to read.

It was created by Guido van Rossum and was first
released in 1991.

Python is commonly used in web development,
data analysis, artificial intelligence, automation,
and software development.""",

                'print("Welcome to Python Programming!")',

                "Welcome to Python Programming!"
            ),

            (
                "Why Learn Python?",
                """Python is beginner-friendly because its code
is easier to read and understand.

Some reasons to learn Python are:

1. It has simple and readable syntax.
2. It can be used in many different fields.
3. It has many built-in functions and libraries.
4. It has a large programming community.
5. It is useful for creating real-world projects.""",

                'name = "Student"\nprint("Hello", name)',

                "Hello Student"
            ),

            (
                "Applications of Python",
                """Python can be used for many purposes.

1. Web Development - creating websites.
2. Data Science - studying and analyzing data.
3. Artificial Intelligence - developing smart systems.
4. Automation - performing repeated tasks.
5. Game Development - creating simple games.
6. Education - teaching programming concepts.""",

                'print("Python is used in many fields.")',

                "Python is used in many fields."
            )
        ],

        "quiz": [
            (
                "What is programming?",
                [
                    "A. Giving instructions to a computer",
                    "B. Playing computer games",
                    "C. Drawing pictures"
                ],
                "A"
            ),
            (
                "Who created Python?",
                [
                    "A. Bill Gates",
                    "B. Guido van Rossum",
                    "C. Mark Zuckerberg"
                ],
                "B"
            ),
            (
                "When was Python first released?",
                [
                    "A. 1991",
                    "B. 2005",
                    "C. 2015"
                ],
                "A"
            ),
            (
                "Which is a programming language?",
                [
                    "A. Keyboard",
                    "B. Monitor",
                    "C. Python"
                ],
                "C"
            ),
            (
                "Which is one use of Python?",
                [
                    "A. Web development",
                    "B. Washing clothes",
                    "C. Charging a computer"
                ],
                "A"
            )
        ]
    },


    {
        "title": "Python Basic Syntax",

        "lessons": [

            (
                "What is Python Syntax?",
                """Syntax refers to the rules and structure
that programmers must follow when writing code.

Python code must follow the correct syntax
so the computer can understand and execute it.

Incorrect syntax can cause a SyntaxError.""",

                'print("Hello Python")',

                "Hello Python"
            ),

            (
                "Case Sensitivity",
                """Python is case-sensitive.

This means uppercase and lowercase letters
are treated as different characters.

For example, name and Name are two
different variable names.

You must use the correct capitalization.""",

                'name = "Jade"\nName = "Alex"\nprint(name)\nprint(Name)',

                "Jade\nAlex"
            ),

            (
                "Indentation",
                """Indentation means adding spaces at the
beginning of a line of code.

Python uses indentation to identify a group
of statements that belong together.

Four spaces are commonly used for indentation.
Incorrect indentation can cause an error.""",

                'if 10 > 5:\n    print("Ten is greater than five")',

                "Ten is greater than five"
            ),

            (
                "Python Statements",
                """A statement is an instruction written
in a Python program.

A statement tells the computer to perform
a particular action.

Examples include assigning a value to a variable,
printing information, and checking a condition.""",

                'name = "Jade"\nprint(name)',

                "Jade"
            ),

            (
                "Python Keywords",
                """Keywords are special reserved words in Python.

They have specific meanings and cannot be used
as ordinary variable names.

Examples include:

if, else, elif, for, while, break,
continue, True, False, and None.""",

                'if True:\n    print("This is a keyword example")',

                "This is a keyword example"
            )
        ],

        "quiz": [
            (
                "What does syntax mean?",
                [
                    "A. Rules for writing code",
                    "B. Computer hardware",
                    "C. Internet connection"
                ],
                "A"
            ),
            (
                "Is Python case-sensitive?",
                [
                    "A. No",
                    "B. Yes",
                    "C. Only sometimes"
                ],
                "B"
            ),
            (
                "What is indentation?",
                [
                    "A. Spaces at the beginning of a line",
                    "B. Deleting a program",
                    "C. Closing a window"
                ],
                "A"
            ),
            (
                "Which is a Python keyword?",
                [
                    "A. keyboard",
                    "B. monitor",
                    "C. if"
                ],
                "C"
            ),
            (
                "What can incorrect syntax cause?",
                [
                    "A. SyntaxError",
                    "B. More memory",
                    "C. Better internet"
                ],
                "A"
            )
        ]
    },


    {
        "title": "Printing Output",

        "lessons": [

            (
                "What is Output?",
                """Output is the information displayed by
a computer after processing instructions.

In Python, the print() function is commonly
used to show output on the screen.

Output can be text, numbers, or results
of calculations.""",

                'print("Hello!")',

                "Hello!"
            ),

            (
                "The print() Function",
                """The print() function displays information
on the screen.

It is one of the most commonly used
functions in Python.

You can use it to display messages,
values, and results.""",

                'print("Welcome to my program!")',

                "Welcome to my program!"
            ),

            (
                "Printing Text",
                """Text is called a string in Python.

Text must be placed inside quotation marks.
You can use single or double quotation marks.

The quotation marks tell Python that
the information is text.""",

                'print("Good morning!")\nprint(\'Hello students!\')',

                "Good morning!\nHello students!"
            ),

            (
                "Printing Numbers",
                """Numbers can be displayed without quotation marks.

Python can display whole numbers and decimal
numbers using the print() function.

When numbers are placed inside quotation marks,
Python treats them as text instead.""",

                'print(100)\nprint(25.50)\nprint(10 + 5)',

                "100\n25.5\n15"
            ),

            (
                "Printing Multiple Values",
                """The print() function can display multiple
values in one statement.

By default, Python separates the values
with a space.

You can also use the sep parameter
to change the separator.""",

                'print("Jade", 17, "Student")\nprint("A", "B", "C", sep="-")',

                "Jade 17 Student\nA-B-C"
            ),

            (
                "Using Escape Characters",
                """Escape characters are special characters
used inside strings.

\\n creates a new line.
\\t adds a tab space.
\\\\ displays a backslash.

They help organize the appearance of output.""",

                'print("Hello\\nPython")\nprint("Name:\\tJade")',

                "Hello\nPython\nName:    Jade"
            )
        ],

        "quiz": [
            (
                "Which function displays output?",
                [
                    "A. input()",
                    "B. print()",
                    "C. type()"
                ],
                "B"
            ),
            (
                "What is text called in Python?",
                [
                    "A. String",
                    "B. Integer",
                    "C. Boolean"
                ],
                "A"
            ),
            (
                "Which is a correct way to print text?",
                [
                    'A. print(Hello)',
                    'B. print("Hello")',
                    'C. print Hello'
                ],
                "B"
            ),
            (
                "What is the output of print(5 + 5)?",
                [
                    "A. 55",
                    "B. 5 + 5",
                    "C. 10"
                ],
                "C"
            ),
            (
                "Which escape character creates a new line?",
                [
                    "A. \\n",
                    "B. \\t",
                    "C. \\\\"
                ],
                "A"
            )
        ]
    },



    {
        "title": "Python Comments",

        "lessons": [

            (
                "What are Comments?",
                """Comments are notes written inside a program
to explain what the code does.

Python ignores comments when executing
the program.

Comments help programmers understand
and organize their code.""",

                '# This is a comment\nprint("Hello Python")',

                "Hello Python"
            ),

            (
                "Single-Line Comments",
                """A single-line comment begins with
the hash symbol (#).

Everything after the # symbol on that line
is treated as a comment.

It is useful for writing short explanations.""",

                '# Display a welcome message\nprint("Welcome!")',

                "Welcome!"
            ),

            (
                "Inline Comments",
                """An inline comment is written on the same
line as a statement.

It explains a specific part of the code.

Use inline comments only when they make
the program easier to understand.""",

                'age = 17  # Store the student age\nprint(age)',

                "17"
            ),

            (
                "Multi-Line Comments",
                """Python does not have a special symbol
made only for multi-line comments.

You can use the # symbol on several lines.

Triple-quoted strings are also often used
for documentation, such as docstrings.""",

                '# This is line one\n# This is line two\n# This is line three\nprint("Done")',

                "Done"
            ),

            (
                "Why are Comments Important?",
                """Comments help programmers remember
the purpose of their code.

They make programs easier to read,
understand, maintain, and update.

Comments are especially useful when
working on large projects with other people.""",

                '# Calculate the total price\nprice = 20\nquantity = 3\ntotal = price * quantity\nprint(total)',

                "60"
            )
        ],

        "quiz": [
            (
                "Which symbol starts a Python comment?",
                [
                    "A. #",
                    "B. @",
                    "C. $"
                ],
                "A"
            ),
            (
                "Does Python execute ordinary comments?",
                [
                    "A. Yes",
                    "B. No",
                    "C. Always"
                ],
                "B"
            ),
            (
                "What is the purpose of comments?",
                [
                    "A. Explain code",
                    "B. Delete variables",
                    "C. Shut down the computer"
                ],
                "A"
            ),
            (
                "What is an inline comment?",
                [
                    "A. A comment inside a computer",
                    "B. A comment on the same line as code",
                    "C. A comment that runs a loop"
                ],
                "B"
            ),
            (
                "Which symbol is used in single-line comments?",
                [
                    "A. #",
                    "B. %",
                    "C. &"
                ],
                "A"
            )
        ]
    },


    {
        "title": "Variables, Constants, and Data Types in Python",

        "lessons": [

            (
                "What are Variables?",
                """A variable is a name used to store
information in a program.

The value of a variable can change
while the program is running.

Variables make it easier to store
and use information.""",

                'name = "Jade"\nage = 17\nprint(name)\nprint(age)',

                "Jade\n17"
            ),

            (
                "Creating and Naming Variables",
                """Variables are created when you assign
a value using the equal sign (=).

Variable names can contain letters,
numbers, and underscores.

A variable name cannot start with a number.
Variable names should also be meaningful.

Python variable names are case-sensitive.""",

                'student_name = "Jade"\nstudent_age = 17\nprint(student_name)\nprint(student_age)',

                "Jade\n17"
            ),

            (
                "Changing Variable Values",
                """The value of a variable can be changed
by assigning a new value to it.

The latest assigned value is the one
that will be stored in the variable.""",

                'score = 80\nscore = 95\nprint(score)',

                "95"
            ),

            (
                "What are Constants?",
                """A constant is a value that is intended
to remain unchanged throughout a program.

Python does not have a special command
that makes a variable completely constant.

By convention, constant names are written
in uppercase letters.""",

                'PI = 3.14159\nSCHOOL_NAME = "ABC School"\nprint(PI)\nprint(SCHOOL_NAME)',

                "3.14159\nABC School"
            ),

            (
                "Assigning Multiple Variables",
                """Python allows you to assign values
to multiple variables in one statement.

You can also assign the same value
to different variables.

This can make some code shorter and easier
to write.""",

                'name, age, grade = "Jade", 17, 95\nprint(name)\nprint(age)\nprint(grade)',

                "Jade\n17\n95"
            ),

            (
                "Using Variables in Calculations",
                """Variables can be used in mathematical
operations and expressions.

Python uses the values stored in variables
to calculate the result.

This is useful when creating programs
that process information.""",

                'price = 20\nquantity = 3\ntotal = price * quantity\nprint(total)',

                "60"
            )
        ],

        "quiz": [
            (
                "What is a variable?",
                [
                    "A. A name used to store a value",
                    "B. A computer screen",
                    "C. A programming error"
                ],
                "A"
            ),
            (
                "Which symbol assigns a value?",
                [
                    "A. ==",
                    "B. =",
                    "C. !="
                ],
                "B"
            ),
            (
                "How are constants commonly written?",
                [
                    "A. lowercase",
                    "B. UPPERCASE",
                    "C. With spaces"
                ],
                "B"
            ),
            (
                "Can a variable's value change?",
                [
                    "A. Yes",
                    "B. No",
                    "C. Never"
                ],
                "A"
            ),
            (
                "Which is a valid variable name?",
                [
                    "A. 2name",
                    "B. student_name",
                    "C. student-name"
                ],
                "B"
            )
        ]
    },


    {
        "title": "Basic Data Types in Python",

        "lessons": [

            (
                "What are Data Types?",
                """Data types identify the kind of information
stored in a variable.

They help Python understand how a value
should be used in a program.

Common Python data types include:
int, float, str, bool, and complex.""",

                'age = 17\nname = "Jade"\nprint(type(age))\nprint(type(name))',

                "<class 'int'>\n<class 'str'>"
            ),

            (
                "Integer (int)",
                """An integer is a whole number without
a decimal point.

Examples include 1, 10, 100, and -5.

Integers are commonly used for counting,
ages, quantities, and scores.""",

                'age = 17\nnumber = -5\nprint(age)\nprint(number)\nprint(type(age))',

                "17\n-5\n<class 'int'>"
            ),

            (
                "Float",
                """A float is a number that contains
a decimal point.

Examples include 3.14, 10.5, and 99.99.

Floats are useful for measurements,
prices, and calculations that need decimals.""",

                'price = 25.50\nheight = 5.5\nprint(price)\nprint(type(height))',

                "25.5\n<class 'float'>"
            ),

            (
                "String (str)",
                """A string is a data type used to store text.

Strings are written inside single or double
quotation marks.

They can contain letters, numbers,
spaces, and special characters.""",

                'name = "Jade"\nmessage = "Hello Python"\nprint(name)\nprint(message)\nprint(type(name))',

                "Jade\nHello Python\n<class 'str'>"
            ),

            (
                "Boolean (bool)",
                """A Boolean is a data type that has
only two possible values: True or False.

Boolean values are often used in conditions
and decision-making statements.

Remember that True and False begin
with uppercase letters in Python.""",

                'is_student = True\nis_absent = False\nprint(is_student)\nprint(is_absent)\nprint(type(is_student))',

                "True\nFalse\n<class 'bool'>"
            ),

            (
                "Checking Data Types",
                """The type() function identifies the data type
of a value or variable.

It helps programmers understand what kind
of information is stored.

This is useful when checking values
and finding programming errors.""",

                'number = 100\nprice = 20.5\nname = "Jade"\nprint(type(number))\nprint(type(price))\nprint(type(name))',

                "<class 'int'>\n<class 'float'>\n<class 'str'>"
            )
        ],

        "quiz": [
            (
                "Which data type stores whole numbers?",
                [
                    "A. int",
                    "B. str",
                    "C. bool"
                ],
                "A"
            ),
            (
                "Which data type stores decimal numbers?",
                [
                    "A. int",
                    "B. float",
                    "C. str"
                ],
                "B"
            ),
            (
                "Which data type stores text?",
                [
                    "A. bool",
                    "B. float",
                    "C. str"
                ],
                "C"
            ),
            (
                "What are the two Boolean values?",
                [
                    "A. True and False",
                    "B. Yes and No",
                    "C. One and Two"
                ],
                "A"
            ),
            (
                "Which function checks a data type?",
                [
                    "A. print()",
                    "B. type()",
                    "C. input()"
                ],
                "B"
            )
        ]
    },


    {
        "title": "Arithmetic Operators and Expressions",

        "lessons": [

            (
                "What are Arithmetic Operators?",
                """Arithmetic operators are symbols used
to perform mathematical calculations.

Python supports addition, subtraction,
multiplication, division, and other operations.

They are commonly used in calculators,
school programs, and business applications.""",

                'print(10 + 5)\nprint(10 - 5)',

                "15\n5"
            ),

            (
                "Addition and Subtraction",
                """The addition operator (+) adds two values.

The subtraction operator (-) finds
the difference between two values.

These operators work with numbers
and numeric variables.""",

                'a = 20\nb = 5\nprint(a + b)\nprint(a - b)',

                "25\n15"
            ),

            (
                "Multiplication and Division",
                """The multiplication operator (*) multiplies
two values.

The division operator (/) divides one value
by another.

Regular division using / usually produces
a float result.""",

                'print(4 * 3)\nprint(12 / 3)',

                "12\n4.0"
            ),

            (
                "Floor Division and Modulus",
                """Floor division (//) divides two numbers
and rounds the result down to a whole number.

Modulus (%) returns the remainder
after division.

These operators are useful for calculations
and checking whether numbers are even or odd.""",

                'print(10 // 3)\nprint(10 % 3)',

                "3\n1"
            ),

            (
                "Exponentiation",
                """The exponentiation operator (**) raises
a number to a specified power.

For example, 2 ** 3 means 2 multiplied
by itself three times.

It is useful for mathematical calculations.""",

                'print(2 ** 3)\nprint(5 ** 2)',

                "8\n25"
            ),

            (
                "Operator Precedence",
                """Operator precedence determines the order
in which Python performs calculations.

Multiplication and division are performed
before addition and subtraction.

Parentheses can be used to control
the order of calculations.""",

                'print(2 + 3 * 4)\nprint((2 + 3) * 4)',

                "14\n20"
            )
        ],

        "quiz": [
            (
                "Which operator is used for addition?",
                [
                    "A. +",
                    "B. -",
                    "C. *"
                ],
                "A"
            ),
            (
                "Which operator is used for multiplication?",
                [
                    "A. /",
                    "B. *",
                    "C. %"
                ],
                "B"
            ),
            (
                "What is the result of 10 % 3?",
                [
                    "A. 3",
                    "B. 0",
                    "C. 1"
                ],
                "C"
            ),
            (
                "What is the result of 2 ** 3?",
                [
                    "A. 6",
                    "B. 8",
                    "C. 9"
                ],
                "B"
            ),
            (
                "What is the result of 2 + 3 * 4?",
                [
                    "A. 20",
                    "B. 14",
                    "C. 24"
                ],
                "B"
            )
        ]
    },


    {
        "title": "Basic Input and Output in Python",

        "lessons": [

            (
                "What is Input and Output?",
                """Input is information entered by a user
into a program.

Output is the information displayed
by the program.

Python uses input() to receive information
and print() to display information.""",

                'name = input("Enter your name: ")\nprint("Hello", name)',

                "If the user enters Jade:\nHello Jade"
            ),

            (
                "The input() Function",
                """The input() function allows a program
to ask the user for information.

The program waits until the user enters
a value and presses Enter.

By default, input() returns the entered
information as a string.""",

                'name = input("Enter your name: ")\nprint(name)',

                "If the user enters Alex:\nAlex"
            ),

            (
                "Displaying User Input",
                """You can use print() to display
information entered by a user.

You can combine a message with the
information entered by the user.

This makes programs more interactive.""",

                'color = input("Favorite color: ")\nprint("Your favorite color is", color)',

                "If the user enters Blue:\nYour favorite color is Blue"
            ),

            (
                "Converting Input to Integer",
                """The int() function converts a value
into an integer when the value is valid.

It is useful when the user enters whole numbers
that will be used in calculations.

Without conversion, input is treated as text.""",

                'age = int(input("Enter your age: "))\nprint(age + 1)',

                "If the user enters 17:\n18"
            ),

            (
                "Converting Input to Float",
                """The float() function converts a value
into a decimal number when the value is valid.

It is useful for prices, measurements,
and calculations involving decimals.""",

                'price = float(input("Enter price: "))\nprint(price + 10)',

                "If the user enters 25.5:\n35.5"
            ),

            (
                "Simple Interactive Program",
                """You can combine input(), variables,
calculations, and print() to create
a simple interactive program.

This example asks for two numbers
and displays their total.""",

                'first = int(input("First number: "))\nsecond = int(input("Second number: "))\ntotal = first + second\nprint("Total:", total)',

                "If the user enters 10 and 5:\nTotal: 15"
            )
        ],

        "quiz": [
            (
                "Which function receives user input?",
                [
                    "A. print()",
                    "B. input()",
                    "C. type()"
                ],
                "B"
            ),
            (
                "What does input() return by default?",
                [
                    "A. String",
                    "B. Integer",
                    "C. Boolean"
                ],
                "A"
            ),
            (
                "Which function converts a value to an integer?",
                [
                    "A. str()",
                    "B. float()",
                    "C. int()"
                ],
                "C"
            ),
            (
                "Which function displays information?",
                [
                    "A. print()",
                    "B. input()",
                    "C. int()"
                ],
                "A"
            ),
            (
                "Which function converts a value to a decimal number?",
                [
                    "A. int()",
                    "B. float()",
                    "C. bool()"
                ],
                "B"
            )
        ]
    },


    {
        "title": "Conditional Statements in Python",

        "lessons": [

            (
                "What are Conditional Statements?",
                """Conditional statements allow a program
to make decisions based on conditions.

They help a program choose which instructions
to perform depending on whether a condition
is True or False.

They are commonly used in applications,
grading systems, and simple games.""",

                'age = 18\nif age >= 18:\n    print("Adult")',

                "Adult"
            ),

            (
                "The if Statement",
                """The if statement runs a block of code
only when its condition is True.

If the condition is False, the code
inside the if block is skipped.

A colon is placed after the condition,
and the next line must be indented.""",

                'number = 10\nif number > 5:\n    print("Greater than five")',

                "Greater than five"
            ),

            (
                "The if-else Statement",
                """The if-else statement is used when
there are two possible results.

The if block runs when the condition
is True.

The else block runs when the condition
is False.""",

                'age = 15\nif age >= 18:\n    print("Adult")\nelse:\n    print("Minor")',

                "Minor"
            ),

            (
                "The if-elif-else Statement",
                """The elif keyword means else if.

It allows a program to check multiple
conditions in order.

Python checks each condition until
one becomes True.

The else block runs if none of the
conditions are True.""",

                'grade = 90\nif grade >= 90:\n    print("Excellent")\nelif grade >= 75:\n    print("Passed")\nelse:\n    print("Failed")',

                "Excellent"
            ),

            (
                "Nested if Statements",
                """A nested if statement is an if statement
placed inside another if statement.

It is useful when a program needs
to check one condition after another.

Each nested block must have the
correct indentation.""",

                'age = 20\nhas_id = True\nif age >= 18:\n    if has_id:\n        print("Access allowed")',

                "Access allowed"
            ),

            (
                "Using Comparison Operators in Conditions",
                """Comparison operators compare two values
and return either True or False.

Common comparison operators include:

== Equal to
!= Not equal to
> Greater than
< Less than
>= Greater than or equal to
<= Less than or equal to""",

                'number = 10\nprint(number == 10)\nprint(number > 5)\nprint(number < 5)',

                "True\nTrue\nFalse"
            )
        ],

        "quiz": [
            (
                "Which keyword checks a condition?",
                [
                    "A. if",
                    "B. print",
                    "C. input"
                ],
                "A"
            ),
            (
                "When does the else block run?",
                [
                    "A. When the if condition is True",
                    "B. When the if condition is False",
                    "C. Every time"
                ],
                "B"
            ),
            (
                "What does elif mean?",
                [
                    "A. Else if",
                    "B. End loop",
                    "C. Exit program"
                ],
                "A"
            ),
            (
                "Which operator means equal to?",
                [
                    "A. =",
                    "B. !=",
                    "C. =="
                ],
                "C"
            ),
            (
                "What is a nested if statement?",
                [
                    "A. An if statement inside another if",
                    "B. A type of variable",
                    "C. A printing function"
                ],
                "A"
            )
        ]
    },


    {
        "title": "Logical Operators",

        "lessons": [

            (
                "What are Logical Operators?",
                """Logical operators are used to combine
or change conditions in Python.

They return Boolean results:
True or False.

Python has three main logical operators:
and, or, and not.""",

                'print(True and True)\nprint(True or False)\nprint(not True)',

                "True\nTrue\nFalse"
            ),

            (
                "The AND Operator",
                """The and operator returns True only when
both conditions are True.

If one or both conditions are False,
the result is False.

It is useful when two requirements
must both be satisfied.""",

                'age = 20\nhas_id = True\nprint(age >= 18 and has_id == True)',

                "True"
            ),

            (
                "The OR Operator",
                """The or operator returns True when
at least one condition is True.

It returns False only when both
conditions are False.

It is useful when there are different
ways to satisfy a requirement.""",

                'has_ticket = True\nhas_pass = False\nprint(has_ticket or has_pass)',

                "True"
            ),

            (
                "The NOT Operator",
                """The not operator reverses a Boolean value.

If a condition is True, not changes
the result to False.

If a condition is False, not changes
the result to True.""",

                'is_raining = False\nprint(not is_raining)',

                "True"
            ),

            (
                "Combining Logical Operators",
                """You can combine and, or, and not
to create more complex conditions.

Parentheses can help organize conditions
and make them easier to understand.

Logical operators are often used with
if statements.""",

                'age = 20\nhas_id = True\nif age >= 18 and has_id:\n    print("You may enter")',

                "You may enter"
            ),

            (
                "Logical Operators and Boolean Results",
                """Logical expressions always produce
a Boolean result.

You can use print() to display the result
of a logical expression.

These results can also be stored
inside Boolean variables.""",

                'result = (10 > 5) and (8 < 12)\nprint(result)\nprint(type(result))',

                "True\n<class 'bool'>"
            )
        ],

        "quiz": [
            (
                "Which are the three logical operators?",
                [
                    "A. +, -, *",
                    "B. and, or, not",
                    "C. if, else, elif"
                ],
                "B"
            ),
            (
                "When does and return True?",
                [
                    "A. Both conditions are True",
                    "B. Both conditions are False",
                    "C. One condition is False"
                ],
                "A"
            ),
            (
                "When does or return True?",
                [
                    "A. Both conditions are False",
                    "B. At least one condition is True",
                    "C. Only when both are False"
                ],
                "B"
            ),
            (
                "What does not do?",
                [
                    "A. Adds numbers",
                    "B. Repeats code",
                    "C. Reverses a Boolean result"
                ],
                "C"
            ),
            (
                "What is the result of True and False?",
                [
                    "A. True",
                    "B. False",
                    "C. None"
                ],
                "B"
            )
        ]
    },

    {
        "title": "Introduction to Iteration and Loops",

        "lessons": [

            (
                "What is Iteration?",
                """Iteration is the process of repeating
a set of instructions multiple times.

It helps programmers avoid writing
the same code repeatedly.

Iteration is useful when displaying numbers,
processing lists, and repeating tasks.""",

                'for number in range(1, 4):\n    print(number)',

                "1\n2\n3"
            ),

            (
                "What are Loops?",
                """A loop is a programming structure
that repeats a block of code.

Python has two common types of loops:

1. For Loop
2. While Loop

Loops make programs shorter and more efficient.""",

                'for x in range(3):\n    print("Hello")',

                "Hello\nHello\nHello"
            ),

            (
                "The For Loop",
                """A for loop repeats a block of code
for each item in a sequence.

It is commonly used when you know
how many times you want to repeat
an instruction or when processing
items in a collection.""",

                'for number in range(1, 6):\n    print(number)',

                "1\n2\n3\n4\n5"
            ),

            (
                "The While Loop",
                """A while loop repeats a block of code
as long as its condition remains True.

The loop stops when the condition
becomes False.

You must make sure the condition can
eventually become False to avoid
an infinite loop.""",

                'number = 1\nwhile number <= 5:\n    print(number)\n    number += 1',

                "1\n2\n3\n4\n5"
            ),

            (
                "The range() Function",
                """The range() function generates
a sequence of numbers.

range(5) generates numbers from 0 to 4.

range(1, 6) generates numbers from 1 to 5.

You can also use a third value to
control the step or interval.""",

                'for x in range(1, 6):\n    print(x)\n\nfor x in range(2, 8, 2):\n    print(x)',

                "1\n2\n3\n4\n5\n2\n4\n6"
            ),

            (
                "The break Statement",
                """The break statement immediately stops
the loop.

When Python encounters break,
it exits the current loop.

It is useful when a program needs
to stop repeating after a certain condition.""",

                'for x in range(1, 6):\n    if x == 3:\n        break\n    print(x)',

                "1\n2"
            ),

            (
                "The continue Statement",
                """The continue statement skips the current
repetition of a loop.

After skipping the current repetition,
Python moves to the next one.

It does not stop the entire loop.""",

                'for x in range(1, 6):\n    if x == 3:\n        continue\n    print(x)',

                "1\n2\n4\n5"
            ),

            (
                "Nested Loops",
                """A nested loop is a loop placed
inside another loop.

The inner loop runs completely for
each repetition of the outer loop.

Nested loops are useful for working
with rows, columns, and patterns.""",

                'for row in range(1, 3):\n    for column in range(1, 3):\n        print(row, column)',

                "1 1\n1 2\n2 1\n2 2"
            )
        ],

        "quiz": [
            (
                "What is iteration?",
                [
                    "A. Repeating instructions",
                    "B. Deleting a program",
                    "C. Naming a variable"
                ],
                "A"
            ),
            (
                "Which loop is commonly used to go through a sequence?",
                [
                    "A. if loop",
                    "B. for loop",
                    "C. print loop"
                ],
                "B"
            ),
            (
                "Which loop repeats while a condition is True?",
                [
                    "A. for loop",
                    "B. while loop",
                    "C. input loop"
                ],
                "B"
            ),
            (
                "What does break do?",
                [
                    "A. Skips one repetition",
                    "B. Stops the loop",
                    "C. Starts another program"
                ],
                "B"
            ),
            (
                "What does continue do?",
                [
                    "A. Skips the current repetition",
                    "B. Stops the entire program",
                    "C. Deletes the loop"
                ],
                "A"
            )
        ]
    }

]


def open_module(module, module_number):

    while True:

        print("\n==============================================")
        print("MODULE " + str(module_number) + ": " + module["title"].upper())
        print("==============================================")

        print("\nLESSON MENU:")

        for number, lesson in enumerate(module["lessons"], start=1):
            print("[" + str(number) + "] " + lesson[0])

        quiz_choice = len(module["lessons"]) + 1
        back_choice = len(module["lessons"]) + 2

        print("[" + str(quiz_choice) + "] Take a Short Quiz")
        print("[" + str(back_choice) + "] Back to Main Menu")

        choice = input("\nChoose Lesson: ").strip()

        if choice.isdigit():

            selected = int(choice)

            if 1 <= selected <= len(module["lessons"]):

                lesson = module["lessons"][selected - 1]

                show_lesson(
                    lesson[0],
                    lesson[1],
                    lesson[2],
                    lesson[3]
                )

            elif selected == quiz_choice:

                take_quiz(module["quiz"], module["title"])

            elif selected == back_choice:

                break

            else:

                print("\nInvalid choice! Please choose from the menu.")

        else:

            print("\nPlease enter a valid number.")



while True:

    print("\n==============================================")
    print("          PYTHON LEARNING TUTORIAL")
    print("==============================================")

    print("\nMAIN MENU:")

    for number, module in enumerate(modules, start=1):
        print("[" + str(number) + "] " + module["title"])

    print("[12] Exit")

    choice = input("\nChoose Module: ").strip()

    if choice.isdigit():

        module_choice = int(choice)

        if 1 <= module_choice <= 11:

            open_module(
                modules[module_choice - 1],
                module_choice
            )

        elif module_choice == 12:

            print("\n==============================================")
            print("Thank you for using our program!")
            print("Keep learning and practicing Python!")
            print("Goodbye!")
            print("==============================================")

            break

        else:

            print("\nInvalid module! Please choose from 1 to 12.")

    else:

        print("\nPlease enter a valid number.")