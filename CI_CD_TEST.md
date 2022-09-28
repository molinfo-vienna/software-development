# Continuous Integration (CI), Deployment (CD), and Testing

### CI
In general, the practice of continuous integration simply means that building and testing each change of the code is done frequently and automatically.
The frequency of the contribution can be individually but it is common practice to do that on a daily basis keeping the contribution rather small. 
As soon as new code is commited, an automated build and test suite is prompted to detect errors as quickly as possible.
This reduces the chances of introducing conflict that you need to resolve later.
The changes can be 



### CD



### Unit Testing

Writing test while writing code is a good practice and makes you code more reliable and prone to failure or bugs.
Testing can be done with many different frameworks. Using the CMS cookiecutter, [pytest](https://docs.pytest.org/en/7.1.x/) is integrated. But you can of course also use python’s standard [unittest](https://docs.python.org/3/library/unittest.html) module.

When writing tests, keep the following in mind:

* Each test unit should focus on a small functionality and prove it correct
* Each test unit should be independet of another one
* Make each test unit run fast and avoid unnecessary, redundant complex structures (only if really necessary)
* Each test unit should be run automatically on push operations
* Run your whole test suite before and after your work too check weather you introduced an error
* Use descriptiv names for your test units - as long as they briefly describe what is done - this differes from the often preferred shorter names in you source code
* Keep in mind: A test unit without purpose should be avoided
* When collaborating, looking and running unit tests can be quite helpful in the beginning to get an understanding of the code itself


Get started with pytest [here](https://docs.pytest.org/en/7.1.x/getting-started.html#getstarted).


__Next Chapter:__ [__Documentation__](/DOCUMENTATION.md)