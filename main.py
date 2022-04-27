from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///users.db', echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class User(Base):
  __tablename__ = 'users'

  id = Column(Integer, primary_key=True)
  name = Column(String)
  fullname = Column(String)
  nickname = Column(String)
  
  def __repr__(self):
    return f'<User(name={self.name}, fullname={self.fullname}, nickname={self.nickname})>'

if __name__ == '__main__':
  Base.metadata.create_all(engine)

  mario_user = User(name='Mario', fullname='Mario Alfredo Torres Lagos', nickname='Negro')

  # print(mario_user.name)
  # print(mario_user.fullname)
  # print(mario_user.nickname)
  # session.add(mario_user)
  # #print(session.new)
  # session.commit()
  # print(mario_user.id)

  new_users = [
    User(name='Francisco', fullname='Francisco Javier Torres Lagos', nickname='Mac'),
    User(name='Maria', fullname='Maria Paz Torres Lagos', nickname='Mary'),
    User(name='Felipe', fullname='Felipe Ignacio Torres Lagos', nickname='Pollin'),
  ]

  session.add_all(new_users)
  session.commit()

  for user in new_users:
    print(user.id)    
  

  


