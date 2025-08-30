# dateutil Service (Model Context Protocol)

## Project Overview

`dateutil` is a powerful date and time processing service, extended from Python's `datetime` module, now adapted as an MCP (Model Context Protocol) service. It provides the following main features:

- **Date Parsing**: Supports parsing of various date string formats, including ISO 8601 standard.
- **Timezone Handling**: Supports timezone conversion and management.
- **Relative Time Calculation**: Implements dynamic date calculations through `relativedelta` (such as adding or subtracting months, days, etc.).
- **Recurrence Rules**: Supports event recurrence rules based on iCalendar standard.
- **Special Date Calculations**: Such as Easter date calculation.
- **Utility Tools**: Provides auxiliary utility functions for date and time.

This service is suitable for various scenarios requiring efficient date and time processing, supporting cross-language and cross-platform calls.

---

## Installation

1. **Environment Dependencies**:
   - Python version: 3.7 and above
   - Required libraries: `six`, `pytz`, `setuptools`

2. **Installation Command**:
   Install using pip:
   ```bash
   pip install python-dateutil
   ```

---

## Quick Start

Here are examples of calling main functions:

1. **Date Parsing**:
   Use the `parser` service to parse date strings:
   ```python
   from dateutil.parser import parse
   result = parse("2023-10-01")
   ```

2. **Timezone Handling**:
   Use the `tz` service for timezone conversion:
   ```python
   from dateutil.tz import gettz
   tz_info = gettz("Asia/Shanghai")
   ```

3. **Relative Time Calculation**:
   Use the `relativedelta` service to calculate relative time:
   ```python
   from dateutil.relativedelta import relativedelta
   new_date = current_date + relativedelta(months=+1)
   ```

4. **Recurrence Rules**:
   Use the `rrule` service to generate event recurrence rules:
   ```python
   from dateutil.rrule import rrule, DAILY
   rules = list(rrule(DAILY, count=5, dtstart=start_date))
   ```

5. **Easter Date Calculation**:
   Use the `easter` service to calculate Easter date:
   ```python
   from dateutil.easter import easter
   easter_date = easter(2023)
   ```

---

## Available Tools and Endpoints

1. **Date Parsing Service**:
   - Function: Parse various format date strings.
   - Endpoint: `parser`
   - Example: Parse ISO 8601 format dates.

2. **Timezone Handling Service**:
   - Function: Provide timezone conversion and management.
   - Endpoint: `tz`
   - Example: Get specified timezone information.

3. **Relative Time Calculation Service**:
   - Function: Dynamically calculate relative changes in dates.
   - Endpoint: `relativedelta`
   - Example: Add or subtract specified time.

4. **Recurrence Rules Service**:
   - Function: Generate event recurrence rules based on iCalendar standard.
   - Endpoint: `rrule`
   - Example: Generate daily recurring events.

5. **Easter Date Calculation Service**:
   - Function: Calculate Easter date for a specified year.
   - Endpoint: `easter`
   - Example: Get Easter date.

6. **Utility Tools Service**:
   - Function: Provide auxiliary utility functions for date and time.
   - Endpoint: `utils`
   - Example: Get current date.

---

## Common Issues and Notes

1. **Dependency Issues**:
   - Ensure `six`, `pytz`, and `setuptools` dependency libraries are installed.
   - Timezone data needs regular updates, recommend using the latest version of `pytz`.

2. **Environment Requirements**:
   - Compatible with Python 3.7 and above versions.
   - When calling in multi-language environments, recommend integration through REST or gRPC interfaces.

3. **Performance Notes**:
   - As a Python service, performance may not match native implementations in some languages (such as C++ or Java).
   - For high-performance requirement scenarios, recommend optimizing service call frequency.

4. **Timezone Data Management**:
   - Timezone data needs regular synchronization updates to ensure service accuracy.

---

## Reference Links and Documentation

- Official Documentation: `https://dateutil.readthedocs.io/`
- GitHub Repository: `https://github.com/dateutil/dateutil`
- MCP (Model Context Protocol) Service Design Guide: Please refer to internal documentation or contact technical support.

---

Through the above content, you can quickly get started and efficiently use the `dateutil` service (Model Context Protocol). For other questions, please refer to the official documentation or submit a support ticket.

---

## Reference Links and Documentation

- Official Documentation: `https://dateutil.readthedocs.io/`
- GitHub Repository: `https://github.com/dateutil/dateutil`
- MCP (Model Context Protocol) Service Design Guide: Please refer to internal documentation or contact technical support.

---

Through the above content, you can quickly get started and efficiently use the `dateutil` service (Model Context Protocol). For other questions, please refer to the official documentation or submit a support ticket.