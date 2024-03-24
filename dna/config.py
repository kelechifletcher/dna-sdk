from pydantic import BaseSettings


class Config(BaseSettings):
    dna_host: str = "localhost:8000"
