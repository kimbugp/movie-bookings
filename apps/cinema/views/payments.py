
from apps.cinema import api
from controllers.basecontroller import BaseController
from flask_restplus import Resource


@api.route("/payments", endpoint="payments")
class PaymentsEndpoint(Resource):
    def post(self):
        body = api.payload
        controller = BaseController(body)
        payment = controller.save()
        return {"payment": payment}, 201
