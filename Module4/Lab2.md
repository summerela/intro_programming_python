# Module 4 Lab 2

## Instructions:

Another programmer quit their job ( this happens a lot ). You are tasked with finishing a script that reads a file and dumps out descriptive statistics about the file numbers from certain columns.

0. Find the zipfile called `module4_lab2.zip` in this GitHub repository. Download and unzip it to your workspace.

0. Unzipped you should see a directory structure like this:

    ```bash
    module4_lab2/
    ---- module4_lab2.py
    ---- data/
    ---- ---- fahrenheit_monthly_readings.tsv
    ```

0. Run the Python script `module4_lab2.py` as is and you should see similar output to this:

    ```bash
    $ python3 module4_lab2.py

    [ AVERAGE MAX TEMP ]: 0.0
    ```

0. Now open the data file `fahrenheit_monthly_readings.tsv` and take a look at this file. Note the column names. Try to get sense for what they are telling you.

0. Find the comment `TODO 1` and read the instructions there. You'll need to open a file and read the rows and put it into a Python nested data structure of dictionaries and lists

0. If `TODO 1` was simple for you, please move on to `TODO 2` where you'll finish writing a function to calculate the max temperature from the column `MNTH_MAX`

0. If `TODO 2` was simple for you, please move on to `TODO 3` where you'll finish writing a function to calculate the mean temperature from the columns `MNTH_MIN` and `MNTH_MAX`
