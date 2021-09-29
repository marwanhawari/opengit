import webbrowser
import argparse
import sys
from typing import Optional, Sequence
import subprocess


def open_remote(dir: str = ".") -> int:
    """Open a remote repository given the git project directory.

    Args:
        dir (str, optional): The git project directory. Defaults to ".".

    Returns:
        int: The return code.
    """

    p = subprocess.run(
        ["git", "-C", f"{dir}", "remote", "get-url", "origin"],
        capture_output=True,
        text=True,
    )

    returncode = p.returncode

    if returncode == 0:
        remote = p.stdout.strip()
        if "git@" in remote:
            ssh = remote.split("@")[-1].split(":")
            repo = ssh[-1]
            domain = ssh[0]
            website = f"https://{domain}/{repo}"
        else:
            website = remote
        print(f"Opening {website}")
        webbrowser.open(website)
    else:
        print("ERROR: No remote url found!")

    return returncode


def main(argv: Optional[Sequence] = None) -> int:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "directory",
        nargs="?",
        help="Specify a directory or leave empty for the current directory.",
    )

    args = parser.parse_args(argv)

    if args.directory:
        return open_remote(args.directory)
    else:
        return open_remote()


if __name__ == "__main__":
    sys.exit(main())
