from datetime import datetime

from src.model import db
from src.utils.model import BaseModel


class SwiperModel(BaseModel):
    __tablename__ = 'swiper'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)  # 标题
    description = db.Column(db.String(255), nullable=False)  # 描述
    image = db.Column(db.String(255), nullable=False)  # 图片
    url = db.Column(db.String(500), nullable=False)  # 跳转地址
    crearetime = db.Column("creare_time", db.DateTime, default=datetime.utcnow)  # 创建时间