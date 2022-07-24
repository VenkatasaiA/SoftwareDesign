from sqlalchemy import create_engine
from sqlalchemy.engine import reflection
insp = reflection.Inspector.from_engine(engine)
print(insp.get_columns(nstream))