from flask import Blueprint, render_template, request
from config import Config
import json
import uuid

bp = Blueprint("main", __name__)


@bp.route("/", methods=["GET"])
def index():
    return render_template("pages/main/index.jinja", title=Config.APP_NAME)

@bp.route("/out-of-band", methods=["GET"])
def short_oob_url():
    oobid = request.args.get('_oobid')
    try:
        uuid.UUID(oobid)
        oobid = request.args.get('_oobid')
        with open(f'app/static/invitations/{oobid}.json', 'r') as f:
            invitation = json.loads(f.read())
        return invitation
    except:
        return {
            'detail': 'Invitation not found',
            'invitation_id': oobid
        }, 404
