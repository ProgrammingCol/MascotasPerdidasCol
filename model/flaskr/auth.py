from crypt import methods
import functools
from flask import (Blueprint,flash,g,redirect,render_template,request,session,url_for)
from werkzeug.security import check_password_hash,generate_password_hash
from flaskr.db import get_db

bp = Blueprint('auth',__name__,url_prefix='/auth')

@bp.route('/registro',methods=('GET','POST'))
def registrar():
    if request.method == 'POST':
        username = request.form['usuario']
        password = request.form['password']
        db = get_db()
        error = None
        
        if not username:
            error = 'El usuario es requerido'
        elif not password:
            error = 'La password es requerida'
        
        if error is None:
            try:
                db.execute(
                    'INSERT INTO user (username, password) VALUES (?,?)',
                    (username,generate_password_hash(password))
                )
                db.commit()
            except db.IntegrityError:
                error = f'Usuario {username} ya esta registrado'
            else: return redirect(url_for('auth.login'))
        flash(error)
    return render_template('auth/registro.html')

@bp.route('/login',methods=('GET','POST'))
def login():
    if request.method == 'POST':
        username = request.form['usuario']
        password = request.form['password']
        db = get_db()
        error = None
        
        user = db.execute(
            "SELECT * FROM user WHERE username = ?",
            (username)
        ).fetchone()
        
        if user is None and (not check_password_hash(user['password'],password)):
            error = 'Usuario o password incorrectos'
            
        if error is None:
            session.clear()
            session['user_id']=user['id']
            return redirect(url_for('index'))
        
    return render_template('auth.login.html')

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    
    if user_id == None:
        g.user = None
    else:
        g.user = get_db().execute(
            "SELECT * FROM user WHERE id = ?", (user_id)
        ).fetchone()
        
@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

def login_required(view):
    @functools.wraps(view)
    def wrapped_views(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_views

    