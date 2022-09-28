# The public best-practice page for the Molecular Informatics group at the University of Vienna

The official MolInfo-Vienna guidline for modern molecular informaticians to keep the focus on the reasearch than the how to set up their repository.

This setup guide is for everyone wanting to set up a molecular informatics project in python project quickly and easily.
In order to maximize collaborations and reusability of each project, we recommend making a package out of your project.
This allows for easy access to your code, reduces the time to implement new features, and collaborate with others. 
If you are working on sensitive topics that should not be public, you do not have to deploy to [Conda](https://anaconda.org/) or [PyPI](https://pypi.org/).

# Administrative

### New to the team?
First of all: `Welcome to the Molecular Informatics group!`

We are glad to have you on-board :)

There are a few practices we consider worth following.
1. Communications
    The main communication channel within the Group is mattermost. There are different channels for each group individually.
    The Cheminfo group has also a group calendar and a mailing list. If you are not part of them yet, depending on the group, please write your admin.
2. Software practices
    We would like you to read through the software debelopment guide starting [here](/IDE.md) and follow the [coding best practices](/BEST_PRACTICE.md). This is by no means a complete guide, but highlights a few practices we would like you to follow.

After reading through the guidelines, create a repo (either private or public - depending on if you are using our self hosted runners or not and if you code contains sensitive information. If its only sensitive data and you are not using self hosted runners, please keep the repo public).

Go to the [Mol-Info GitHub page](../) and create an empty repo, then use the cookiecutter template to create a local repo with the same name and connect/push it to the remote one.
Please only use the Mol-Info GitHub page for code/repos that you create during the time here.
Add then the team members to your repo and do awesome work!


### Server Usage and self-hosted runners

The [Molecular-Informatics Group]() provides a server and self hosted runners. The best practices can be found [here](https://wiki.univie.ac.at/pages/viewpage.action?spaceKey=ChemInfo&title=Cheminformatics+Research+Group+Wiki+Home).
You have to first define your university and then log in with your credentials.
If you do not have access, please write either Thomas Seidel (thomas.seidel@univie.ac.at), or Oliver Wieder (oliver.wieder@univie.ac.at) and we will add you to the user list.

# Content of the software development guide:

[__Integrated Development Environment Software__](/IDE.md):

For everyone interested in getting started right away with a proper IDE and package management

[__Licencing__](/LICENCING.md):

Choose a proper licence

[__Project Structure__](/PROJECT_STRUCTURE.md):

The key to a successful project is its structure

[__Version Control__](/VERSION_CONTROL.md): 

The main idea behind version control

[__Continuous Integration, Continuous Delivery, Continuous Deployment, and Testing__](/CI_CD_TEST.md):

Build your code frequently while making making sure your code does what you want it to do without breaking

[__Documentation__](/DOCUMENTATION.md):

Make it easier for you and collaborators to understand what your code tries to achieve

[__Packaging__](/PACKAGING.md)


## Some administative remarks and ML related things
[__Cluster and private runner usage__](/ADMINISTRATION.md)

[__Interesting machine learning resources__](/ML.md)

## Related Guides

Be sure to check out these related guides and materials:
* [MolSSI Software Best Practices](https://molssi.org/education/best-practices/)
* [MolSSI Education resources](https://molssi-education.github.io/resources.html)
* [Software Sustainability Institute Guides](https://software.ac.uk/resources/guides)
* [Chodera-Lab Software Development](https://github.com/choderalab/software-development/blob/master/README.md)

## Help Make this Page Better

Want to contribute to this repository? Have a suggestion for an improvement?
Spot a typo? We're always looking to improve this document for the betterment of all.

* Please feel free to [open a new issue](https://github.com/molinfo-vienna/software-development/issues/new) with your feedback and suggestions!
* Or [make a pull request](https://github.com/molinfo-vienna/software-development/compare) from your branch or fork!

__Next Chapter:__ [__Integrated Development Environment Software__](/IDE.md)