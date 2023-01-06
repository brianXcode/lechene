class InternalServerError(Exception):
    pass

class SchemaValidationError(Exception):
    pass

class UpdatingProductError(Exception):
    pass

class DeletingProductError(Exception):
    pass

class ProductNotExistsError(Exception):
    pass

class FieldDoesNotExistError(Exception):
    pass



errors = {
    "InternalServerError": {
        "message": "Something went wrong on the code",
        "status": 500
    },
     "SchemaValidationError": {
         "message": "Request is missing required fields",
         "status": 400
     },
     "UpdatingProductError": {
         "message": "Updating Product added by other is forbidden",
         "status": 403
     },
     "DeletingProductError": {
         "message": "Deleting Product added by other is forbidden",
         "status": 403
     },
     "ProductNotExistsError": {
         "message": "Product with given id doesn't exists",
         "status": 400
     },     
     "FieldDoesNotExistError": {
        "message": "The field is invalid",
        "status": 400
     },

}


#ordered errors

class UpdatingOrderedError(Exception):
    pass

class DeletingOrderedError(Exception):
    pass

class OrderedNotExistsError(Exception):
    pass

class FieldDoesNotExistError(Exception):
    pass


errors = {
     
    "OrderedError": {
         "message": "Updating ordered added by other is forbidden",
         "status": 403
     },
     "DeletingOrderedError": {
         "message": "Deleting ordered added by other is forbidden",
         "status": 403
     },
     "OrderedNotExistsError": {
         "message": "ordered with given id doesn't exists",
         "status": 400
     }, 
     "FieldDoesNotExistError": {
        "message": "The field is invalid",
        "status": 400
     }    
}

