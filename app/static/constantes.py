from app import db
from app.models.site import Site

#Seteamos variable para paginar registros
ITEMS_PERPAGE = Site.obtain_site().pages