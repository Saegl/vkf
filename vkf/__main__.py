import fire

import vkf.auth
import vkf.api


def auth():
    vkf.auth.web_auth()


def load_friends(
    access_token: str,
    user_id: int,
    format: str = "csv",
    output: str = "",
):
    friends = list(vkf.api.get_friends(access_token, user_id))
    for friend in friends:
        print(friend)


def _main():
    """
    This function needed to conf `poetry scripts entry point`
    It starts from underscore to prevent showing it in fire cmd
    """
    fire.Fire(name="vkf")


if __name__ == "__main__":
    _main()
