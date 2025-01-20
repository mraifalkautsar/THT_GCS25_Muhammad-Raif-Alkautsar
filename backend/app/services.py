from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from app.models import Base, Item

# konfigurasi database
DATABASE_URL = "postgresql://user:password@db:5432/mydatabase"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# buat semua tabel yang didefinisikan di Base
Base.metadata.create_all(bind=engine)

# fungsi untuk mengambil semua item dari database
def get_items():
    with SessionLocal() as session:
        return session.query(Item).all()

# fungsi untuk membuat item baru di database
def create_item(name, description):
    with SessionLocal() as session:
        new_item = Item(name=name, description=description)
        session.add(new_item)
        session.commit()
        return new_item

# fungsi untuk menghapus item dari database berdasarkan id
def delete_item(item_id):
    with SessionLocal() as session:
        item = session.query(Item).get(item_id)
        if item:
            session.delete(item)
            session.commit()