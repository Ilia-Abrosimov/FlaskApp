from flask_restful import Resource

from src import db
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
        pass

    def put(self):
        pass

    def patch(self):
        pass

    def delete(self):
        pass
