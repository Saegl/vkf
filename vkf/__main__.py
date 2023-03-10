import fire
from vkf.cli import CliCommands


def _main():
    """
    This function needed to conf `poetry scripts entry point`
    It starts from underscore to prevent showing it in fire cmd
    """

    fire.Fire(CliCommands, name="vkontakte_friends")


if __name__ == "__main__":
    _main()
