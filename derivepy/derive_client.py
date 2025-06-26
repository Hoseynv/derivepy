import requests
from typing import Optional

from derivepy.models.response_model import ResponseModel
from derivepy.models.derive_response_model import *
from derivepy.models.derive_request_model import *


class DeriveClient:
    def __init__(self, test_net: bool = False) -> None:
        self.__base_url = self.__get_base_url(test_net)
        self.__header = {
            "accept": "application/json",
            "content-type": "application/json",
        }

    def get_all_instruments(self, body: AllInstrumentRequest) -> ResponseModel:
        url = f"{self.__base_url}/public/get_all_instruments"

        try:
            response = requests.post(url, json=body.to_json(), headers=self.__header)
            if response.status_code == 200:
                resp_json = response.json()

                if "error" in resp_json:
                    return ResponseModel(
                        success=False,
                        status_code=response.status_code,
                        error_message=resp_json["error"],
                    )

                return ResponseModel(
                    success=True,
                    status_code=response.status_code,
                    data=AllInstruments.from_dict(resp_json),
                )
            else:
                try:
                    data = response.json()
                except ValueError:
                    data = response.text
                return ResponseModel(
                    success=False,
                    status_code=response.status_code,
                    error_message={"message": "HTTP error", "details": data},
                )
        except requests.RequestException as e:
            return ResponseModel(
                success=False,
                status_code=getattr(e.response, "status_code", 500),
                error_message=str(e),
            )

    def get_instruments(self, body: InstrumentRequest) -> ResponseModel:
        url = f"{self.__base_url}/public/get_instruments"

        try:
            response = requests.post(url, json=body.to_json(), headers=self.__header)
            print(response.json())
            if response.status_code == 200:
                resp_json = response.json()

                if "error" in resp_json:
                    return ResponseModel(
                        success=False,
                        status_code=response.status_code,
                        error_message=resp_json["error"],
                    )

                return ResponseModel(
                    success=True,
                    status_code=response.status_code,
                    data=Instruments.from_dict(resp_json),
                )

            try:
                data = response.json()
            except ValueError:
                data = response.text

                return ResponseModel(
                    success=False,
                    status_code=response.status_code,
                    error_message={"message": "HTTP error", "details": data},
                )
        except requests.RequestException as e:
            return ResponseModel(
                success=False,
                status_code=getattr(e.response, "status_code", 500),
                error_message=str(e),
            )

    def get_ticker(self, body: TickerRequest) -> ResponseModel:
        url = f"{self.__base_url}/public/get_ticker"

        try:
            response = requests.post(url, json=body.to_json(), headers=self.__header)
            if response.status_code == 200:
                resp_json = response.json()

                if "error" in resp_json:
                    return ResponseModel(
                        success=False,
                        status_code=response.status_code,
                        error_message=resp_json["error"],
                    )

                return ResponseModel(
                    success=True,
                    status_code=response.status_code,
                    data=TickerResponse.from_dict(resp_json),
                )

            try:
                data = response.json()
            except ValueError:
                data = response.text

            return ResponseModel(
                success=False,
                status_code=response.status_code,
                error_message={"message": "HTTP error", "details": data},
            )

        except requests.RequestException as e:
            return ResponseModel(
                success=False,
                status_code=getattr(e.response, "status_code", 500),
                error_message=str(e),
            )

    def __get_base_url(self, test_net_status: bool) -> str:
        return (
            "https://api-demo.lyra.finance"
            if test_net_status
            else "https://api.lyra.finance"
        )
