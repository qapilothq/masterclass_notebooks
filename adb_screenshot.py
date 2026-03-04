#!/usr/bin/env python3
"""
Take screenshots from an ADB-connected Android device and save to the screenshots folder.
Usage: python adb_screenshot.py [--name optional_filename]
"""

import argparse
import os
import subprocess
import sys
from datetime import datetime


SCREENSHOTS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "screenshots")


def ensure_screenshots_dir():
    """Create screenshots folder if it doesn't exist."""
    os.makedirs(SCREENSHOTS_DIR, exist_ok=True)
    return SCREENSHOTS_DIR


def check_adb_device():
    """Verify that an ADB device is connected."""
    try:
        result = subprocess.run(
            ["adb", "devices"],
            capture_output=True,
            text=True,
            check=False,
        )
        lines = result.stdout.strip().split("\n")[1:]  # Skip "List of devices"
        devices = [line for line in lines if line.strip() and "device" in line]
        if not devices:
            return False, "No device connected. Connect a device and enable USB debugging."
        return True, None
    except FileNotFoundError:
        return False, "ADB not found. Install Android SDK platform-tools and add to PATH."
    except Exception as e:
        return False, str(e)


def capture_screenshot(output_path: str) -> bool:
    """
    Capture screenshot from device using adb exec-out screencap.
    Returns True on success, False otherwise.
    """
    try:
        result = subprocess.run(
            ["adb", "exec-out", "screencap", "-p"],
            capture_output=True,
            check=False,
        )
        if result.returncode != 0:
            return False
        with open(output_path, "wb") as f:
            f.write(result.stdout)
        return True
    except Exception:
        return False


def main():
    parser = argparse.ArgumentParser(description="Capture screenshot from ADB device")
    parser.add_argument(
        "--name",
        "-n",
        type=str,
        default=None,
        help="Optional filename (without path). Default: screenshot_YYYY-MM-DD_HH-MM-SS.png",
    )
    args = parser.parse_args()

    ok, err = check_adb_device()
    if not ok:
        print(f"Error: {err}", file=sys.stderr)
        sys.exit(1)

    ensure_screenshots_dir()

    if args.name:
        name = args.name if args.name.endswith(".png") else f"{args.name}.png"
        output_path = os.path.join(SCREENSHOTS_DIR, name)
    else:
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        output_path = os.path.join(SCREENSHOTS_DIR, f"screenshot_{timestamp}.png")

    if capture_screenshot(output_path):
        print(f"Saved: {output_path}")
    else:
        print("Failed to capture screenshot.", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
