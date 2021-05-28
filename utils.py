import sys


def catch_exception(e, path):
    if "PermissionDenied" in str(e) or "Endpoint" in str(e):
        sys.exit(f"{e}\n"
                 f"Please run 'ml configure azcv' to update your private information. ")
    else:
        sys.exit(f"Error: {e}\n{path}")
