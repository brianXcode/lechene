
from ..views.customOrder import CustomOrderApi, CustomOrderDetailsApi, CustomOrderSearchApi
from ..views.measurement import MeasurementApi, MeasurementDetailsApi, MeasurementSearchApi



def initialize_routes(api):
   api.add_resource(CustomOrderApi, '/api/customOrder')
   api.add_resource(CustomOrderDetailsApi, '/api/customOrder/<id>')
   api.add_resource(CustomOrderSearchApi, '/api/customOrder/search/')


   api.add_resource(MeasurementApi, '/api/measurement')
   api.add_resource(MeasurementDetailsApi, '/api/measurement/<id>')
   api.add_resource(MeasurementSearchApi, '/api/measurement/search/')