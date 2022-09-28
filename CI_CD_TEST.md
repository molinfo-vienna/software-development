# Continuous Integration, Continuous Delivery, Continuous Deployment, and Testing

### Continuous Integration (CI)
#### The main idea of CI is to have everyone working on a known stable base

In general, the practice of continuous integration simply means that building and testing each change of the code is done frequently and automatically.
The frequency of the contribution can be individually but it is common practice to do that on a daily basis keeping the contribution rather small. 
As soon as new code is commited, an automated build and test suite is prompted to detect errors as quickly as possible.
This reduces the chances of introducing conflict that you need to resolve later and assures that your changes did not break your code or introduced bugs.

Building your code means taking the raw source code and everthing necessary for its execution, and translating it into a format that computers can run directly.
As python is an [interpreted language](https://en.wikipedia.org/wiki/Interpreter_(computing)) its [`build`] revolves around test execution rather than compilation.

For scientists and developers, doing these steps manually takes a long time - so a big part of CI is about automating that process.
This is were testing come in handy.

### Unit Testing

Writing test while writing code is a good practice and makes you code more reliable and prone to failure or bugs.
Testing can be done with many different frameworks. Using the CMS cookiecutter, [pytest](https://docs.pytest.org/en/7.1.x/) is integrated. But you can of course also use python’s standard [unittest](https://docs.python.org/3/library/unittest.html) module.

When writing tests, keep the following in mind:

* Each test unit should focus on a small functionality and prove it correct
* Each new functionality should be covered by a unit test
* Each test unit should be independet of another one
* Make each test unit run fast and avoid unnecessary, redundant complex structures (only if really necessary)
* Each test unit should be run automatically on push operations
* Run your whole test suite before and after your work too check weather you introduced an error - do this in an automated way
* Use descriptiv names for your test units - as long as they briefly describe what is done - this differes from the often preferred shorter names in you source code
* Keep in mind: A test unit without purpose should be avoided
* When collaborating, looking and running unit tests can be quite helpful in the beginning to get an understanding of the code itself

Get started with pytest [here](https://docs.pytest.org/en/7.1.x/getting-started.html#getstarted).
Using GitHub Actions as the [CI/CD](/CI_CD_TEST.md#cicd-services) service, you can write your test the same way and then integrate it in your [`yaml`] file as shown [here](https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python#testing-your-code)

### Continuous delivery
Continuous delivery is an extension of continuous integration since it automatically deploys all code changes to a testing and/or production environment after the build stage. 

This means that on top of automated testing, you have an automated release process and you can deploy your application any time by clicking a button.

In theory, with continuous delivery, you can decide to release daily, weekly, fortnightly, or whatever suits your business requirements. However, if you truly want to get the benefits of continuous delivery, you should deploy to production as early as possible to make sure that you release small batches that are easy to troubleshoot in case of a problem.


### Continuous Deployment (CD)
Continuous deployment goes one step further than continuous delivery. With this practice, every change that passes all stages of your production pipeline is released to your customers. There's no human intervention, and only a failed test will prevent a new change to be deployed to production.

Continuous deployment is an excellent way to accelerate the feedback loop with your customers and take pressure off the team as there isn't a "release day" anymore. Developers can focus on building software, and they see their work go live minutes after they've finished working on it.

For further reading please look at the sites provided in the next section [CI/CD](/CI_CD_TEST.md#cicd-services)


### CI/CD services
There are many CI/CD services out there — such as [GitHub Actions](https://docs.github.com/en/actions), [Travis CI](https://www.travis-ci.com/), and [CircleCi](https://circleci.com/). 
We recommend using GitHub Actions, which is a service for executing CI/CD workflows for software stored in a GitHub repository.
Github Actions offers integrated [CI](https://docs.github.com/en/actions/deployment/about-deployments/about-continuous-deployment) and [CD](https://docs.github.com/en/actions/deployment/about-deployments/about-continuous-deployment) workflows.

In order to get to know GitHub Actions we recommend the official [Understaind GitHub Actions homepage](https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions) as well as the [building and testing python code](https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python) GitHub Actions site.
Another good resource is the [Python Packages homepage](https://py-pkgs.org/08-ci-cd.html) for more details, key concepts, and examples.

One important note is that when using self hosted runners [`ALWAYS`] use private repos! Please read the security concerns [here](https://docs.github.com/en/actions/hosting-your-own-runners/about-self-hosted-runners#self-hosted-runner-security).

We provide self hosted runners for GitHub Actions CI/CD - the how to use them can be found [here](https://github.com/molinfo-vienna/software-development/blob/main/ADMINISTRATION.md#server-usage-and-self-hosted-runners)


__Next Chapter:__ [__Documentation__](/DOCUMENTATION.md)