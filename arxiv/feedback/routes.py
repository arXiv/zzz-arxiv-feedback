"""Provides routes for the feedback add-on."""

from flask import Blueprint, Response, make_response, render_template


ui = Blueprint('feedback', __name__, url_prefix='/feedback')


@ui.route('/contribute')
def contribute() -> Response:
    """Render the 'Help Improve This' landing page."""
    raise NotImplementedError('Implement me!')

