from datetime import datetime

from app import models, db
from flask import current_app as app, jsonify, abort, request


@app.route('/')
@app.route('//')
def page_index():
    return 'Главная страничка)'


@app.route('/users', methods=['GET'])
def page_get_users():
    """ Возвращает список всех пользователей. """
    users = db.session.query(models.User).all()
    return jsonify([user.serialize() for user in users])


@app.route('/users/<int:user_id>', methods=['GET'])
def page_get_user(user_id):
    """ Возвращает пользователя по его id. """
    user = db.session.query(models.User).filter(models.User.id == user_id).first()
    if user is None:
        abort(404)
    return jsonify(user.serialize())


@app.route('/orders', methods=['GET'])
def page_get_orders():
    """ Возвращает список всех ордеров. """
    orders = db.session.query(models.Order).all()
    return jsonify([order.serialize() for order in orders])


@app.route('/orders/<int:order_id>', methods=['GET'])
def page_get_order(order_id):
    """ Возвращаем список ордера по его id.(с поверкой) """
    order = db.session.query(models.Order).filter(models.Order.id == order_id).first()
    if order is None:
        abort(404)
    return jsonify(order.serialize())


@app.route('/offers', methods=['GET'])
def page_get_offers():
    """ Показываем все offers. """
    offers = db.session.query(models.Offer).all()
    return jsonify([offer.serialize() for offer in offers])


@app.route('/offers/<int:offer_id>', methods=['GET'])
def page_get_offer(offer_id):
    """ Показываем один offer по его id. """
    offer = db.session.query(models.Offer).filter(models.Offer.id == offer_id).first()
    if offer is None:
        abort(404)
    return jsonify(offer.serialize())


@app.route('/users', methods=['POST'])
def create_user():
    """ Создаем нового пользователя """
    data = request.json
    db.session.add(models.User(**data))
    db.session.commit()
    return 'В процессе завершения создания'


@app.route('/users/<int:user_id>', methods=['PUT'])
def edit_user(user_id):
    """ Меняем данные пользователя по его id. """
    data = request.json
    user = db.session.query(models.User).filter(models.User.id == user_id).first()
    if user is None:
        abort(404)

    db.session.query(models.User).filter(models.User.id == user_id).update(data)
    db.session.commit()

    return f' пользователь с id: {user_id}'


@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """ Удаляем пользователя по его id. """
    result = db.session.query(models.User).filter(models.User.id == user_id).delete()
    if result == 0:
        abort(404)
    db.session.commit()

    return 'удален безвозвратно'


@app.route('/orders', methods=['POST'])
def create_order():
    """ Создаем новый заказ """
    data = request.json

    for field_name, field_value in data.items():
        if isinstance(field_value, str) and (field_name == "start_date" or field_name == "end_date"):
            data[field_name] = datetime.strptime(field_value, '%m/%d/%Y').date()

    db.session.add(models.Order(**data))
    db.session.commit()
    return 'создан новый заказ!'


@app.route('/orders/<int:order_id>', methods=['PUT'])
def edit_order(order_id):
    """ Меняем данные заказа по его id. """
    data = request.json
    user = db.session.query(models.Order).filter(models.Order.id == order_id).first()

    if user is None:
        abort(404)

    db.session.query(models.Order).filter(models.Order.id == order_id).update(data)
    db.session.commit()

    return f' что-то изменилось в заказе с id: {order_id}'


@app.route('/orders/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    """ Удаляем заказ по его id. """
    result = db.session.query(models.Order).filter(models.Order.id == order_id).delete()
    if result == 0:
        abort(404)
    db.session.commit()

    return '... безвозвратно потерян один из заказов ...'


@app.route('/offers', methods=['POST'])
def create_offer():
    """ Создаем новое предложение (офер) """
    data = request.json

    db.session.add(models.Offer(**data))
    db.session.commit()
    return 'данные ушли за новым offer!'


@app.route('/offers/<int:offer_id>', methods=['PUT'])
def edit_offer(offer_id):
    """ Меняем данные предложения (офера) по его id. """
    data = request.json
    user = db.session.query(models.Offer).filter(models.Offer.id == offer_id).first()

    if user is None:
        abort(404)

    db.session.query(models.Offer).filter(models.Offer.id == offer_id).update(data)
    db.session.commit()

    return f'данные ушли... что-то изменилось в офере с id: {offer_id}'


@app.route('/offers/<int:offer_id>', methods=['DELETE'])
def delete_offer(offer_id):
    """ Удаляем офер по  id. """
    result = db.session.query(models.Offer).filter(models.Offer.id == offer_id).delete()
    if result == 0:
        abort(404)
    db.session.commit()

    return 'Безвозвратно потерян один из оферов!!!'
