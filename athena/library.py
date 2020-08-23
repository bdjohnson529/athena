from flask import Blueprint, flash, g, redirect, render_template, request, url_for, session, send_from_directory
from werkzeug.exceptions import abort
from werkzeug.utils import secure_filename

import os
import sys
import pandas as pd
import numpy as np

sys.path.append('..')
from pdfir.retrieval import ConstructInvertedIndex


bp = Blueprint('library', __name__)


def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@bp.record
def record_params(setup_state):
    """
    Inherit app config
    """
    app = setup_state.app
    bp.config = app.config


@bp.route('/', methods=['GET', 'POST'])
def index():
    """
    Landing page
    """
    filenames = os.listdir(bp.config['UPLOAD_FOLDER'])
    data = [{'name' : x,
             'size': f"{int(os.path.getsize( os.path.join(bp.config['UPLOAD_FOLDER'], x)) / 1000):,}"
            } for x in filenames]

    return render_template('library.html', library=data)



@bp.route('/upload', methods=['GET', 'POST'])
def upload():
    """
    Landing page
    """
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        
        file = request.files['file']
        
        # catch empty file
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        # upload file
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(bp.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('library.index'))

    return render_template('upload.html', html="")



@bp.route('/delete/<filename>', methods=['GET', 'POST'])
def delete(filename):
    """
    Delete document from library
    """
    print(filename)

    os.remove(os.path.join(bp.config['UPLOAD_FOLDER'], filename))

    return redirect(url_for('library.index'))



@bp.route('/uploads/<filename>')
def serve_file(filename):
    """
    Serves file to browser
    """
    return send_from_directory(os.path.join('../', bp.config['UPLOAD_FOLDER']),
                               filename)


'''
def parse():
    # store inverted index as dataframe
    data = ConstructInvertedIndex(file)
    df = pd.DataFrame.from_dict(data).T \
                .reset_index().rename(columns={'index': 'term'})

    df['postings'] = df['postings'].apply(lambda x: ','.join(map(str, x)))


    # convert dataframe to list of tuples
    records = list(df.to_records(index=False))
    str_records = [str(x) for x in records]
    insert_vals = ",".join(str_records)

    print(insert_vals)

    db = get_db()
    db.execute(
        f"""INSERT INTO inverted_index (Term, 
                            Frequency, 
                            Postings)
            VALUES {insert_vals}
        """
    )
    db.commit()
'''