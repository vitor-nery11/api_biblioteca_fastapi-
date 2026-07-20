from sqlalchemy import String,Integer,Boolean
from sqlalchemy.orm import Mapped,mapped_column

from database import Base 

class Livro(Base):
  __tablename__ = 'livros'

  id: Mapped[int] = mapped_column(primary_key=True)
  titulo: Mapped[str] = mapped_column(String(100))
  autor: Mapped[str] = mapped_column(String(80))
  paginas: Mapped[int] = mapped_column(Integer)
  disponivel: Mapped[bool] = mapped_column(Boolean)
  ano_publicacao: Mapped[int] = mapped_column(Integer)

  

