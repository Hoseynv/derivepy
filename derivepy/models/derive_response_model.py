from dataclasses import dataclass
from typing import Optional, List, Dict


@dataclass
class OptionDetails:
    index: str
    expiry: int
    strike: str
    option_type: str
    settlement_price: Optional[float]

    @staticmethod
    def from_dict(data: dict) -> "OptionDetails":
        return OptionDetails(
            index=data["index"],
            expiry=data["expiry"],
            strike=data["strike"],
            option_type=data["option_type"],
            settlement_price=data.get("settlement_price"),
        )


@dataclass
class ERC20Details:
    decimals: int
    underlying_erc20_address: str
    borrow_index: str
    supply_index: str

    @staticmethod
    def from_dict(data: dict) -> "ERC20Details":
        return ERC20Details(
            decimals=data["decimals"],
            underlying_erc20_address=data["underlying_erc20_address"],
            borrow_index=data["borrow_index"],
            supply_index=data["supply_index"],
        )


@dataclass
class PerpDetails:
    index: str
    max_rate_per_hour: str
    min_rate_per_hour: str
    static_interest_rate: str
    aggregate_funding: str
    funding_rate: str

    @staticmethod
    def from_dict(data: dict) -> "PerpDetails":
        return PerpDetails(
            index=data["index"],
            max_rate_per_hour=data["max_rate_per_hour"],
            min_rate_per_hour=data["min_rate_per_hour"],
            static_interest_rate=data["static_interest_rate"],
            aggregate_funding=data["aggregate_funding"],
            funding_rate=data["funding_rate"],
        )


@dataclass
class Instrument:
    instrument_type: str
    instrument_name: str
    scheduled_activation: int
    scheduled_deactivation: int
    is_active: bool
    tick_size: str
    minimum_amount: str
    maximum_amount: str
    amount_step: str
    mark_price_fee_rate_cap: str
    maker_fee_rate: str
    taker_fee_rate: str
    base_fee: str
    base_currency: str
    quote_currency: str
    option_details: Optional[OptionDetails]
    perp_details: Optional[PerpDetails]
    erc20_details: Optional[ERC20Details]
    base_asset_address: str
    base_asset_sub_id: str
    pro_rata_fraction: str
    fifo_min_allocation: str
    pro_rata_amount_step: str

    @staticmethod
    def from_dict(data: dict) -> "Instrument":
        return Instrument(
            instrument_type=data["instrument_type"],
            instrument_name=data["instrument_name"],
            scheduled_activation=data["scheduled_activation"],
            scheduled_deactivation=data["scheduled_deactivation"],
            is_active=data["is_active"],
            tick_size=data["tick_size"],
            minimum_amount=data["minimum_amount"],
            maximum_amount=data["maximum_amount"],
            amount_step=data["amount_step"],
            mark_price_fee_rate_cap=data["mark_price_fee_rate_cap"],
            maker_fee_rate=data["maker_fee_rate"],
            taker_fee_rate=data["taker_fee_rate"],
            base_fee=data["base_fee"],
            base_currency=data["base_currency"],
            quote_currency=data["quote_currency"],
            option_details=(
                OptionDetails.from_dict(data["option_details"])
                if data.get("option_details")
                else None
            ),
            perp_details=(
                PerpDetails.from_dict(data["perp_details"])
                if data.get("perp_details")
                else None
            ),
            erc20_details=(
                ERC20Details.from_dict(data["erc20_details"])
                if data.get("erc20_details")
                else None
            ),
            base_asset_address=data["base_asset_address"],
            base_asset_sub_id=data["base_asset_sub_id"],
            pro_rata_fraction=data["pro_rata_fraction"],
            fifo_min_allocation=data["fifo_min_allocation"],
            pro_rata_amount_step=data["pro_rata_amount_step"],
        )


@dataclass
class Pagination:
    num_pages: int
    count: int

    @staticmethod
    def from_dict(data: dict) -> "Pagination":
        return Pagination(num_pages=data["num_pages"], count=data["count"])


@dataclass
class AllInstrumentsResult:
    instruments: List[Instrument]
    pagination: Optional[Pagination]

    @staticmethod
    def from_dict(data: dict) -> "AllInstrumentsResult":
        return AllInstrumentsResult(
            instruments=[Instrument.from_dict(item) for item in data["instruments"]],
            pagination=(
                Pagination.from_dict(data["pagination"])
                if data.get("pagination")
                else None
            ),
        )


@dataclass
class AllInstruments:
    result: AllInstrumentsResult
    id: Optional[str]

    @staticmethod
    def from_dict(data: dict) -> "AllInstruments":
        return AllInstruments(
            result=AllInstrumentsResult.from_dict(data["result"]), id=data.get("id")
        )


@dataclass
class InstrumentsResult:
    instruments: List[Instrument]

    @staticmethod
    def from_dict(data: list) -> "InstrumentsResult":
        return InstrumentsResult(
            instruments=[Instrument.from_dict(item) for item in data],
        )


@dataclass
class Instruments:
    result: InstrumentsResult
    id: Optional[str]

    @staticmethod
    def from_dict(data: dict) -> "Instruments":
        return Instruments(
            result=InstrumentsResult.from_dict(data["result"]), id=data.get("id")
        )


@dataclass
class PerpDetails:
    index: str
    max_rate_per_hour: str
    min_rate_per_hour: str
    static_interest_rate: str
    aggregate_funding: str
    funding_rate: str


@dataclass
class Stats:
    contract_volume: str
    num_trades: str
    open_interest: str
    high: str
    low: str
    percent_change: str
    usd_change: str


@dataclass
class OpenInterestEntry:
    current_open_interest: str
    interest_cap: str
    manager_currency: Optional[str]


@dataclass
class TickerResult:
    instrument_type: str
    instrument_name: str
    scheduled_activation: int
    scheduled_deactivation: int
    is_active: bool
    tick_size: str
    minimum_amount: str
    maximum_amount: str
    amount_step: str
    mark_price_fee_rate_cap: str
    maker_fee_rate: str
    taker_fee_rate: str
    base_fee: str
    base_currency: str
    quote_currency: str
    option_details: Optional[dict]
    perp_details: Optional[PerpDetails]
    erc20_details: Optional[dict]
    base_asset_address: str
    base_asset_sub_id: str
    pro_rata_fraction: str
    fifo_min_allocation: str
    pro_rata_amount_step: str
    best_ask_amount: str
    best_ask_price: str
    best_bid_amount: str
    best_bid_price: str
    five_percent_bid_depth: str
    five_percent_ask_depth: str
    option_pricing: Optional[dict]
    index_price: str
    mark_price: str
    stats: Stats
    timestamp: int
    min_price: str
    max_price: str
    open_interest: Dict[str, List[OpenInterestEntry]]


@dataclass
class OptionDetails:
    index: str
    expiry: int
    strike: str
    option_type: str
    settlement_price: Optional[str]


@dataclass
class OptionPricing:
    delta: str
    theta: str
    gamma: str
    vega: str
    iv: str
    rho: str
    mark_price: str
    forward_price: str
    discount_factor: str
    bid_iv: str
    ask_iv: str


@dataclass
class TickerResponse:
    result: TickerResult
    id: str

    def from_dict(data: dict) -> "TickerResponse":
        result = data["result"]

        return TickerResponse(
            id=data["id"],
            result=TickerResult(
                instrument_type=result["instrument_type"],
                instrument_name=result["instrument_name"],
                scheduled_activation=result["scheduled_activation"],
                scheduled_deactivation=result["scheduled_deactivation"],
                is_active=result["is_active"],
                tick_size=result["tick_size"],
                minimum_amount=result["minimum_amount"],
                maximum_amount=result["maximum_amount"],
                amount_step=result["amount_step"],
                mark_price_fee_rate_cap=result["mark_price_fee_rate_cap"],
                maker_fee_rate=result["maker_fee_rate"],
                taker_fee_rate=result["taker_fee_rate"],
                base_fee=result["base_fee"],
                base_currency=result["base_currency"],
                quote_currency=result["quote_currency"],
                option_details=(
                    OptionDetails(**result["option_details"])
                    if result.get("option_details")
                    else None
                ),
                perp_details=(
                    PerpDetails(**result["perp_details"])
                    if result.get("perp_details")
                    else None
                ),
                erc20_details=(
                    ERC20Details(**result["erc20_details"])
                    if result.get("erc20_details")
                    else None
                ),
                base_asset_address=result["base_asset_address"],
                base_asset_sub_id=result["base_asset_sub_id"],
                pro_rata_fraction=result["pro_rata_fraction"],
                fifo_min_allocation=result["fifo_min_allocation"],
                pro_rata_amount_step=result["pro_rata_amount_step"],
                best_ask_amount=result["best_ask_amount"],
                best_ask_price=result["best_ask_price"],
                best_bid_amount=result["best_bid_amount"],
                best_bid_price=result["best_bid_price"],
                five_percent_bid_depth=result["five_percent_bid_depth"],
                five_percent_ask_depth=result["five_percent_ask_depth"],
                option_pricing=(
                    OptionPricing(**result["option_pricing"])
                    if result.get("option_pricing")
                    else None
                ),
                index_price=result["index_price"],
                mark_price=result["mark_price"],
                stats=Stats(**result["stats"]),
                timestamp=result["timestamp"],
                min_price=result["min_price"],
                max_price=result["max_price"],
                open_interest={
                    k: [OpenInterestEntry(**entry) for entry in v]
                    for k, v in result["open_interest"].items()
                },
            ),
        )
