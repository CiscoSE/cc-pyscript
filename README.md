# Python Script | Cookiecutter Project Template

*Cookiecutter template for a Python script.*

This [Cookiecutter] project template makes it easy for you to start a *Cisco Sample Code* project to create and share an executable Python Script.

## Motivation

Creating a Python script is easy. Sharing one, with the needed licensing and essential documentation, should also be easy.

## Show Me

```bash
$ cookiecutter cc-pyscript

$ tree -a my-project/
```

## Features

- [Cisco Sample Code License][CiscoSampleCodeLicense] and code headers
- README template for Cisco sample code projects
- GitHub recommended docs and templates
- Command line interface using [Click] (optional)

## Using this Project Template

### The First Time

```bash
$ cookiecutter https://github.com/CiscoSE/cc-pyscript
```

...or using abbreviated syntax:

```bash
$ cookiecutter gh:CiscoSE/cc-pyscript
```

### Thereafter

```bash
$ cookiecutter cc-pyscript
```

## Installation

Install the latest Cookiecutter if you haven't installed it yet:

```bash
pip install -U cookiecutter
```

If you need a bit more help, see [Installation][CookiecutterInstallation] in the Cookiecutter docs.

## Credits

The following resources were influencial in the creation of this project:

- [Cookiecutter] by Audrey Roy Greenfeld ([@audreyr](https://github.com/audreyr))

## Who is this for?

This project template is for use by **Cisco Systems Engineers** who are creating example and demonstration code *(aka. Cisco Sample Code)* and sharing it with Cisco's customers and partners for use with Cisco products and services.  **The Cisco Sample Code License is for use in Cisco Repositories Only.**  It is not an Open Source license. The license should only be used by Cisco and/or its affiliates to post and share Cisco Sample Code.

[CiscoSampleCodeLicense]: ./LICENSE
[Click]: https://click.palletsprojects.com
[CookiecutterInstallation]: https://cookiecutter.readthedocs.io/en/latest/installation.html
[Cookiecutter]: https://github.com/audreyr/cookiecutter
