from flask import Flask, render_template, abort, send_file, request, flash, redirect, url_for
import os
import subprocess
# import logging
import pickle

app = Flask(__name__)
# logging.basicConfig(level=logging.DEBUG)
# logging.debug('This is error output')
root = '/Users/ramon/Papers'


@app.route('/')
def root_page():
    global root
    print(222)
    # Return 404 if path doesn't exist
    if not os.path.exists(root) or os.path.isfile(root):
        return abort(404)

    # Show directory contents
    files = [f for f in os.listdir(root) if f.endswith('.pdf')]
    return render_template('files.html', files=files)


@app.route('/<path:req_path>')
def get_page(req_path):
    print(111)
    subprocess.call(["open", f'{root}/{req_path}'])
    return redirect(url_for('root_page'))


@app.route('/tag/<path:req_path>/')
def tag(req_path):
    print(req_path)
    if os.path.getsize('db.p') > 0:
        with open('db.p', 'rb') as f:
            db = pickle.load(f)
            print(db.get(req_path, 0))
    return redirect(url_for('root_page'))


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(port=8888, debug=True)
