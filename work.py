import sqlalchemy
from sqlalchemy.orm import Query

from models import db_session, User, Subscription, Streamers



def user_db_add_user(chat_id, first_name=None, last_name=None, username=None):
    user = db_session.query(User).filter(User.user_id == chat_id).first()
    if user: # если chat_id уже есть в БД - обновляет инфу
        user.username = username
        user.first_name = first_name
        user.last_name = last_name
    else:
        new_user = User(chat_id, first_name, last_name, username) # если chat_id нет в БД - добавляет
        db_session.add(new_user)    
    try:
        db_session.commit() # обновляет данные в БД
        return 'add_user: User created' if not user else 'add_user: User is exist, data have updated'
    except sqlalchemy.exc.IntegrityError:
        db_session.rollback()
        return 'add_user: Error'


def subscriptions_db_add_sub(chat_id, streamer_id):
    subs = Subscription.query.filter(Subscription.user_id == chat_id,Subscription.streamer_id == streamer_id).first()
    if not subs:
        print(subs)
        sub_new = Subscription()
        sub_new.streamer_id = streamer_id
        sub_new.user_id = chat_id
        db_session.add(sub_new)
        # db_session.add(Subscription.user_id == chat_id, Subscription.streamer_id == streamer_id)
        db_session.commit()


def db_add_streamer(streamer_name):
    print('sn1 %s' % streamer_name)
    print('sn2 %s' % Streamers.query.filter(Streamers.streamer_name == streamer_name).first())
    select = Streamers()
    # select = select.streamer_name
    print('sn3 %s' % select)
    if streamer_name != select.streamer_name:

        streamer_new = Streamers()
        streamer_new.streamer_name = streamer_name
        db_session.add(streamer_new)
        try:
            db_session.commit() # обновляет данные в БД
            print('commit')
        except sqlalchemy.exc.IntegrityError:
            db_session.rollback()
    streamer = Streamers().query.filter(Streamers.streamer_name == streamer_name).first()
    streamerid = streamer.id
    return streamerid



if __name__ == '__main__':
    pass