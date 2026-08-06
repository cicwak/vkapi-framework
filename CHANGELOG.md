# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.3] - 2026-08-06

### Fixed

- Preserve the callable `Bot.api()` raw API helper when generated method namespaces are installed.
- Keep `Bot.send_message()` and other convenience methods operational with the generated `api` namespace.

### Added

- Strict Pyright checks alongside Ruff, mypy, and Pyrefly.
- Regression coverage for raw API calls, convenience message sending, uploads, and malformed API responses.

## [0.1.0] - 2026-06-18

### Added

- Initial async VK API SDK and bot framework implementation.
- Community Bots Long Poll support.
- Typed method objects and raw VK API fallback.
- Routers, filters, middlewares, dependency injection, keyboards, and upload helpers.
