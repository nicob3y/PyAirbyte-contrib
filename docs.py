# Copyright (c) 2023 Airbyte, Inc., all rights reserved.
from __future__ import annotations

import os
import pathlib
import shutil

import pdoc


def run() -> None:
    """Generate docs for all public modules in airbyte and save them to docs/generated.

    Public modules are:
    * The main airbyte module
    * All directory modules in airbyte that don't start with an underscore.
    """
    public_modules = ["airbyte"]

    # recursively delete the docs/generated folder if it exists
    if pathlib.Path("docs/generated").exists():
        shutil.rmtree("docs/generated")

    # All folders in `airbyte` that don't start with "_" are treated as public modules.
    for d in os.listdir("airbyte"):
        dir_path = pathlib.Path(f"airbyte/{d}")
        if dir_path.is_dir() and not d.startswith("_") and (dir_path / "__init__.py").exists():
            public_modules.append(dir_path)

    pdoc.render.configure(template_directory="docs", show_source=False, search=False)
    pdoc.pdoc(*public_modules, output_directory=pathlib.Path("docs/generated"))
