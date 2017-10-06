from flask import abort, redirect, request, url_for
from flask_admin.contrib.sqla import ModelView
from flask_security import current_user

from models import Role, User


class GenericView(ModelView):
    def is_accessible(self):
        if not current_user.is_active or not current_user.is_authenticated:
            return False
        if current_user.admin:
            return True
        if current_user.has_role("superuser"):
            return True
        return False

    def _handle_view(self, name, **kwargs):
        if not self.is_accessible():
            if current_user.is_authenticated:
                abort(403)
            else:
                return redirect(url_for("users.login", next=request.url))


class RoleView(GenericView):
    def __init__(self, session):
        super().__init__(Role, session)


class UserView(GenericView):
    column_exclude_list = ("password", )

    def __init__(self, session):
        super().__init__(User, session)
