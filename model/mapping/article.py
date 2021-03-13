from model.mapping import Base, generate_id

from sqlalchemy import Column, String, UniqueConstraint, Integer


class Article(Base):
    __tablename__ = 'articles'
    __table_args__ = (UniqueConstraint('name', 'price'),)

    id = Column(String(36), default=generate_id, primary_key=True)

    name = Column(String(50), nullable=False)
    price = Column(Integer(), nullable=False)

    def __repr__(self):
        return "<Article(%s %s)>" % (self.name, self.price)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
        }
