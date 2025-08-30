import os
import sys

source_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "source")
sys.path.insert(0, source_path)

from fastmcp import FastMCP
from src.dateutil.parser import parse, isoparse
from src.dateutil.tz import gettz, tzutc, tzoffset, tzlocal
from src.dateutil.relativedelta import relativedelta
from src.dateutil.rrule import rrule, rruleset, rrulestr
from src.dateutil.easter import easter
from src.dateutil.utils import today, default_tzinfo

mcp = FastMCP("dateutil_service")

@mcp.tool(name="parse_date", description="Parse date string to datetime object")
def parse_date(date_string):
    """
    Parse date string to datetime object.

    Parameters:
        date_string (str): Date string to parse.

    Returns:
        dict: Dictionary containing parsing result, format: {'success': bool, 'result': datetime, 'error': str}.
    """
    try:
        result = parse(date_string)
        return {"success": True, "result": str(result), "error": None}
    except Exception as e:
        return {"success": False, "result": None, "error": str(e)}

@mcp.tool(name="isoparse_date", description="Parse ISO 8601 format date string")
def isoparse_date(date_string):
    """
    Parse ISO 8601 format date string.

    Parameters:
        date_string (str): ISO 8601 format date string to parse.

    Returns:
        dict: Dictionary containing parsing result, format: {'success': bool, 'result': datetime, 'error': str}.
    """
    try:
        result = isoparse(date_string)
        return {"success": True, "result": str(result), "error": None}
    except Exception as e:
        return {"success": False, "result": None, "error": str(e)}

@mcp.tool(name="get_timezone", description="Get specified timezone object")
def get_timezone(tz_name):
    """
    Get specified timezone object.

    Parameters:
        tz_name (str): Timezone name, e.g., "UTC" or "America/New_York".

    Returns:
        dict: Dictionary containing timezone object, format: {'success': bool, 'result': tzinfo, 'error': str}.
    """
    try:
        result = gettz(tz_name)
        return {"success": True, "result": str(result), "error": None}
    except Exception as e:
        return {"success": False, "result": None, "error": str(e)}

@mcp.tool(name="calculate_relativedelta", description="Calculate relative time difference")
def calculate_relativedelta(years=0, months=0, days=0):
    """
    Calculate relative time difference.

    Parameters:
        years (int): Year difference.
        months (int): Month difference.
        days (int): Day difference.

    Returns:
        dict: Dictionary containing relative time difference, format: {'success': bool, 'result': relativedelta, 'error': str}.
    """
    try:
        years = int(years) if years is not None else 0
        months = int(months) if months is not None else 0
        days = int(days) if days is not None else 0
        result = relativedelta(years=years, months=months, days=days)
        return {"success": True, "result": str(result), "error": None}
    except Exception as e:
        return {"success": False, "result": None, "error": str(e)}

@mcp.tool(name="generate_rrule", description="Generate repeating rules based on iCalendar standard")
def generate_rrule(freq, dtstart, count=None, until=None):
    """
    Generate repeating rules based on iCalendar standard.

    Parameters:
        freq (str): Frequency, e.g., "DAILY".
        dtstart (str): Start date string.
        count (int, optional): Number of repetitions.
        until (str, optional): End date string.

    Returns:
        dict: Dictionary containing repeating rules, format: {'success': bool, 'result': list, 'error': str}.
    """
    try:
        from src.dateutil.rrule import DAILY, WEEKLY, MONTHLY, YEARLY
        
        freq_map = {
            "DAILY": DAILY,
            "WEEKLY": WEEKLY,
            "MONTHLY": MONTHLY,
            "YEARLY": YEARLY
        }
        
        freq_value = freq_map.get(freq.upper(), DAILY)
        dtstart_parsed = parse(dtstart) if isinstance(dtstart, str) else dtstart
        count = int(count) if count is not None else None
        
        rule = rrule(freq_value, dtstart=dtstart_parsed, count=count, until=until)
        result = list(rule)
        return {"success": True, "result": [str(r) for r in result], "error": None}
    except Exception as e:
        return {"success": False, "result": None, "error": str(e)}

@mcp.tool(name="calculate_easter", description="Calculate Easter date")
def calculate_easter(year):
    """
    Calculate Easter date for a given year.

    Parameters:
        year (int): Year.

    Returns:
        dict: Dictionary containing Easter date, format: {'success': bool, 'result': date, 'error': str}.
    """
    try:
        year = int(year) if year is not None else 2025
        result = easter(year)
        return {"success": True, "result": str(result), "error": None}
    except Exception as e:
        return {"success": False, "result": None, "error": str(e)}

@mcp.tool(name="get_today", description="Get current date")
def get_today():
    """
    Get current date.

    Returns:
        dict: Dictionary containing current date, format: {'success': bool, 'result': date, 'error': str}.
    """
    try:
        result = today()
        return {"success": True, "result": str(result), "error": None}
    except Exception as e:
        return {"success": False, "result": None, "error": str(e)}

@mcp.tool(name="health_check", description="Check service health status")
def health_check():
    """
    Check service health status.

    Returns:
        dict: Dictionary containing health check result, format: {'success': bool, 'result': str, 'error': str}.
    """
    return {"success": True, "result": "Service is healthy", "error": None}

@mcp.tool(name="get_version", description="Get service version information")
def get_version():
    """
    Get service version information.

    Returns:
        dict: Dictionary containing version information, format: {'success': bool, 'result': str, 'error': str}.
    """
    return {"success": True, "result": "1.0.0", "error": None}

def create_app():
    """
    Create and return FastMCP instance.

    Returns:
        FastMCP: FastMCP instance.
    """
    return mcp