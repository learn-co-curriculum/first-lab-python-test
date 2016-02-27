# Your First Lab

One of the neat features on Learn is the ability to download labs, add your code to them and know immediately if you met your goal.

In order to get your own copy of the labs to work on, you will need to work with Git and Github.

The goal of this lab is to walkthough what the overall workflow is for your prework labs.

To complete this lab you will have to:
1. Fork the lab via Github.
2. Clone your fork.
3. Solve the Lab
4. Push that commit to your fork.
5. Open a Pull Request for your fork.

## 1. Forking from Github

Forking is the process of making a personal remote copy of the Learn lab.

<img width="100%" height="auto" src="http://ironboard-curriculum-content.s3.amazonaws.com/front-end/lab-assets/git-workflow-1.png" alt="Git Workflow 1">

To get started, in Learn click the title of the lab to go to Flatiron School's copy of the lab on Github.

<img width="100%" height="auto" src="http://ironboard-curriculum-content.s3.amazonaws.com/front-end/lab-assets/ironboard-labs-step-0.jpg" alt="Ironboard Labs Step 0">

Next on Flatiron's Github page for the lab click the Fork button.

<img width="100%" height="auto" src="http://ironboard-curriculum-content.s3.amazonaws.com/front-end/lab-assets/ironboard-labs-step-1.jpg" alt="Ironboard Labs Step 1">

Then select your personal Github account as the location to fork to.

<img width="100%" height="auto" src="http://ironboard-curriculum-content.s3.amazonaws.com/front-end/lab-assets/ironboard-labs-step-1b.jpg" alt="Ironboard Labs Step 1B">

## 2. Clone Your Fork

Cloning is the process of making a local copy of the lab from your personal remote on Github.

<img width="100%" height="auto" src="http://ironboard-curriculum-content.s3.amazonaws.com/front-end/lab-assets/git-workflow-2.png" alt="Git Workflow 2">

To clone, make sure you've first clicked on the SSH link, then click the
copy button next to the Clone URL to copy it to your clipboard.

<img width="100%" height="auto" src="http://ironboard-curriculum-content.s3.amazonaws.com/front-end/lab-assets/ironboard-labs-step-2.jpg" alt="Ironboard Labs Step 2">

Next, in Terminal navigate to the parent directory where you would like to place this lab. For example, you can create a new folder on your Desktop called CSSI_Prework and keep all of your labs in that folder. In that case, make sure you cd into that directory: `cd Desktop\CSSI_Prework`

Once you are in the directory that you want this lab to go, you want to clone (copy) the
files from git to your local machine. To do this, type:  `git clone <paste the clone URL here>`  

Note: You should replace the &lt;paste the clone URL here&gt; including the &lt; and &gt; symbols in the snippet above with your actual clone URL by pressing command+v on mac or ctrl+v on windows. Example: git clone git@github.com:jongrover/first-lab-000.git

<img width="100%" height="auto" src="http://ironboard-curriculum-content.s3.amazonaws.com/front-end/lab-assets/ironboard-labs-step-2b.png" alt="Ironboard Labs Step 2b">

## 3. Solving this Lab

<img width="100%" height="auto" src="http://ironboard-curriculum-content.s3.amazonaws.com/front-end/lab-assets/git-workflow-3.png" alt="Git Workflow 3">

Now that you have forked and cloned your fork, your goal is simple. Just create a new file within this lab.

Go into this lab's directory by typing 'cd first-lab'. Confirm that your working directory in terminal is this lab by typing: `pwd`

You should see something like: `/Users/avi/first-lab`

![1](https://dl.dropboxusercontent.com/s/4h2yls40mf9femj/2015-05-03%20at%209.05%20PM.png)

Now, try to run your test by running `python test_first_lab.py` on your terminal. You'll see output similar with failing tests (that's fine, don't panic).

2. Simply create a file. It doesn't matter what you call it.
`touch my-new-file.txt`

3. Once you've done that, run `python test_first_lab.py` again, which will run one test. This test is looking to see that you've added a new file. If you have the test passing on your computer, you should see something like this on Learn, indicating the local build is passing:


![1](https://dl.dropboxusercontent.com/s/rfs3onevx3l2o21/2015-05-03%20at%209.10%20PM%20%281%29.png)

4. Add it to the repo, staging it for commit.

`git add my-new-file.txt`

![1](https://dl.dropboxusercontent.com/s/kesh225ztp4owbk/2015-05-03%20at%209.12%20PM.png)

5. Commit the file. The -m is a message option. You should always save your changes with a message that describes what you changed or added to your project. If it's your first ever commit, most people write "initial commit"

`git commit -m "initial commit - I'm a genius"`

![1](https://dl.dropboxusercontent.com/s/9y3zt153pvaabh0/2015-05-03%20at%209.14%20PM.png)

## 4. Push Your Code to Github

<img width="100%" height="auto" src="http://ironboard-curriculum-content.s3.amazonaws.com/front-end/lab-assets/git-workflow-4.png" alt="Git Workflow 4">

After adding and committing your most recent work next we want to push our work up to our personal Github remote (origin).

`git push origin master`

![1](https://dl.dropboxusercontent.com/s/7qta395mpnmst7x/2015-05-03%20at%209.15%20PM.png)

Go to github and confirm the push.

![1](http://flatiron-videos.s3.amazonaws.com/ironboard/ironboard-tutorial/7-solving-the-lab.png)

## 5. Opening a Pull Request

Submitting a pull request can be described as the process of asking the maintainer of the Learn lab (upstream remote) to consider pulling (fetching & merging) in your work from your personal remote copy (origin remote). This enables your instructor to see your solution for the lab.

<img width="100%" height="auto" src="http://ironboard-curriculum-content.s3.amazonaws.com/front-end/lab-assets/git-workflow-5.png" alt="Git Workflow 5">

To do so, in Learn click the title of the lab to go to your forked copy on Github.

<img width="100%" height="auto" src="http://ironboard-curriculum-content.s3.amazonaws.com/front-end/lab-assets/ironboard-labs-step-0b.jpg" alt="Ironboard Labs Step 0b">

Then click the green Pull Request button.

<img width="100%" height="auto" src="http://ironboard-curriculum-content.s3.amazonaws.com/front-end/lab-assets/ironboard-labs-step-4.jpg" alt="Ironboard Labs Step 4">

After reviewing the comparison code and making sure it shows your solution, click the Create pull request button.

<img width="100%" height="auto" src="http://ironboard-curriculum-content.s3.amazonaws.com/front-end/lab-assets/ironboard-labs-step-4e.jpg" alt="Ironboard Labs Step 4e">

Then click Create pull request button again.

<img width="100%" height="auto" src="http://ironboard-curriculum-content.s3.amazonaws.com/front-end/lab-assets/ironboard-labs-step-4f.jpg" alt="Ironboard Labs Step 4f">

That's it, you're done! Now go back to Learn and you should see the Pull Request flip to green, and the remote build will be kicked off. Once it passes, you will be able to proceed to the Next Lesson.
