#!/usr/bin/env python3
# # -*- coding: utf-8 -*-

"""
CLI for BSL Reverse Proxy.
________________________________________________________________________________

Created by brightSPARK Labs
www.brightsparklabs.com
"""

from appcli.cli_builder import create_cli
from appcli.models.configuration import Configuration


# ------------------------------------------------------------------------------
# PRIVATE METHODS
# ------------------------------------------------------------------------------


def main():
    configuration = Configuration(
        app_name="reverse-proxy",
        docker_image="docker.brightsparklabs.com/brightsparklabs/reverse-proxy",
    )
    cli = create_cli(configuration)
    cli()


# ------------------------------------------------------------------------------
# ENTRYPOINT
# ------------------------------------------------------------------------------

if __name__ == "__main__":
    main()
