## Python import & modules
- *0-add.py*:
  - A program that imports the function _def add(a, b):_ from the file *add_0.py* and prints the result of the additon *1 + 2 = 3*
  
- *1-calculation.py*:
  - A program that imports function from the file _calculator_1.py_, does some Maths, and prints the result
  
- *2-args.py*:
  - A program that prints the number of and the list of its arguments
  - Its output is:
    - the number of argument(s) followed by _argument_ (if number is one) or _arguments_ (otherwise), followed by
    - *:* (or *.* if no arguments were passed) followed by
    - a new line, followed by (if at least one argument),
    - one line per argument:
      - the position of the argument (starting at _1_) followed by _:_, followed by the argument value and a new line
      
- *3-infinite_add.py*:
  - A program that prints the result of the addition of all arguments
  
- *4-hidden_discovery.py*:
  - A program that prints all the names defined by the compiled module [hidden_4.pyc](https://github.com/holbertonschool/0x02.py/raw/master/hidden_4.pyc) (please download it locally) 
  
- *5-variable_load.py*:
  - A program that imports the variable *a* from the file **variable_load_5.py** and prints its value
  
- *100-my_calculator.py*:
  - A program that imports all functions from the file **calculator_1.py** and handles basic operations
  - Usage: **./100-my_calculator.py a operator b**
    - If the number of arguments is not 3, the program has to:
      - print **Usage: ./100-my_calculator.py** a <operator> b followed with a new line
      - exit with the value _1_
    - _operator_ can be:
      - _+_ for addition
      - _-_ for subtraction
      - _*_ for multiplication
      - _/_ for division
    - If the operator is not one of the above:
      - print **Unknown operator. Available operators: +, -, * and /** followed with a new line
      - exit with the value _1_
    - The variables _a_ and _b_ are casted into integers by using _int()_ 
    - The result is printed as **[a operator b = result]**, followed by a new line
 
- *101-easy_print.py*: 
  - A program that prints **#pythoniscool**, followed by a new line, in the standard output
  - program should be maximum 2 lines long
  - the functions **print** or **eval** or **open** or **import sys** in your file **101-easy_print.py**
-`*102-magic_calculation.py*:
  - A Python function **def magic_calculation(a, b):** that does exactly the same as the following Python bytecode:
- *103-fast_alphabet.py*:
  - A program that prints the alphabet in uppercase, followed by a new line
