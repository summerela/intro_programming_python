# Module 6 Lab 2

## Instructions:

When you try to `open` a file that doesn't exist on your file system the `open` function raises a nice error called `FileNotFoundError`

    ```bash
    >>> open('some_file_location.txt', 'r')
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    FileNotFoundError: [Errno 2] No such file or directory: 'some_file_location.txt'
    >>>
    ```

0. Write a script called `lab2.py`. In the script write some pseudo code that opens a non-existant file location
 and use `try/except` to handle the `FileNotFoundError` and output a nicer message for the user about what happened?

0. Let's say some other type of error happens but we don't know the specifc name of it. How can our `try/except` handle this?

0. Files must always be closed! If an error is thrown how can we assure the file still gets closed? HINT: look up `try/except/finally`

