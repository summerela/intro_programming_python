# Module 7 Lab 2

Life is about the `push` and the `pull`

## Instructions:

# The *Push*
0. Let's add a new file to our local repository. Later we will push it up to the remote Github repository:

0. First make sure you're in the repository directory (HINT: our `README.md` should be there):

  ```
  $ ls -lah
  total 24
  drwxr-xr-x   5 whizmob  staff   170B Feb 19 19:05 ./
  drwxr-xr-x   4 whizmob  staff   136B Feb 19 18:40 ../
  -rw-r--r--@  1 whizmob  staff   6.0K Feb 19 18:40 .DS_Store
  drwxr-xr-x  14 whizmob  staff   476B Feb 19 18:55 .git/
  -rw-r--r--   1 whizmob  staff    52B Feb 19 18:24 README.md
  ```
  
0. Then create a file called `homework7.py`. I'm gonna use a Linux command to do that ( also available on Mac ). 
Use whatever you want:
  ```
  $ touch homework7.py
  $ ls -lah
  ...
  -rw-r--r--   1 whizmob  staff     0B Feb 19 19:06 homework7.py
  ```
  
0. Now we're gonna add it to "Staging". Say What? Let's talk about it:
  ```
  $ git add homework7.py
  ```

0. Let's see what the "status" of our local repository is. Let's talk about what this stuff means:
  ```
  $ git add homework7.py 
  $ git status
  # On branch master
  # Untracked files:
  #   (use "git add <file>..." to include in what will be committed)
  #
  #	.DS_Store
  nothing added to commit but untracked files present (use "git add" to track)
  ```
  
0. Let's "commit" our changes in staging so they are ready to "push":
  ```
   $ git commit -m "adding homework 7"
  [master 098ec88] adding homework 7
   0 files changed
   create mode 100644 homework7.py
  ```
0. Our status has probably changed. Let's talk about it:
  ```
  $ git status
  # On branch master
  # Your branch is ahead of 'origin/master' by 1 commit.
  #
  # Untracked files:
  #   (use "git add <file>..." to include in what will be committed)
  #
  #	.DS_Store
  nothing added to commit but untracked files present (use "git add" to track)
  ```
  
0. Finally, we are ready to push our changes to the remote respository:
  ```
  $ git push
  Username for 'https://github.com': whizmob
  Password for 'https://whizmob@github.com': 
  Counting objects: 4, done.
  Delta compression using up to 4 threads.
  Compressing objects: 100% (2/2), done.
  Writing objects: 100% (3/3), 286 bytes, done.
  Total 3 (delta 0), reused 0 (delta 0)
  To https://github.com/whizmob/PythonFoundationsWhizmob.git
     f95e320..098ec88  master -> master
  ```
  
# The *Push*

0. Now let's go edit some files in Github itself ( like in the browser ).

0. Open this file

0. Click the edit pencil

0. Add some stuff

0. Add a commit message and click save

0. Then go back to your terminal window

0. Finally, let's "pull" our changes from the remote repo down to our local repo:


  
  
