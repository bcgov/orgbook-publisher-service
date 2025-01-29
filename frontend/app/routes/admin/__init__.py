from flask import (
    Blueprint,
    render_template,
    url_for,
    session,
    redirect,
    jsonify,
    request,
)
from config import Config
from app.plugins.publisher import PublisherController
from app.plugins.traction import TractionController
from .forms import (
    AdminLoginForm, 
    RegisterIssuerForm, 
    OfferAuthCredentialForm
)

bp = Blueprint("admin", __name__)


@bp.before_request
def before_request_callback():
    if "tenant_id" not in session:
        return redirect(url_for("admin.logout"))


@bp.route("/logout", methods=["GET"])
def logout():
    session.clear()
    return redirect(url_for('admin.login'))


@bp.route("/login", methods=["GET", "POST"])
def login():
    form_login = AdminLoginForm()
    if request.method == "POST":
        traction = TractionController()
        session['access_token'] = traction.admin_login(
            request.form.tenant_id,
            request.form.api_key,
        )
        session['tenant_id'] = request.form.tenant_id
        
    return render_template(
        'pages/admin/login.jinja',
        form_login=form_login
    )


@bp.route("/", methods=["GET"])
def index():
    publisher = PublisherController()
    issuers = publisher.get_issuers()
    
    form_issuer_registration = RegisterIssuerForm()
    form_offer_auth_credential = OfferAuthCredentialForm()
    return render_template(
        'pages/admin/index.jinja',
        issuers=issuers,
        form_issuer_registration=form_issuer_registration,
        form_offer_auth_credential=form_offer_auth_credential
    )