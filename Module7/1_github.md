# Github

## Version Control
![Github](https://github.com/summerela/intro_programming_python/blob/master/Module7/github.jpg)

- Track who changed what
- Roll back to previous version
- Roll back mistakes
- Keep your project in a safe, online location

## Github basics
- Git = version control system
- GitHub = social code repository (place to store your code)
- Your computer = local repository
- Github servers = remote repository

** The following outline assumes you have already installed git and
   setup a github account. We will do that portion in the lab **

### Clone an Existing Repo
If the repository already exists, you can just copy it right onto your
computer.

- This copy becomes your own
- Add/edit/delete
- Create a request to add your changes to the original branch (they
don't have to accept)

    git clone https://github.com/summerela/intro_programming_python

### Create a new repo
The easiest way to do this is to first create a blank repo on
github.com and then pull it to your computer

### Pulling down changes to a repo
Before you start working on a git repository locally, good practice is
to pull down all the recent changes from github.

From your local computer:

    cd intro_programming_python
    git pull intro_programming_python

### Adding a new file to the repository
Your file will never be pushed to the remote repo on github.com until
you tell git to start tracking the file by using "git add":

    git add new_file.txt

### Commiting changes to a file
Any time you do something to a file that you want to be pushed up to
the remote repo, you must commit those changes and use the -m argument
to add a commit message detailing what you've done:

    git commit new_file.txt -m "added new_file.txt. remind summer to
    show you where these message show up on github"

### Check the status of your repo
See what files have been changed, and what you need to commit before a
push/pull.

    git status

### View the differences between local and remote files
Determine what you've changed in a file and decide if you want to keep
those changes.

    git diff

### View the log of recent commits

    git log
