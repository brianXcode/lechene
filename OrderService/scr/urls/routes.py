from ..views.orderProduct import OrderProductsApi, OrderProductApi, OrderProductSearchAPi
from ..views.ordered import OrderedApi,OrderedDetailsApi,OrderedSearchApi
from ..views.orderedReview import OrderedReviews, OrderedReviewDetails, OrderedReviewSearch


def initialize_routes(api):
  
    api.add_resource(OrderProductsApi, '/api/orderproducts')
    api.add_resource(OrderProductApi, '/api/orderproducts/<id>')
    api.add_resource(OrderProductSearchAPi, "/api/orderproduct/search/")


    api.add_resource(OrderedApi, '/api/ordered')
    api.add_resource(OrderedDetailsApi, '/api/ordered/<id>')
    api.add_resource(OrderedSearchApi, '/api/ordered/search/')

    api.add_resource(OrderedReviews, '/api/orderedReviews')
    api.add_resource(OrderedReviewDetails, '/api/orderedReviews/<id>')
    api.add_resource(OrderedReviewSearch, '/api/orderedReviews/search/')

   
   