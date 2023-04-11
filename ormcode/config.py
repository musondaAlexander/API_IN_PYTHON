from pydantic import BaseSettings

# code yet to be fixed 
class Settings(BaseSettings):
    database_name: str
    database_user: str
    database_password: str
    database_host: str
    database_port: str
    secret_key: str 
    algorithm: str 
    access_token_expire_minutes: int 
    
    class Config:
        env_file = ".env"
        
settings = Settings()