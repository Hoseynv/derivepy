from dataclasses import dataclass
from typing import Optional


@dataclass
class AllInstrumentRequestModel:
    currency: str
    expired: Optional[bool]
    instrument_type: Optional[str]
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
