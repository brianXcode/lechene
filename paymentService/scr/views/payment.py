
from flask import Response, jsonify, request
from flask_restful import Resource
from ..database.models import Payment
from mongoengine.errors import ValidationError,FieldDoesNotExist
from scr.utility.errors import SchemaValidationError




class PaymentApi(Resource):
    def get(self):
        payment = Payment.objects.all()
        return Response(
            payment.to_json(), 
            mimetype="application/json", 
            status=200
        )

    def post(self):
        try:
            data = request.get_json()
            payment = Payment.objects.create(
                payment_mode = data["payment_mode"],
                currency = data["currency"],
                transaction_status = data["transaction_status"],
                amount_paid = data["amount_paid"]
            )
            payment.save()
            return Response(payment.to_json(), mimetype="application/json", status=200)

        except (FieldDoesNotExist, ValidationError):
            raise SchemaValidationError


class PaymentDetailsApi(Resource):
    def get(self, id):
        try:
            payment = Payment.objects.get(id=id).to_json()
            return Response(payment,mimetype="application/json", status=200 )
        except:
            return jsonify( 
                message="that Id does not exist",
                status=404
            )

    def put(self, id):
        try:

            update_payment = Payment.objects.get(id=id)
            data = request.get_json()

            update_payment.update(
                payment_mode = data["payment_mode"],
                currency = data["currency"],
                transaction_status = data["transaction_status"],
                amount_paid = data["amount_paid"]
            )

            update_payment.save()  
            return Response(update_payment.to_json(), mimetype="application/json", status=200)

        except :
            return jsonify(
                message="that Id does not exist or check the payload",
                status=404
            )

    def delete(self, id):
        try:
            delete_payment = Payment.objects.get(id=id)
            delete_payment.delete()
            return jsonify({
                "message": "orderedReview deleted successfully"
            })
        except Exception:
            return jsonify(
                message="that Id does not exist",
                status=404
            )


class PaymentSearchApi(Resource):
    def get(self):
        payment_mode = request.args.get("payment_mode")
        currency  = request.args.get("currency")
        transaction_status  = request.args.get("transaction_status")
        amount_paid = request.args.get("amount_paid")
        created_at = request.args.get("created_at")

        if payment_mode:
            payment = Payment.objects(payment_mode__icontains = payment_mode)
        elif currency :
            payment = Payment.objects(currency__icontains = currency)
        elif transaction_status:
            payment = Payment.objects(transaction_status__icontains = transaction_status)
        elif amount_paid:
            payment = Payment.objects(amount_paid__lte = amount_paid)
        elif created_at:
            payment =  Payment.objects(created_at__icontains = created_at)
        else:
            return jsonify({
                "messeage":"please enter a valid field and value"
            })
            

        return Response( payment.to_json(), mimetype="application/json", status=200 )


