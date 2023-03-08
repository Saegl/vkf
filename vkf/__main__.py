import fire

import vkf.auth


def auth():
    vkf.auth.web_auth()


def _main():
    """
    This function needed to conf `poetry scripts entry point`
    It starts from underscore to prevent showing it in fire cmd
    """
    fire.Fire(name="vkf")


if __name__ == "__main__":
    _main()
