# Version Control System

Version control is a substantial part of any software project. It helps to keep track of different versions of your code, simplifies working together with collaborators, but also to store your code somewhere safe.

[Git](https://git-scm.com/) is a open source distributed version control system that we recommend.

If you do not have git installed, follow the [instructions](https://git-scm.com/downloads) here.

Then, if you do not have a GitHub account yet, create an account [here](https://github.com/).
As part of the MolInfo group, write us an email and we add you to your corresponding team.
Afterward, you can push your own, local GitHub project created with cookiecutter to the remote GitHub location.
To do this you can follow the instructions for [adding an existing project to GitHub using the command line](https://docs.github.com/en/get-started/importing-your-projects-to-github/importing-source-code-to-github/adding-locally-hosted-code-to-github#adding-a-local-repository-to-github-using-git). Follow the first steps (1-3) to create a new repo within the MolInfo group on GitHub. From there, you can **skip point 4**, as the cookiecutter template initialized a local GitHub repo already.
Continue then with point 5.

If you are doing research or making projects for any part of the MolInfo group, please create the repo there, not in your private account.
Some best-practice for git usage can be found [here](https://deepsource.io/blog/git-best-practices/).
Moreover, when using our self-hosted [runners](https://docs.github.com/en/actions/hosting-your-own-runners/about-self-hosted-runners) <mark>please only create private repos</mark>.

In general, we recommend when collaborating with others, to generate a `main` and `development` branch.
The `main` branch should always include the lastest, running instance of your package. You can tag it with a particular version.
Creating branches in the terminal can be done like this:
```
# when in the development branch use the following command to create and switch to the new-feature branch 
git checkout -b "new-feature"
```
For a detailed description of branching, how its done and how to merge and resolve merge conflicts, look at the [git homepage](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging).

The `development` branch is the branch you and your collaborators should work on.
When you are working on a new implementation or feature, create a `feature` branch starting from the `development` branch. Name that branch in a easy to read and recognizeable fashion that describes the new feature.
Work on it till you think you are finished, write tests to evaluate your new feature, then use a pull request from the `development` branch to your `feature` branch and assign someone else to have a look at it.
When the tests are finished successfully, do more testing on the `development` branch. Then if you are certain it works, you can repeate the pull request from the `main` branch into the `development`.

If another feature request or hotfix occures, leave the `feature` branch as is, create and switch to another `hotfix` branch or `other-feature` branch and come back later to finish your work.
Try to define the new feature as narrow as possible. Doing so, `feature` branches can be merged with the `development` branch more frequently, avoiding possible conflicts when working with several other collaborators. The reason for this is that the `development` branch moves forward and the more time you spend on you `feature` branch without merging, the higher the chances are that someone else is also changing the code you are currently working on. 
Some features take a long time, so it often cannot be avoided, but in general, it would be adviceable to create, merge, and then delte `feature` branches on a regular and frequent basis.
This concept is also described in the [next chapter (Continuous Integration, Deployment, and Testing)](https://github.com/molinfo-vienna/wiki/blob/main/CI_CD_TEST.md)

Commit on a regular basis to your remote branch. This saves your code even if your machine somehow gets busted. This can be done by:
```
# adds your current in that folder to the staging area
git add .
# adds a commit message
git commit -m "short message"
# finally pushes to your remote branch
git push
```    
Add a short message to your commit so that you know what it did. When looking at the history, commits should make sense.
Try to avoid committing broken code.
There are several ways of how to approach a consisten collaboration, however, we recommend the above.

If there are merge conflicts, dont worry, they can be fixed - you can start with reading on this page under [Basic Merge Conflicts](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging).


__Next Chapter:__ [__Continuous Integration, Deployment, and Testing__](/CI_CD_TEST.md)