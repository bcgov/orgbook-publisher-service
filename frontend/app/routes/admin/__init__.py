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


# @bp.before_request
# def before_request_callback():
#     if not session.get('tenant_id'):
#         return redirect(url_for("admin.logout"))


@bp.route("/issuers", methods=["GET"])
def get_issuers():
    if not session.get('tenant_id'):
        return redirect(url_for("admin.logout"))

    publisher = PublisherController()
    issuers = publisher.get_issuers()
    print(issuers)
    registry = publisher.get_registry()
    print(registry)



@bp.route("/", methods=["GET"])
def index():
    if not session.get('tenant_id'):
        return redirect(url_for("admin.logout"))

    publisher = PublisherController()
    issuers = publisher.get_issuers()
    registry = publisher.get_registry()
    issuers = [{
        'id': 'did:web:example.com:mines-act:chief-permitting-officer',
        'name': 'Chief Permitting Officer',
        'active': True,
    },{
        'id': 'did:web:example.com:petroleum-and-natural-gas-act:director-of-petroleum-lands',
        'name': 'Director of Petroleum Lands',
        'active': False,
    }]
    
    form_issuer_registration = RegisterIssuerForm()
    form_offer_auth_credential = OfferAuthCredentialForm()
    return render_template(
        'pages/admin/index.jinja',
        issuers=issuers,
        form_issuer_registration=form_issuer_registration,
        form_offer_auth_credential=form_offer_auth_credential
    )


@bp.route("/logout", methods=["GET"])
def logout():
    session.clear()
    session['tenant_id'] = None
    return redirect(url_for('admin.login'))


@bp.route("/login", methods=["GET", "POST"])
def login():
    form_login = AdminLoginForm()
    if request.method == "POST":
        traction = TractionController()
        session['access_token'] = traction.admin_login(
            request.form.get("tenant_id"),
            request.form.get("api_key"),
        )
        session['tenant_id'] = request.form.get("tenant_id")
        return redirect(url_for('admin.index'))
        
    return render_template(
        'pages/admin/login.jinja',
        form_login=form_login
    )