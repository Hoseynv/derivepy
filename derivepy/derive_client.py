class DeriveClient:
    def __init__(self, test_net: bool = False) -> None:
        self.__base_url = self.__get_base_url(test_net)

    def __get_base_url(self, test_net_status: bool) -> str:
        return "https://api-demo.lyra.finance" if test_net_status else "https://api.lyra.finance"
