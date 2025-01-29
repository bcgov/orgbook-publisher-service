from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    SubmitField,
    PasswordField,
    SelectField,
    EmailField
)
from wtforms.validators import InputRequired

class AdminLoginForm(FlaskForm):
    tenant_id = StringField(
        "Traction Tenant Id", [InputRequired()]
    )
    api_key = PasswordField(
        "Traction API Key", [InputRequired()]
    )
    submit = SubmitField("Login")

class RegisterIssuerForm(FlaskForm):
    namespace = StringField(
        "WebVH Namespace", [InputRequired()]
    )
    identifier = StringField(
        "WebVH Identifier", [InputRequired()]
    )
    submit = SubmitField("Register")

class OfferAuthCredentialForm(FlaskForm):
    email = EmailField(
        "BCGov Email", [InputRequired()]
    )
    issuer = SelectField(
        "Delegated Issuer", [InputRequired()]
    )
    submit = SubmitField("Offer")