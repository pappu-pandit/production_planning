from import_export import resources
from .models import production_order

class production_order_resource(resources.ModelResource):
    class meta:
        model=production_order