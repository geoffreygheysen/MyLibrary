from contextlib import contextmanager
from sqlalchemy.orm import sessionmaker
from app import engine

Session = sessionmaker(bind=engine)

@contextmanager
def session_scope():
    from app import db
    
    session = db.session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise  # relancer l'erreur après rollback
    finally:
        session.close()  # fermeture propre de la session
