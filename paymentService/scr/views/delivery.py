from flask import Response, jsonify, request
from flask_restful import Resource
from scr.database.models import Delivery
from scr.utility.errors import FieldDoesNotExistError, SchemaValidationError
from mongoengine.errors import ValidationError,FieldDoesNotExist



class DeliveryApi(Resource):

    def get(self):
        delivery = Delivery.objects.all()
        return Response(delivery.to_json(), mimetype="application/json",status = 200)

    
    def post(self):
        try:
            data = request.get_json()
            delivery = Delivery.objects.create(
                ordered_id = data["ordered_id"],
                delivery_staff_name = data["delivery_staff_name"],
                location = data["location"],
                status = data["status"],
                status_report = data["status_report"]
            )

            delivery.save()
            return Response(delivery.to_json(), mimetype="application/json", status=200)
        except (FieldDoesNotExistError, ValidationError):
            raise SchemaValidationError



class DeliveryDetailsApi(Resource):
    def get(self, id):
        try:
            delivery = Delivery.objects.get(id=id)
            return Response(delivery.to_json(), mimetype="application/json", status=200)
        except:
            return jsonify( 
                message="that Id does not exist",
                status=404
            )
    

    def put(self, id):
        try:
            update_delivery = Delivery.objects.get(id=id)
            data = request.get_json()

            update_delivery.update(
                ordered_id = data["ordered_id"],
                delivery_staff_name = data["delivery_staff_name"],
                location = data["location"],
                status = data["status"],
                status_report = data["status_report"]
            )

            update_delivery.save()
            return Response(update_delivery.to_json(), mimetype="application/json", status=200)
        except :
            return jsonify(
                message="that Id does not exist or check the payload",
                status=404
            )

    
    def delete(self, id):
        try:
            delete_payment = Delivery.objects.get(id=id)
            delete_payment.delete()
            return jsonify({
                "message": "Delivery deleted successfully"
            })
        except Exception:
            return jsonify(
                message="that Id does not exist",
                status=404
            )


    
class DeliverySearchApi(Resource):
    def get(self):
        ordered_id = request.args.get("ordered_id")
        delivery_staff_name  = request.args.get("delivery_staff_name")
        location  = request.args.get("location")
        status = request.args.get("status")
        status_report = request.args.get("status_report")
        delivered_at = request.args.get("delivered_at")

        if ordered_id:
            delivery = Delivery.objects(ordered_id__icontains = ordered_id)
        elif delivery_staff_name :
            delivery = Delivery.objects(delivery_staff_name__icontains = delivery_staff_name)
        elif location:
            delivery = Delivery.objects(location__icontains = location)
        elif status:
            delivery = Delivery.objects(status__icontains = status)
        elif status_report:
            delivery = Delivery.objects(status_report__icontains = status_report)
        elif delivered_at:
            delivery =  Delivery.objects(delivered_at__icontains = delivered_at)
        else:
            return jsonify({
                "messeage":"please enter a valid field and value"
            })
            

        return Response( delivery.to_json(), mimetype="application/json", status=200 )


