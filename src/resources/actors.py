from datetime import datetime

from flask import request
from flask_restful import Resource
from marshmallow import ValidationError

from src import db
from src.database.models import Actor
from src.schemas.actors import ActorSchema
from src.services.actor_service import ActorService


class ActorListApi(Resource):
    actor_schema = ActorSchema()

    def get(self, id=None):
        if not id:
            actors = ActorService.fetch_all_actors(db.session).all()
            return self.actor_schema.dump(actors, many=True), 200
        actor = ActorService.fetch_actor_by_id(db.session, id)
        if not actor:
            return '', 404
        return self.actor_schema.dump(actor), 200

    def post(self):
        try:
            actor = self.actor_schema.load(request.json, session=db.session)
        except ValueError as e:
            return {'massage': str(e)}, 400
        db.session.add(actor)
        db.session.commit()
        return self.actor_schema.dump(actor), 201

    def put(self, id):
        actor = ActorService.fetch_actor_by_id(db.session, id)
        if not actor:
            return '', 404
        try:
            actor = self.actor_schema.load(request.json, instance=actor, session=db.session)
        except ValidationError as e:
            return {'massage': str(e)}, 400
        db.session.add(actor)
        db.session.commit()
        return self.actor_schema.dump(actor), 200


    def patch(self, id):
        actor = db.session.query(Actor).filter_by(id=id).first()
        if not actor:
            return '', 404
        actor_json = request.json
        name = actor_json.get('name')
        birthday = datetime.strptime(actor_json.get('birthday'), '%B %d, %Y') if actor_json.get(
            'birthday') else None
        is_active = actor_json.get('is_active')
        if name:
            actor.name = name
        if birthday:
            actor.birthday = birthday
        if is_active:
            actor.is_active = is_active
        db.session.add(actor)
        db.session.commit()
        return {'massage': 'Updated successfully'}, 200

    def delete(self, id):
        actor = ActorService.fetch_actor_by_id(db.session, id)
        if not actor:
            return '', 404
        db.session.delete(actor)
        db.session.commit()
        return '', 204
