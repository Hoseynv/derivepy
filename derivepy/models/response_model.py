from typing import Any, Optional


class ResponseModel:
    def __init__(
        self,
        success: bool,
        status_code: int,
        data: Optional[Any] = None,
        error_message: Optional[str] = None,
    ):
        self.success = success
        self.status_code = status_code
        self.data = data
        self.error_message = error_message

    def __repr__(self):
        return (
            f"<ResponseModel "
            f"success={self.success}, "
            f"status_code={self.status_code}, "
            f"data_preview={str(self.data)[:100]}, "
            f"error_message={self.error_message!r}>"
        )

    def is_success(self) -> bool:
        return self.success

    def is_error(self) -> bool:
        return not self.success
