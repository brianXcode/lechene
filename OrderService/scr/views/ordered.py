from flask import Response, jsonify, request
from scr.utility.errors import InternalServerError, SchemaValidationError
from ..database.models import Ordered
from flask_restful import Resource 
from mongoengine.errors import ValidationError, FieldDoesNotExist, DoesNotExist



class OrderedApi(Resource):
    def get(self):
        ordered = Ordered.objects.all()
        return Response(
            ordered.to_json(),
            mimetype="application/json",
            status=200
        )


    def post(self):
        try:
            data = request.get_json()
            ordered = Ordered.objects.create(
               order_product_id  = data["order_product_id"]
            )

            ordered.save()
            return Response(ordered.to_json(), mimetype="application/json", status=200)
       
        except (FieldDoesNotExist, ValidationError):
            raise SchemaValidationError
        


class OrderedDetailsApi(Resource):
    def get(self, id):
        try:
            ordered = Ordered.objects.get(id=id).to_json()
            return Response(ordered, mimetype="application/json", status=200)
        except:
            return jsonify(
                message="that Id does not exist",
                status=404
            )
    
    def put(self, id):
        try:

            update_ordered = Ordered.objects.get(id=id)
            data = request.get_json()

            update_ordered.update(
                order_product_id = data["order_product_id"],  
            )

            update_ordered.save()  
            return Response(update_ordered.to_json(), mimetype="application/json", status=200)

        except :
            return jsonify(
                message="that Id does not exist or check the payload",
                status=404
            )


    def delete(self, id):
        try:
            delete_ordered = Ordered.objects.get(id=id)
            delete_ordered.delete()
            return jsonify({
                "message": "order-product deleted successfully"
            })
        except Exception:
            return jsonify(
                message="that Id does not exist",
                status=404
            )


class OrderedSearchApi(Resource):
    def get(self):
        order_product_id = request.args.get("order_product_id")
        ordered_date = request.args.get("ordered_date")
        
        if order_product_id:
            ordered = Ordered.objects(order_product_id__icontains = order_product_id)
        elif ordered_date:
            ordered =  Ordered.objects(ordered_date__icontains = ordered_date)
        else:
            return jsonify({
                "message": "Please enter a valid field name"
            })

        return Response(ordered.to_json(), mimetype="application/json", status=200)
        