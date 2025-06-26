from dataclasses import dataclass
from typing import Optional

from derivepy.enums import InstrumentType


@dataclass
class AllInstrumentRequest:
    currency: str
    expired: Optional[bool]
    instrument_type: InstrumentType
    page: Optional[int]
    page_size: Optional[int]

    def to_json(self) -> dict:
        return {
            "currency": self.currency,
            "expired": self.expired,
            "instrument_type": self.instrument_type,
            "page": self.page,
            "page_size": self.page_size,
        }


@dataclass
class InstrumentRequest:
    expired: bool
    instrument_type: InstrumentType
    currency: Optional[str]

    def to_json(self) -> dict:
        return {
            "expired": self.expired,
            "instrument_type": self.instrument_type.value,
            "currency": self.currency,
        }


@dataclass
class TickerRequest:
    instrument_name: str

    def to_json(self) -> dict:
        return {"instrument_name": self.instrument_name}


@dataclass
class OptionSettlementPricesRequest:
    currency: str

    def to_json(self) -> dict:
        return {"currency": self.currency}
