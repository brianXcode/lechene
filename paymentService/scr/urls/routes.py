from ..views.payment import PaymentApi, PaymentDetailsApi, PaymentSearchApi
from ..views.delivery import DeliveryApi, DeliveryDetailsApi, DeliverySearchApi



def initialize_routes(api):     

    api.add_resource(PaymentApi, '/api/payment')
    api.add_resource(PaymentDetailsApi, '/api/payment/<id>')
    api.add_resource(PaymentSearchApi, '/api/payment/search/')


    api.add_resource(DeliveryApi, '/api/delivery')
    api.add_resource(DeliveryDetailsApi, '/api/delivery/<id>')
    api.add_resource(DeliverySearchApi, '/api/delivery/search/')