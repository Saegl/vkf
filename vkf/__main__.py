"""
Entry point for `vkf` cli program
"""
import fire  # type: ignore # no stubs for fire
from vkf.cli import CliCommands


def _main() -> None:
    """
    This function needed to conf `poetry scripts entry point`
    It starts from underscore to prevent showing it in fire cmd
    """

    fire.Fire(CliCommands, name="vkontakte_friends")


if __name__ == "__main__":
    _main()
