from flask import Blueprint, jsonify
from scr.database.models import User
from scr.views.auth import (
    AdminSignUpApi,
    TailorSignUpApi,
    StaffSignUpApi,
    VisiorSignUpApi,
    UserSignInApi,
   
)

# from scr.views.profile import(
#     UserProileApi,
#     UserProfileDetails,
#     ProileApi
# )

# from scr.views.reset_password import (
#     ForgotPassword,
#     ResetPassword
# )


def initialize_routes(api):
  
    """ Users Registrations"""
    api.add_resource(AdminSignUpApi, '/api/adminAuth')
    api.add_resource(TailorSignUpApi, '/api/tailorAuth')
    api.add_resource(StaffSignUpApi, '/api/staffAuth')
    api.add_resource(VisiorSignUpApi, '/api/visitorAuth')

    """ Users Signup """
    api.add_resource(UserSignInApi, "/api/userSignIn")



    """  TODO ---> Reset password  """
    # api.add_resource(ForgotPassword, '/api/auth/forgot')
    # api.add_resource(ResetPassword, '/api/auth/reset')

