# Module 4 Lab 1

## Instructions:

You're a programmer with no time. Your boss asked you to write a script that takes input but not through the user prompt ( the `input` command ).
She want's you to use "command line arguments". With no time to spare you use the `sys` module to help you:

0. Find the starter script called `module4_lab1.py` in this GitHub repository. Copy and past it to a script in your workspace.

0. Run it as is and you should see similar output to this:

    ```bash
    $ python module4_lab1.py
    [ ARG-0 ]: module4_lab1.py
    ```

0. Now run it again and add arbitrary arguments to the end of the command line:

    ```bash
    $ python module4_lab1.py --foo bar 1 2 3 baz 10,11
    ```

0. How is `sys.argv` parsing the arguments? What is the delimiter ( the think that it splits on )?

0. Can you modify `module4_lab1.py` and write a script that will take two command line arguments ( don't use `input` ) and outputs the sum? 
You'll need to think about converting arguments to the correct data types. You'll need to think about handling errors ( too few arguments, too many arguments ).


NOTE: you can imagine how much work this would be for a large script with many inputs  data types. Next we'll look at a better solution
