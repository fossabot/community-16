"""Karrio eShipper client settings."""

import attr
import karrio.providers.eshipper.utils as provider_utils


@attr.s(auto_attribs=True)
class Settings(provider_utils.Settings):
    """eShipper connection settings."""

    principal: str
    credential: str

    id: str = None
    test_mode: bool = False
    carrier_id: str = "eshipper"
    account_country_code: str = None
    metadata: dict = {}
    config: dict = {}
