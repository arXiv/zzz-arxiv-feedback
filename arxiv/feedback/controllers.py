"""Provides request controllers for the feedback add-on."""

from typing import Dict, Any, Optional, Tuple
from http import HTTPStatus

Response = Tuple[Dict[str, Any], HTTPStatus, Dict[str, Any]]


def get_contribute_page() -> Response:
    """Handle a GET request for the 'Help Improve This' landing page."""
    raise NotImplementedError('Implement me!')
    # return {}, HTTPStatus.OK, {}