# SPDX-FileCopyrightText: 2023-present Yoshiki Sato <ysklove.music1stsight@gmail.com>
#
# SPDX-License-Identifier: MIT
import click

from poc_hatch.__about__ import __version__


@click.group(context_settings={"help_option_names": ["-h", "--help"]}, invoke_without_command=True)
@click.version_option(version=__version__, prog_name="poc_hatch")
def poc_hatch():
    click.echo("Hello world!")
