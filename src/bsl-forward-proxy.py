#!/usr/bin/env python3
# # -*- coding: utf-8 -*-

"""
CLI for BSL Forward Proxy.
________________________________________________________________________________

Created by brightSPARK Labs
www.brightsparklabs.com
"""

import shutil
import os
from pathlib import Path
from typing import Dict, Any

import click
from appcli.cli_builder import create_cli
from appcli.logger import logger
from appcli.models.cli_context import CliContext
from appcli.models.configuration import Configuration, Hooks

# ------------------------------------------------------------------------------
# PRIVATE METHODS
# ------------------------------------------------------------------------------


def get_hooks() -> Hooks:
    def migrate_variables(
        cli_context: CliContext,
        current_variables: Dict[str, Any],
        previous_version: str,
        clean_new_version_variables: Dict[str, Any],
    ) -> Dict[str, Any]:
        logger.info(
            f"Migrating bsl-forward-proxy `{previous_version}` to `{cli_context.app_version}` ..."
        )

        # Handle migration from schema v1 to v2.
        if current_variables["metadata"]["schema_version"] == 1:
            pass

        return current_variables

    return Hooks(
        migrate_variables=migrate_variables,
    )


def main():
    configuration = Configuration(
        app_name="bsl-forward-proxy",
        docker_image="docker.brightsparklabs.com/brightsparklabs/bsl-forward-proxy",
        hooks=get_hooks(),
    )
    cli = create_cli(configuration)
    cli()


# ------------------------------------------------------------------------------
# ENTRYPOINT
# ------------------------------------------------------------------------------

if __name__ == "__main__":
    main()
