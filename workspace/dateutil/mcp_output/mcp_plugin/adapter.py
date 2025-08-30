import os
import sys

# Set path
source_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "source")
sys.path.insert(0, source_path)

# Import modules
try:
    from src.dateutil.parser import parse, isoparse
    from src.dateutil.tz import gettz, tzutc, tzoffset, tzlocal, tzfile, tzwin, tzwinlocal
    from src.dateutil.relativedelta import relativedelta
    from src.dateutil.rrule import rrule, rruleset, rrulestr
    from src.dateutil.easter import easter
    from src.dateutil.utils import today, default_tzinfo
    import_success = True
except ImportError as e:
    import_success = False
    import_error = str(e)

class Adapter:
    """
    MCP plugin Import mode adapter class.
    Provides encapsulation of dateutil library core functionality, supporting date parsing, timezone handling, relative time calculation and other functions.
    """

    def __init__(self):
        """
        Initialize adapter class.
        Set mode to "import" and check module import status.
        """
        self.mode = "import"
        if not import_success:
            self.mode = "fallback"
            self.error_message = f"Module import failed: {import_error}"

    # ------------------------- Date Parsing Functions -------------------------

    def parse_date(self, date_string, **kwargs):
        """
        Parse date string to datetime object.

        Parameters:
        - date_string (str): Date string to parse.
        - kwargs: Other optional parameters.

        Returns:
        - dict: Dictionary containing parsing result or error information.
        """
        if self.mode == "fallback":
            return {"status": "error", "message": "Parsing function unavailable, module import failed."}
        try:
            result = parse(date_string, **kwargs)
            return {"status": "success", "result": result}
        except Exception as e:
            return {"status": "error", "message": f"Parsing failed: {str(e)}"}

    def parse_iso_date(self, iso_date_string):
        """
        Parse ISO 8601 format date string.

        Parameters:
        - iso_date_string (str): ISO 8601 format date string.

        Returns:
        - dict: Dictionary containing parsing result or error information.
        """
        if self.mode == "fallback":
            return {"status": "error", "message": "ISO parsing function unavailable, module import failed."}
        try:
            result = isoparse(iso_date_string)
            return {"status": "success", "result": result}
        except Exception as e:
            return {"status": "error", "message": f"ISO parsing failed: {str(e)}"}

    # ------------------------- Timezone Handling Functions -------------------------

    def get_timezone(self, tz_name):
        """
        Get timezone object by specified name.

        Parameters:
        - tz_name (str): Timezone name.

        Returns:
        - dict: Dictionary containing timezone object or error information.
        """
        if self.mode == "fallback":
            return {"status": "error", "message": "Timezone function unavailable, module import failed."}
        try:
            result = gettz(tz_name)
            return {"status": "success", "result": result}
        except Exception as e:
            return {"status": "error", "message": f"Failed to get timezone: {str(e)}"}

    def get_utc_timezone(self):
        """
        Get UTC timezone object.

        Returns:
        - dict: Dictionary containing UTC timezone object or error information.
        """
        if self.mode == "fallback":
            return {"status": "error", "message": "UTC timezone function unavailable, module import failed."}
        try:
            result = tzutc()
            return {"status": "success", "result": result}
        except Exception as e:
            return {"status": "error", "message": f"Failed to get UTC timezone: {str(e)}"}

    # ------------------------- Relative Time Calculation Functions -------------------------

    def create_relativedelta(self, **kwargs):
        """
        Create a relative time object.

        Parameters:
        - kwargs: Parameters for relative time, such as years, months, days, etc.

        Returns:
        - dict: Dictionary containing relative time object or error information.
        """
        if self.mode == "fallback":
            return {"status": "error", "message": "Relative time function unavailable, module import failed."}
        try:
            result = relativedelta(**kwargs)
            return {"status": "success", "result": result}
        except Exception as e:
            return {"status": "error", "message": f"Failed to create relative time: {str(e)}"}

    # ------------------------- Easter Date Calculation Functions -------------------------

    def calculate_easter(self, year):
        """
        Calculate the date of Easter for a given year.

        Parameters:
        - year (int): Year.

        Returns:
        - dict: Dictionary containing Easter date or error information.
        """
        if self.mode == "fallback":
            return {"status": "error", "message": "Easter calculation function unavailable, module import failed."}
        try:
            result = easter(year)
            return {"status": "success", "result": result}
        except Exception as e:
            return {"status": "error", "message": f"Failed to calculate Easter date: {str(e)}"}

    # ------------------------- Repeating Rule Functions -------------------------

    def create_rrule(self, **kwargs):
        """
        Create a repeating rule object.

        Parameters:
        - kwargs: Parameters for repeating rules, such as freq, dtstart, interval, etc.

        Returns:
        - dict: Dictionary containing repeating rule object or error information.
        """
        if self.mode == "fallback":
            return {"status": "error", "message": "Repeating rule function unavailable, module import failed."}
        try:
            result = rrule(**kwargs)
            return {"status": "success", "result": result}
        except Exception as e:
            return {"status": "error", "message": f"Failed to create repeating rule: {str(e)}"}

    # ------------------------- Auxiliary Tools Functions -------------------------

    def get_today(self):
        """
        Get current date.

        Returns:
        - dict: Dictionary containing current date or error information.
        """
        if self.mode == "fallback":
            return {"status": "error", "message": "Get current date function unavailable, module import failed."}
        try:
            result = today()
            return {"status": "success", "result": result}
        except Exception as e:
            return {"status": "error", "message": f"Failed to get current date: {str(e)}"}