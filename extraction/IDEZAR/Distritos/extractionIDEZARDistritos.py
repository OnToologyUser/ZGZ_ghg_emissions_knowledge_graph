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
## List capabilities
# list(wms.contents)
# print(wms['distritos'].title, "\n",
#       wms['distritos'].boundingBoxWGS84, "\n",
#       wms['distritos'].crsOptions, "\n",
#       wms['distritos'].styles, "\n",
#       [op.name for op in wms.operations])
# print(wms.getOperationByName('GetMap').methods, "\n",
#       wms.getOperationByName('GetMap').formatOptions)

# %%
### Extract and store data
data = wms.getmap(  layers=['distritos'],
                    styles=['IDEZar_base_Distritos'],
                    srs='EPSG:4326',
                    bbox= wms["distritos"].boundingBoxWGS84,
                    size=(300, 250),
                    format='application/atom+xml',
                    transparent=True
                    )
out = open('data/IDEZAR/Distritos/raw/distritos.xml', 'wb')
out.write(data.read())
out.close()

# %%
