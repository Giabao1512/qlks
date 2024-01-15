from sqlalchemy import Column, Integer, String, ForeignKey, Float, Boolean, DateTime
from sqlalchemy.orm import relationship, backref
from flask_login import UserMixin
from datetime import datetime
from sqlalchemy import Date
from my_app import db


# class BaseModel(db.Model):
#     __abstract__ = True
#     id = Column(Integer, primary_key=True, autoincrement=True)

class TaiKhoanNhanVien(db.Model, UserMixin):
    emp_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    username = Column(String(100), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    active = Column(Boolean, default=True)
    taiKhoanAdmin = relationship('TaiKhoanAdmin', backref='TaiKhoanNhanVien', lazy=True)

    def __str__(self):
        return self.name

    def get_id(self):
        return self.emp_id

    def is_active(self):
        return self.active

    def activate_user(self):
        self.active = True

    def get_username(self):
        return self.username

    def get_urole(self):
        return 'NhanVien'


class TaiKhoanAdmin(db.Model):
    admin_id = Column(Integer, primary_key=True, autoincrement=True)
    emp_id = Column(Integer, ForeignKey(TaiKhoanNhanVien.emp_id), nullable=False)

    def __str__(self):
        return str(self.admin_id)


class LoaiPhong(db.Model):
    MaLoaiPhong = Column(Integer, primary_key=True, autoincrement=True)
    LoaiPhong = Column(String(5), nullable=False)
    DonGia = Column(Integer, nullable=False)
    phong = relationship('Phong', backref='LoaiPhong', lazy=True)
    @property
    def giaPhong(self):
        return self.thong_so_quy_dinh.giaPhong if self.thong_so_quy_dinh else None

    @property
    def LP(self):
        return self.thong_so_quy_dinh.LP if self.thong_so_quy_dinh else None
    def __str__(self):
        return str(self.LoaiPhong)


class Phong(db.Model):
    MaPhong = Column(Integer, primary_key=True, autoincrement=True)
    MaLoaiPhong = Column(Integer, ForeignKey(LoaiPhong.MaLoaiPhong), nullable=False)
    GhiChu = Column(String(255), nullable=True)
    TinhTrang = Column(String(2), nullable=False)
    HinhAnh = Column(String(255), nullable=True)

    chiTietThue = relationship('ChiTietThue', backref='phong_chiTietThue', lazy=True)
    danhGia = relationship('DanhGiaCuaKhach', backref='phong_danhGia', lazy=True)

    def __str__(self):
        return str(self.MaPhong)


class LoaiKhach(db.Model):
    MaLoaiKhach = Column(Integer, primary_key=True, autoincrement=True)
    LoaiKhach = Column(String(50), nullable=False)
    khach = relationship('Khach', backref='LoaiKhach', lazy=True)


class Khach(db.Model):
    MaKhach = Column(Integer, primary_key=True, autoincrement=True)
    MaLoaiKhach = Column(Integer, ForeignKey(LoaiKhach.MaLoaiKhach), nullable=False)
    CMND = Column(String(12), nullable=False)
    DiaChi = Column(String(255), nullable=False)
    NgaySinh = Column(Date, nullable=True)
    SDT = Column(Integer, nullable=False)
    chiTietThue = relationship('ChiTietThue', backref='Khach_ChiTietThue', lazy=True)
    danhGia = relationship('DanhGiaCuaKhach', backref='Khach_danhGia', lazy=True)
    taiKhoan = relationship('TaiKhoanKhach', backref='Khach_TaiKhoan', lazy=True)

    def __str__(self):
        return str(self.MaKhach)


class TaiKhoanKhach(db.Model):
    MaKhach = Column(Integer, ForeignKey(Khach.MaKhach), primary_key=True, nullable=False)
    username = Column(String(100), nullable=False, unique=True)
    password = Column(String(100), nullable=False)

    def get_id(self):
        return self.MaKhach

    def is_active(self):
        return True

    def get_username(self):
        return self.username

    def get_urole(self):
        return 'Khach'



class ChiTietThue(db.Model):
    MaHopDong = Column(Integer, primary_key=True, autoincrement=True)
    MaPhong = Column(Integer, ForeignKey(Phong.MaPhong), nullable=False)
    MaKhach = Column(Integer, ForeignKey(Khach.MaKhach), nullable=False)
    NgayBatDau = Column(DateTime, default=datetime.now(), nullable=False)
    SoNgayODuKien = Column(Integer, nullable=True)
    hopDong = relationship('HoaDon', backref='ChiTietThue', lazy=True)
    SoLuongKhach = Column(Integer, nullable=False)

    def __str__(self):
        return str(self.MaHopDong)


class DanhGiaCuaKhach(db.Model):
    MaDanhGia = Column(Integer, primary_key=True, autoincrement=True)
    MaPhong = Column(Integer, ForeignKey(Phong.MaPhong), nullable=False)
    MaKhach = Column(Integer, ForeignKey(Khach.MaKhach), nullable=False)
    NgayBatDau = Column(DateTime, default=datetime.now(), nullable=False)
    NoiDung = Column(String(255), nullable=False)
    SoSao = Column(Integer, nullable=True)

    def __str__(self):
        return str(self.MaDanhGia)


class HoaDon(db.Model):
    MaHopDong = Column(Integer, ForeignKey(ChiTietThue.MaHopDong), primary_key=True)
    NgayTraPhong = Column(DateTime, default=datetime.now(), nullable=False)
    ThanhTien = Column(Integer, nullable=False)

    def __str__(self):
        return str(self.MaHopDong)


class ThongSoQuyDinh(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    SoLuongPhong = Column(Integer, nullable=False)
    giaPhong = Column(Float, nullable=False)
    SoKhachTrongPhong = Column(Integer, nullable=False)
    TyLePhuThu = Column(Float, nullable=False)
    loai_phong_id = Column(Integer, ForeignKey('loai_phong.MaLoaiPhong'))

    loai_phong = relationship('LoaiPhong', backref='thong_so_quy_dinh')


if __name__ == "__main__":
    db.create_all()
