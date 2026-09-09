#!/usr/bin/env python3
"""Configuration script for Electronic Bible.

Handles configuration file generation and management.
"""

import argparse
import logging
import shutil
from pathlib import Path

logger = logging.getLogger(__name__)


def generate_config() -> None:
    """Generate configuration file from template."""
    logger.info("Generating configuration file...")

    config_dir = Path("config")
    config_dir.mkdir(exist_ok=True)

    # Copy example config
    example_config = Path("config/example.yaml")
    target_config = Path("config/config.yaml")

    if example_config.exists() and not target_config.exists():
        shutil.copy2(example_config, target_config)
        logger.info(f"Created config/config.yaml from example")
    else:
        logger.info("Configuration file already exists or example not found")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description="Electronic Bible Configuration Script")
    parser.add_argument("--generate", action="store_true", help="Generate configuration file")
    parser.add_argument("--validate", action="store_true", help="Validate configuration")

    args = parser.parse_args()

    if args.generate:
        generate_config()
    elif args.validate:
        logger.info("Validating configuration...")
        # TODO: Add validation logic


if __name__ == "__main__":
    main()