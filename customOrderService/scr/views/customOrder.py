from flask import Response, jsonify, request
from flask_restful import Resource
from scr.database.models import CustomOrder
from scr.utility.errors import FieldDoesNotExistError, SchemaValidationError
from mongoengine.errors import ValidationError



class CustomOrderApi(Resource):
    def get(self):
        customOrder = CustomOrder.objects.all()
        return Response(customOrder.to_json(), mimetype="applicaton/json", status=200)

    def post(self):
        try:
            body = request.get_json()
            productCategoryReq = request.get(
                "127.0.0.1:5000/api/product_category/%s" %body["product_category_id"],
            )
            productSubCategoryReq = request.get(
                "127.0.0.1:5000/api/product_sub_category/%s" %body["product_SubCategory_id"]
            )
            product_category = productCategoryReq.json()
            product_SubCategory = productSubCategoryReq.json()
            
            
            customOrder = CustomOrder.objects.create(
                product_category_id = body["product_category_id"],
                product_SubCategory_id = body["product_SubCategory_id"],
                gender = body["gender"],
                sizes = body["sizes"]
            )

            customOrder.save()
            return Response(customOrder.to_json(), mimetype="application/json", status=200)
        except (FieldDoesNotExistError, ValidationError):
            raise SchemaValidationError


class CustomOrderDetailsApi(Resource):
    def get(self, id):
        try:
            customOrder = CustomOrder.objects.get(id=id)
            return Response(customOrder.to_json(), mimetype="applicaton/json", status=200)
        except:
             return jsonify( 
                message="that Id does not exist",
                status=404
            )

    def put(self, id):
        try:

            customOrder = CustomOrder.objects.get(id=id)
            data = request.get_json()

            customOrder.update(
                    product_category_id = data["product_category_id"],
                    product_SubCategory_id = data["product_SubCategory_id"],
                    gender = data["gender"],
                    sizes = data["sizes"],
                )
            customOrder.save()
            return Response(customOrder.to_json(), mimetype="application/json", status=200)
        except :
            return jsonify(
                message="that Id does not exist or check the payload",
                status=404
            )

  
    
    def delete(self, id):
        try:
            update_customOrder = CustomOrder.objects.get(id=id)
            update_customOrder.delete()
            return jsonify({
                "message": "Delivery deleted successfully"
            })
        except Exception:
            return jsonify(
                message="that Id does not exist",
                status=404
            )




class CustomOrderSearchApi(Resource):
    def get(self):
        product_category_id = request.args.get("product_category_id")
        product_SubCategory_id  = request.args.get("product_SubCategory_id")
        gender  = request.args.get("gender")
        sizes = request.args.get("sizes")
        created_at = request.args.get("created_at")

        if product_category_id:
            customOrder = CustomOrder.objects(product_category_id__icontains = product_category_id)
        elif product_SubCategory_id:
            customOrder = CustomOrder.objects(product_SubCategory_id__icontains = product_SubCategory_id)
        elif gender:
            customOrder = CustomOrder.objects(gender__icontains = gender)
        elif sizes:
            customOrder = CustomOrder.objects(sizes__icontains = sizes)
        elif created_at:
           customOrder =  CustomOrder.objects(created_at__icontains = created_at)
        else:
            return jsonify({
                "messeage":"please enter a valid field and value"
            })
            
        return Response( customOrder.to_json(), mimetype="application/json", status=200 )


