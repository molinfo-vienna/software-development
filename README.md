# Welcome to the Molecular Informatics Vienna Platform

First of all: `Welcome :)`

This repository provides guidelines and best practices for Python development within the Molecular Informatics Vienna platform. Whether you're new to coding or an experienced developer, you'll find valuable information to help you write clean, maintainable, and collaborative code.

## Introduction

The Molecular Informatics Vienna platform consists of three teams:
1. [Christian-Doppler Laboratory for Molecular Informatics in the Bioscience team](https://cdlab-mib.univie.ac.at/)
2. [Cheminfo team](https://cheminfo.univie.ac.at/home/)
3. [comp3d team](https://comp3d.univie.ac.at/)

This guide is designed to help everyone set up a molecular informatics project in Python quickly and easily, with a focus on creating reusable packages to maximize collaboration and efficiency.

## Table of Contents

### Essential Practices (For Everyone)
1. [Project Structure](./PROJECT_STRUCTURE.md)
2. [Documentation, Code Style, and Linting](./DOCUMENTATION.md)
3. [Version Control Basics](./VERSION_CONTROL.md)
4. [Testing Fundamentals](./TEST)
5. [Continues Integration (CI)](./CI.md)
5. [IDE Setup for Beginners](./IDE.md)

### Advanced Topics (For Deeper Exploration)
7. [Packaging and Distribution](./PACKAGING.md)
8. [Advanced Continuous Integration (CI)](./ADVANCED_CI_CD.md)
9. [GitHub Actions](./ADVANCED_CI_CD.md##Best_Practices_for_CI/CD)
10. [Licensing](./LICENCING.md)
11. [Machine Learning Resources](./ML.md)

## Getting Started

If you're new to the group or to coding in general, we recommend starting with the Essential Practices. These will help you set up a solid foundation for writing good Python code.

1. Begin by setting up your [Integrated Development Environment (IDE)](./IDE.md).
2. Learn about proper [Project Structure](./PROJECT_STRUCTURE.md).
3. Familiarize yourself with our [Documentation and Linting](./DOCUMENTATION.md) guidelines.
4. Understand the basics of [Version Control](./VERSION_CONTROL.md).
5. Learn about [Testing](./TEST.md) your code.

For those looking to dive deeper or contribute to more complex projects, check out the Advanced Topics section.

## Minimum Requirements for CD-Lab MIB

When working on code in the CD-Lab Molecular Informatics in the Biosciences, please ensure you follow these minimum requirements:

1. Adhere to the [CI/CD Guidelines](./CI.md) and the [advanced](./ADVANCED_CI_CD.md) section for each new project.
2. Implement [linting](./LINTING.md), [good documentation](./DOCUMENTATION.md), and [packaging](./PACKAGING.md) for your Python projects.
3. Use pip package manager over conda when possible.

## Administrative Information

### New to the team?

1. **Communications:** Join our Mattermost channels. The Cheminfo team also has a team calendar and mailing list.
2. **Software project good-practices:** Read through this software development guide and follow the [coding best practices](./README.md).
3. **Issues and bug reporting:** Use the repository's issue tracker or the [CD-Lab MiB dedicated issue repository](https://github.com/molinfo-vienna/cd_mib_open_issues) for general requests.

After reading the guidelines, create a repo on the [Mol-Info GitHub page](https://github.com/organizations/molinfo-vienna/repositories/new), use the cookiecutter template to set it up locally, and push it to the remote repository.

## CDPKit, Server Usage, and Self-Hosted Runners

Information about server usage and self-hosted runners can be found in our [Best Practice Computer Resources Guide](https://wiki.univie.ac.at/display/ChemInfo/Best+Pracitice+Computer+Resources+Guide).

### CDPKit

The [Chemical Data Processing Toolkit (CDPKit)](https://github.com/molinfo-vienna/CDPKit) is an open-source cheminformatics toolkit. You can install it via:

```bash
pip install cdpkit
```

## Contributing

We encourage all members to contribute to this repository by suggesting improvements, reporting issues, or submitting pull requests. Please feel free to:

- [Open a new issue](https://github.com/molinfo-vienna/software-development/issues/new) with your feedback and suggestions.
- [Make a pull request](https://github.com/molinfo-vienna/software-development/compare) from your branch or fork.
- Comment on a commit.

## Related Guides

Be sure to check out these related guides and materials:
- [MolSSI Software Best Practices](https://molssi.org/education/best-practices/)
- [MolSSI Education resources](https://molssi-education.github.io/resources.html)
- [Software Sustainability Institute Guides](https://software.ac.uk/resources/guides)
- [Chodera-Lab Software Development](https://github.com/choderalab/software-development/blob/master/README.md)

## Questions and Support

If you have any questions or need support, please open an issue or contact Thomas Seidel (thomas.seidel@univie.ac.at) or Oliver Wieder (oliver.wieder@univie.ac.at).

Happy coding!