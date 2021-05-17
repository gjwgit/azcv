import os
from mlhub.pkg import get_private


# ----------------------------------------------------------------------
# Request subscription key and location from user.
# ----------------------------------------------------------------------

def reuqest_priv_info():
    PRIVATE_FILE = "private.json"

    path = os.path.join(os.getcwd(), PRIVATE_FILE)

    private_dic = get_private(path, "azcv")

    subscription_key = private_dic["Computer Vision"]["key"]

    endpoint = private_dic["Computer Vision"]["endpoint"]
    return subscription_key, endpoint