from app.core.settings.db.sqlite import SessionLocal

# Dependency: Ver Inyección de dependencias
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()