import time
from flask import Response, jsonify, request
from ..database.models import OrderProduct
from flask_restful import Resource 
import requests 



class OrderProductsApi(Resource):

    def get(self):
        order_product = OrderProduct.objects.all().to_json()
        return Response(
            order_product,
            mimetype="application/json",
            status=200
        )
    
    def post(self):
        body = request.get_json()
        
        req = requests.get("http://127.0.0.1:5000/api/product/%s" %body["id"])
        product = req.json()

        ordered = OrderProduct.objects.create(
            product_id  = body["product_id"],
            price = product["sale_price"],
            quantity = body["quantity"],
            status = "completed"
        )
        ordered.save()

        return Response(
            product, 
            mimetype="application/json", 
            status=200
        )
        # return jsonify(product)
      
    

class OrderProductApi(Resource):
    def get(self, id):
        try:
            product = OrderProduct.objects.get(id=id).to_json()
            return Response(product, mimetype="application/json", status=200 )
        except:
            return jsonify( 
                message="that Id does not exist",
                status=404
            )


    def put(self, id):
        try:

            update_orderproduct = OrderProduct.objects.get(id=id)
            data = request.get_json()

            update_orderproduct.update(
                product_id = data["product_id"],
                added_fee = data["added_fee"],
                quantity = data["quantity"],
            )

            update_orderproduct.save()  
            return Response(update_orderproduct.to_json(), mimetype="application/json", status=200)

        except :
            return jsonify(
                message="that Id does not exist or check the payload",
                status=404
            )


    def delete(self, id):
        try:
            delete_product = OrderProduct.objects.get(id=id)
            delete_product.delete()
            return jsonify({
                "message": "order-product deleted successfully"
            })
        except Exception:
            return jsonify(
                message="that Id does not exist",
                status=404
            )


class OrderProductSearchAPi(Resource):
    def get(self):
        product_id = request.args.get("product_id")
        added_fee = request.args.get("added_fee")
        status  = request.args.get("status")
        quantity = request.args.get("quantity")
        created_at = request.args.get("created_at")
        

        if product_id:
            orderproducts = OrderProduct.objects(product_id__icontains = product_id)
        elif added_fee:
            orderproducts = OrderProduct.objects(added_fee__lte = added_fee)
        elif status:
            orderproducts = OrderProduct.objects(status__icontains = status)
        elif quantity:
            orderproducts = OrderProduct.objects(quantity__lte = quantity)
        elif created_at:
            orderproducts =  OrderProduct.objects(created_at__icontains = created_at)
        else:
            return jsonify({
                "messeage":"please enter a valid field and value"
            })
            

        return Response( orderproducts.to_json(), mimetype="application/json", status=200 )

