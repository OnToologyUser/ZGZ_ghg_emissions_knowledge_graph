# %%
### Import block
from owslib.wms import WebMapService

# %%
### Config and describe service
wms = WebMapService('http://idezar.zaragoza.es/wms/IDEZar_base/IDEZar_base')
# print(wms.identification.type, 
#       wms.identification.version, 
#       wms.identification.title,
#       wms.identification.abstract)

# %%
### List capabilities
# list(wms.contents)
# print(wms['BARRIO_DELIMITACION'].title,
#       wms['BARRIO_DELIMITACION'].boundingBoxWGS84, "\n",
#       wms['BARRIO_DELIMITACION'].crsOptions, "\n",
#       wms['BARRIO_DELIMITACION'].styles, "\n",
#       [op.name for op in wms.operations])
# print(wms.getOperationByName('GetMap').methods, "\n",
#       wms.getOperationByName('GetMap').formatOptions)

# %%
### Extract and store data
data = wms.getmap(  layers=['BARRIO_DELIMITACION'],
                    styles=['BARRIO_DELIMITACION'],
                    srs='EPSG:4326',
                    bbox=(-1.1792692070827793, 41.4488949772607, -0.6664220744662599, 41.93490845284696),
                    size=(300, 250),
                    format='application/atom+xml',
                    transparent=True
                    )
out = open('data/IDEZAR/Barrios/raw/BARRIO_DELIMITACION.xml', 'wb')
out.write(data.read())
out.close()

# %%
