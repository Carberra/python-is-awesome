from enum import Enum, auto

import requests

POSTCODES_IO_URL = "https://api.postcodes.io"


class PostcodeStatus(Enum):
    INVALID = auto()
    LIVE = auto()
    TERMINATED = auto()
    UNKNOWN = auto()


def postcode_status(postcode: str) -> PostcodeStatus:
    with requests.get(f"{POSTCODES_IO_URL}/terminated_postcodes/{postcode}") as resp:
        match resp.json():
            case {"status": 200}:
                return PostcodeStatus.TERMINATED
            case {"status": 404, "error": "Invalid postcode"}:
                return PostcodeStatus.INVALID
            case {"status": 404, "error": "Terminated postcode not found"}:
                return PostcodeStatus.LIVE
            case _:
                return PostcodeStatus.UNKNOWN


if __name__ == "__main__":
    print(postcode_status("EC1A 1BB"))  # Live postcode
    print(postcode_status("INVALID"))  # Invalid postcode
    print(postcode_status("W1A 0AA"))  # Terminated postcode
