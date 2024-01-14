from flask_admin.contrib.sqla import ModelView
from sqlalchemy import event
from wtforms.fields.simple import PasswordField
from wtforms.validators import DataRequired

from my_app.models import TaiKhoanNhanVien, TaiKhoanAdmin, TaiKhoanKhach, Phong, LoaiPhong, LoaiKhach, ThongSoQuyDinh, \
    ChiTietThue
from my_app import db, admin, pass_KS
from flask_login import logout_user, current_user
from flask import redirect, session, url_for, request, flash, render_template
from flask_admin import BaseView, expose
import hashlib
from flask_wtf import FlaskForm


class AuthenticatedView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated


class logoutView(BaseView):
    @expose("/")
    def index(self):
        logout_user()
        del session['khach']
        return redirect("/")

    def is_accessible(self):
        return current_user.is_authenticated


@event.listens_for(TaiKhoanNhanVien.password, 'set', retval=True)
def hash_user_password(target, value, oldvalue, initiator):
    if value != oldvalue:
        return str(hashlib.md5(value.encode("utf-8")).digest())
    return str(value)


class ThongSoQuyDinhView(ModelView):
        def is_accessible(self):
            return True

        def inaccessible_callback(self, name, **kwargs):
            return redirect(url_for('tsqd', next=request.url))


admin.add_view(AuthenticatedView(TaiKhoanAdmin, db.session, name='Tài Khoản Admin'))
admin.add_view(AuthenticatedView(TaiKhoanNhanVien, db.session, name='Tài Khoản Nhân viên'))
admin.add_view(AuthenticatedView(TaiKhoanKhach, db.session, name='Tài Khoản Khách'))
admin.add_view(AuthenticatedView(Phong, db.session, name='Phòng'))
admin.add_view(AuthenticatedView(LoaiKhach, db.session, name='Loại Khách'))
admin.add_view(AuthenticatedView(LoaiPhong, db.session, name='Loại phòng'))
admin.add_view(AuthenticatedView(ChiTietThue, db.session, name='Chi tiet thue'))
admin.add_view(ThongSoQuyDinhView(ThongSoQuyDinh, db.session, name='Thông số quy định', endpoint='thongsoquydinhview'))

admin.add_view(logoutView(name="Đăng xuất"))
