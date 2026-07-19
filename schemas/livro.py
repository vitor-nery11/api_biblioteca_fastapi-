from pydantic import BaseModel, Field

class LivroCreate(BaseModel):
  titulo:str = Field(
      min_length=3,
      max_length=100
  )
  autor:str = Field(
      min_length=3,
      max_length=80
  )

  paginas:int = Field(
      gt=0 
  )
  disponivel:bool
  ano_publicacao:int = Field(
      gt=1400,
      le=2026
  )


class LivroResponse(BaseModel):
    titulo:str 
    autor:str 


