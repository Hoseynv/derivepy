from enum import Enum


class InstrumentType(str, Enum):
    ERC20 = "erc20"
    OPTION = "option"
    PERP = "perp"
