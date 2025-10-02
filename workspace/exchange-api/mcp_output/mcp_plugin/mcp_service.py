import os
import sys
import json
from typing import Any, Dict, List, Optional

# Path settings
source_path = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
    "source",
)
sys.path.insert(0, source_path)

from fastmcp import FastMCP

# Load JSON data at module import
def _load_json(file_path: str) -> Any:
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return None

ALL_CURRENCIES_PATH = os.path.join(source_path, "allcurrencies.min.json")
COUNTRY_PATH = os.path.join(source_path, "country.json")
CURRENCIES_PATH = os.path.join(source_path, "other", "currencies.json")

ALL_CURRENCIES_DATA = _load_json(ALL_CURRENCIES_PATH) or {}
COUNTRY_DATA = _load_json(COUNTRY_PATH) or {}
CURRENCIES_DATA = _load_json(CURRENCIES_PATH) or {}

# Helper functions
def _find_currency_info(code: str) -> Optional[Dict[str, Any]]:
    return CURRENCIES_DATA.get(code.upper())

def _find_country_info(code: str) -> Optional[Dict[str, Any]]:
    return COUNTRY_DATA.get(code.upper())

def _get_exchange_rate(base: str, target: str) -> Optional[float]:
    base = base.upper()
    target = target.upper()
    rates = ALL_CURRENCIES_DATA.get("rates") or {}
    base_rate = rates.get(base)
    target_rate = rates.get(target)
    if base_rate is None or target_rate is None:
        return None
    return target_rate / base_rate

# MCP service
mcp = FastMCP("exchange_service")

@mcp.tool(name="get_all_currencies", description="Retrieve a list of all supported currency codes.")
def get_all_currencies() -> Dict[str, Any]:
    """
    Returns a list of all currency codes available in the service.

    Returns:
        dict: A dictionary containing success status, result list, and error message if any.
    """
    try:
        codes = list(ALL_CURRENCIES_DATA.get("rates", {}).keys())
        return {"success": True, "result": codes, "error": None}
    except Exception as e:
        return {"success": False, "result": None, "error": str(e)}

@mcp.tool(name="get_currency_info", description="Retrieve detailed information for a specific currency.")
def get_currency_info(currency_code: str) -> Dict[str, Any]:
    """
    Parameters:
        currency_code (str): The ISO 4217 currency code (e.g., 'USD', 'EUR').

    Returns:
        dict: A dictionary containing success status, result dict, and error message if any.
    """
    try:
        info = _find_currency_info(currency_code)
        if info is None:
            return {"success": False, "result": None, "error": f"Currency '{currency_code}' not found."}
        return {"success": True, "result": info, "error": None}
    except Exception as e:
        return {"success": False, "result": None, "error": str(e)}

@mcp.tool(name="convert_currency", description="Convert an amount from one currency to another.")
def convert_currency(amount: float, from_currency: str, to_currency: str) -> Dict[str, Any]:
    """
    Parameters:
        amount (float): The amount of money to convert.
        from_currency (str): The ISO 4217 code of the source currency.
        to_currency (str): The ISO 4217 code of the target currency.

    Returns:
        dict: A dictionary containing success status, result dict with converted amount, and error message if any.
    """
    try:
        rate = _get_exchange_rate(from_currency, to_currency)
        if rate is None:
            return {"success": False, "result": None, "error": "Exchange rate not available for the given currencies."}
        converted = amount * rate
        result = {
            "amount": amount,
            "from_currency": from_currency.upper(),
            "to_currency": to_currency.upper(),
            "converted_amount": converted,
            "rate": rate,
        }
        return {"success": True, "result": result, "error": None}
    except Exception as e:
        return {"success": False, "result": None, "error": str(e)}

@mcp.tool(name="get_country_info", description="Retrieve country information based on country code.")
def get_country_info(country_code: str) -> Dict[str, Any]:
    """
    Parameters:
        country_code (str): The ISO 3166-1 alpha-2 country code (e.g., 'US', 'GB').

    Returns:
        dict: A dictionary containing success status, result dict, and error message if any.
    """
    try:
        info = _find_country_info(country_code)
        if info is None:
            return {"success": False, "result": None, "error": f"Country '{country_code}' not found."}
        return {"success": True, "result": info, "error": None}
    except Exception as e:
        return {"success": False, "result": None, "error": str(e)}

@mcp.tool(name="get_exchange_rate", description="Retrieve the exchange rate between two currencies.")
def get_exchange_rate(base_currency: str, target_currency: str) -> Dict[str, Any]:
    """
    Parameters:
        base_currency (str): The ISO 4217 code of the base currency.
        target_currency (str): The ISO 4217 code of the target currency.

    Returns:
        dict: A dictionary containing success status, result dict with rate, and error message if any.
    """
    try:
        rate = _get_exchange_rate(base_currency, target_currency)
        if rate is None:
            return {"success": False, "result": None, "error": "Exchange rate not available for the given currencies."}
        result = {
            "base_currency": base_currency.upper(),
            "target_currency": target_currency.upper(),
            "rate": rate,
        }
        return {"success": True, "result": result, "error": None}
    except Exception as e:
        return {"success": False, "result": None, "error": str(e)}

def create_app() -> FastMCP:
    """
    Factory function to create and return the FastMCP application instance.

    Returns:
        FastMCP: The configured FastMCP application.
    """
    return mcp