from flask import Response, jsonify, request, Blueprint
from flask_restful import Resource 
from ..database.models import User, Profile
from flask_jwt_extended import (
    jwt_required, 
    get_jwt_identity
)
from flask.views import View

""" 
    Users Profile Creation 
"""

# class UserProileApi(Resource):
#     pass

    # @jwt_required()
    # def get(self):
    #     user_id = get_jwt_identity()
    #     id = User.objects.get(id=user_id)

    #     profiles = Profile.objects(
    #         user = id ,
    #         active = True
    #     )
    #     profiles.user = user_id 

    #     return Response (
    #         profiles.to_json(),
    #         mimetype="application/json",
    #         status=200
    #     )

    # @jwt_required()
    # def post(self):
    #     user_id = get_jwt_identity()
    #     body = request.get_json()

    #     try:
    #         profile = Profile.objects.create(
    #             user = User.objects.get(id=user_id),
    #             first_name = body["first_name"],
    #             last_name = body["last_name"],
    #             address = body["address"],
    #             # image = body["image"],  --------> TODO
    #             phone_number = body["phone_number"],
    #             about = body["about"],
    #             active = True
    #         )

    #         profile.save()
       
    #         return Response (
    #                 profile.to_json(),
    #                 mimetype="application/json",
    #                 status=200
    #             )
    #     except:
    #         return jsonify({
    #             "message":"You can not have more than one profile"
    #         })


# class UserProfileDetails(Resource):

#     @jwt_required()
#     def put(self, id):
#         body = request.get_json()
#         user_id = get_jwt_identity()

#         profile = Profile.objects.get(
#             id=id, 
#             user = User.objects.get(id=user_id),
#         )

#         profile.update(
#             first_name = body["first_name"],
#             last_name = body["last_name"],
#             address = body["address"],
#             # image = body["image"],  --------> TODO
#             phone_number = body["phone_number"],
#             about = body["about"],
#         )

#         profile.save()
#         return Response (
#                     profile.to_json(),
#                     mimetype="application/json",
#                     status=200
#                 )

    

""" General Profile """

# class ProileApi(Resource):

    # @jwt_required()
    # def get(self):
       
    #     profiles = Profile.objects(
    #         active = True
    #     )

    #     return Response (
    #         profiles.to_json(),
    #         mimetype="application/json",
    #         status=200
    #     )



""" Modified Profile View and Routes """

profile_api_blueprint = Blueprint("profile_api", __name__)


class ProfileViews(View):

    @profile_api_blueprint.route("/api/profiles", methods = ["GET"])
    @jwt_required()
    def get_all_profile():
        profiles = Profile.objects(active=True)
        return jsonify(
            profiles=profiles
        )

    @profile_api_blueprint.route("/api/profile", methods = ["POST"])
    @jwt_required()
    def create_profile():

        user_id = get_jwt_identity()
        body = request.get_json()
        pro = Profile.objects.with_id(user_id)

        try :
            if pro is None:
                profile = Profile.objects.create(
                    user = User.objects.get(id=user_id),
                    first_name = body["first_name"],
                    last_name = body["last_name"],
                    address = body["address"],
                    # image = body["image"],  --------> TODO
                    phone_number = body["phone_number"],
                    about = body["about"],
                    active = True
                )
                profile.save()
                return jsonify({
                    "response":profile
                })
        except:
            return jsonify({
                "response":"You can not have more than one profile"
            })

    @profile_api_blueprint.route("/api/profile/me", methods = ["GET"])
    @jwt_required()
    def get_profile():
        user_id = get_jwt_identity()
        id = User.objects.get(id=user_id)

        profile = Profile.objects.filter(
            user = id ,
            active = True
        )
        profile.user = user_id 

        return jsonify({
            "response":profile
        })

    @profile_api_blueprint.route("/api/profile/<id>", methods = ["PUT"])
    @jwt_required()
    def update_profile(id):
        user_id = get_jwt_identity()
        body = request.get_json()

        profile = Profile.objects(
            id=id, 
            user = user_id
        )

        profile.update(
            first_name = body["first_name"],
            last_name = body["last_name"],
            address = body["address"],
            # image = body["image"],  --------> TODO
            phone_number = body["phone_number"],
            about = body["about"],
        )

        return jsonify({
            "response":profile
        })


    @profile_api_blueprint.route("/api/profile/<id>", methods = ["DELETE"])
    @jwt_required()
    def delete_profile(id):
        user_id = get_jwt_identity()
        profile = Profile.objects.get(
            id=id, 
            user = User.objects.get(id=user_id),
            active=True
        )

        profile.delete()
        return jsonify({
            "message":"profile succesffully deleted"
        })


        
        
