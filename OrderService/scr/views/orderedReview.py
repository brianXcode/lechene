from flask import Response, jsonify, request
from scr.utility.errors import SchemaValidationError
from ..database.models import OrderedReview
from flask_restful import Resource
from mongoengine.errors import ValidationError,FieldDoesNotExist



class OrderedReviews(Resource):

    def get(self):
        order_review = OrderedReview.objects.all()
        return Response(
            order_review.to_json(),
            mimetype="application/json",
            status=200
        )


    def post(self):
        try:
            data = request.get_json()
            ordered = OrderedReview.objects.create(
               ordered_id  = data["ordered_id"],
               rating = data["rating"],
               review = data["review"],
               return_request = data["return_request"]
            )

            ordered.save()
            return Response(ordered.to_json(), mimetype="application/json", status=200)
        except (FieldDoesNotExist, ValidationError):
            raise SchemaValidationError
        

class OrderedReviewDetails(Resource):
    def get(self, id):
        try:
            order_review = OrderedReview.objects.get(id=id).to_json()
            return Response(order_review,mimetype="application/json", status=200 )
        except:
            return jsonify( 
                message="that Id does not exist",
                status=404
            )

    def put(self, id):
        try:

            update_orderReview = OrderedReview.objects.get(id=id)
            data = request.get_json()

            update_orderReview.update(
                ordered_id  = data["ordered_id"],
                rating = data["rating"],
                review = data["review"],
                return_request = data["return_request"]
            )

            update_orderReview.save()  
            return Response(update_orderReview.to_json(), mimetype="application/json", status=200)

        except :
            return jsonify(
                message="that Id does not exist or check the payload",
                status=404
            )

    def delete(self, id):
        try:
            delete_orderReview = OrderedReview.objects.get(id=id)
            delete_orderReview.delete()
            return jsonify({
                "message": "orderedReview deleted successfully"
            })
        except Exception:
            return jsonify(
                message="that Id does not exist",
                status=404
            )


class OrderedReviewSearch(Resource):
    def get(self):
        ordered_id = request.args.get("ordered_id")
        rating = request.args.get("rating")
        review  = request.args.get("review")
        return_request = request.args.get("return_request")
        created_at = request.args.get("created_at")

        if ordered_id:
            orderedReview = OrderedReview.objects(ordered_id__icontains = ordered_id)
        elif rating:
            orderedReview = OrderedReview.objects(rating__lte = rating)
        elif review:
            orderedReview = OrderedReview.objects(review__icontains = review)
        elif return_request:
            orderedReview = OrderedReview.objects(return_request__icontains = return_request)
        elif created_at:
            orderedReview =  OrderedReview.objects(created_at__icontains = created_at)
        else:
            return jsonify({
                "messeage":"please enter a valid field and value"
            })
            

        return Response( orderedReview.to_json(), mimetype="application/json", status=200 )
