# Module 1 — Git & GitHub

**Student:** Sapnu, Charlotte G.
<<<<<<< HEAD
**Date:** September 24, 2026
=======
**Date:** September 27, 2026
>>>>>>> module-1

---

## What is Git? What is GitHub? (explain like you're teaching a friend who's never used either)

So Git is a command tool that helps the developers to manipulate the code's change over time through the terminal and also can track your code's history. While the GitHub is an online website/platform collaboration for the developers where they can actually store their work such as files or code, and they can also work together at the same time.

---

## Key vocabulary (in your own words)

- repository: This is the project or more likely a folder where your file stored your codes or files. Also, you'll be able to see the history of your changes in your code.
- commit: So basically this saves your code with the initial message.
- branch: It's like another piece of the tree where it is separate from the actual main project so that you'll be able to work on something without affecting the main project whenever you're trying to edit something and testing.
- push / pull:  The push actually gets or sends the local commits from your computer to github, and then the pull is getting the latest changes from the Github to your computer.
- pull request: This is basically asking permission if you can add your changes to the main project, especially when you are working with a collaborator. It allows the other developers to review your changes before they are merged into the project.
- merge conflict: This is when the two branches modify the same part of a file and then the git doesn’t know which change to keep.

---

## Walking through what I did

[Describe, step by step, a real branch → commit → push → PR you did. Include the actual commands you used.]

<<<<<<< HEAD
```
# paste your actual commands here
=======
Yesterday, during our midterm activity, I first configured my Git username and email using `git config --local user.name "sapnucharlotte-spec"` and `git config --local user.email "sapnucharlotte@gmail.com"`. After that, I checked my existing Git remote using `git remote`, then added my GitHub repository using `git remote add devnet-sapnu-charlotte https://github.com/sapnucharlotte-spec/devnet-sapnu-charlotte`. I verified the remote using `git remote -v`. Next, I created a new branch called `midterm` and switched to it using `git switch -c midterm`. After making my changes to `petAd.py`, I staged the file with `git add petAd.py`. I then committed my changes using `git commit -m "up5"`. Finally, I pushed my `midterm` branch to GitHub using `git push`. After pushing the branch, I went to GitHub and created a Pull Request for my changes.


```
git config --local user.name "sapnucharlotte-spec"
git config --local user.email "sapnucharlotte@gmail.com"
git remote
git remote add devnet-sapnu-charlotte https://github.com/sapnucharlotte-spec/devnet-sapnu-charlotte
git remote -v
git switch -c midterm
git add petAd.py
git commit -m "up5"
git push
>>>>>>> module-1
```

---

## A mistake I made (or one I want to avoid)

[What tripped you up? A confusing error message, committing to the wrong branch, a merge conflict — explain it so a classmate reading this avoids the same mistake.]

<<<<<<< HEAD
=======
What confused me was when I was creating a new branch, my computer detected the GitHub repository, but I was not sure why Git was not detecting it the way I expected. At first, I was confused about whether my branch was connected to the correct GitHub repository. I learned that I should always check the repository and remote before creating a branch or pushing my changes. This helped me understand that I need to check my Git status and remote information first so I know that I am working in the correct repository and branch.

>>>>>>> module-1
---

## How this connects to something else

[Optional: how does version control relate to anything else you've learned or used before?]
<<<<<<< HEAD
=======

Version control connects to programming because it helps me keep track of the changes I make to my code. It is also useful when working with other people because everyone can work on their own branch without affecting the main project. I learned that GitHub makes it easier to share code, review changes, and keep the project organized even though I'm still confused with git command it's very helful to the developers.

>>>>>>> module-1
