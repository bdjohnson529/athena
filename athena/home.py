import os
import sys
from flask import Blueprint, flash, g, redirect, render_template, request, url_for, session, send_from_directory
from werkzeug.exceptions import abort
from werkzeug.utils import secure_filename

sys.path.append('..')
import pdfir.retrieval


bp = Blueprint('home', __name__)





@bp.record
def record_params(setup_state):
    """
    Inherit app config
    """
    app = setup_state.app
    bp.config = app.config


@bp.route('/', methods=['GET', 'POST'])
def index():
    return render_template('home/index.html')