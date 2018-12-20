#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""{{ cookiecutter.project_name }} Console Script.

Copyright (c) {% now 'local', '%Y' %} Cisco and/or its affiliates.

This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.0 (the "License"). You may obtain a copy of the
License at

               https://developer.cisco.com/docs/licenses

All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.

"""

{% if cookiecutter.use_click|lower|trim == "y" -%}
import sys

import click


{% endif -%}
__author__ = "{{ cookiecutter.full_name }}"
__email__ = "{{ cookiecutter.email }}"
__version__ = "{{ cookiecutter.version }}"
__copyright__ = "Copyright (c) {% now 'local', '%Y' %} Cisco and/or its affiliates."
__license__ = "Cisco Sample Code License, Version 1.0"


{% if cookiecutter.use_click|lower|trim == "y" -%}
@click.command()
def main(*args, **kwargs):
    """{{cookiecutter.project_slug}} Console Script."""
    click.echo("Replace this message by putting your code into "
               "{{cookiecutter.project_slug}}.py")
    click.echo("See click documentation at http://click.pocoo.org/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
{% else -%}
# Ready for your code.
{% endif -%}
