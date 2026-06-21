from __future__ import annotations

from typing import Any, cast


class VKAPIError(Exception):
    """Base exception for vkapi."""


class VKNetworkError(VKAPIError):
    """Network transport failed."""


class VKDecodeError(VKAPIError):
    """Response body cannot be decoded or validated."""

    def __init__(self, message: str, payload: Any) -> None:
        super().__init__(message)
        self.payload = payload


class VKAPIResponseError(VKAPIError):
    """VK returned an `error` object."""

    def __init__(
        self,
        *,
        error_code: int,
        error_msg: str,
        request_params: list[dict[str, Any]] | None = None,
        raw: dict[str, Any] | None = None,
        method: str | None = None,
    ) -> None:
        super().__init__(f"[{error_code}] {error_msg}")
        self.error_code = error_code
        self.error_msg = error_msg
        self.request_params = request_params or []
        self.raw = raw or {}
        self.method = method


class VKRateLimitError(VKAPIResponseError):
    """VK API rate limit was exceeded."""


class VKAuthError(VKAPIResponseError):
    """Token or auth scope is invalid."""


class VKAccessDeniedError(VKAPIResponseError):
    """Access to requested object or method is denied."""


class VKCaptchaError(VKAPIResponseError):
    """VK requires captcha handling."""

    @property
    def captcha_sid(self) -> str | None:
        value = self.raw.get("captcha_sid")
        return str(value) if value is not None else None

    @property
    def captcha_img(self) -> str | None:
        value = self.raw.get("captcha_img")
        return str(value) if value is not None else None


ERROR_CODE_MAP: dict[int, type[VKAPIResponseError]] = {
    5: VKAuthError,
    6: VKRateLimitError,
    7: VKAccessDeniedError,
    14: VKCaptchaError,
    15: VKAccessDeniedError,
    27: VKAccessDeniedError,
    28: VKAccessDeniedError,
    29: VKRateLimitError,
}


def _any_list(value: Any) -> list[Any]:
    return cast(list[Any], value)


def make_api_error(method: str, error: dict[str, Any]) -> VKAPIResponseError:
    error_code = int(error.get("error_code", 0))
    error_cls = ERROR_CODE_MAP.get(error_code, VKAPIResponseError)
    raw_request_params = error.get("request_params")
    if not isinstance(raw_request_params, list):
        request_params = []
    else:
        request_param_items = _any_list(raw_request_params)
        request_params = [
            cast(dict[str, Any], item)
            for item in request_param_items
            if isinstance(item, dict)
        ]
    return error_cls(
        error_code=error_code,
        error_msg=str(error.get("error_msg", "VK API error")),
        request_params=request_params,
        raw=error,
        method=method,
    )
