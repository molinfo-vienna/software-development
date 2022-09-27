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
Moreover, when using our self-hosted [runners](https://docs.github.com/en/actions/hosting-your-own-runners/about-self-hosted-runners) please only create private repos.

In general, we recommend when collaborating with others, to generate a 'main' and 'development' branch.
The 'main' branch should always include the lastest, running instance of your package. You can tag it with a particular version.
The 'development' branch is the branch you and your collaborators should work on.
When you are working on a new implementation or feature, create a 'feature' branch starting from the 'development' branch. Name that branch in a easy to read and recognizeable fashion that describes the new feature.
Work on it till you think you are finished, write tests to evaluate your new feature, then use a pull request from the 'development' branch to your 'feature' branch and assign someone else to have a look at it.
When the tests are finished successfully, do more testing on the 'development' branch. Then if you are certain it works, you can repeate the pull request from the 'main' branch into the development.

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

If there are conflicts, dont worry, they can be fixed. #TODO


__Next Chapter:__ [__Continuous Integration__](https://github.com/molinfo-vienna/wiki/blob/main/CI_TEST.md)