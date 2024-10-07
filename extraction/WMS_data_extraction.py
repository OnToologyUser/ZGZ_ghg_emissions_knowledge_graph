# %%
### Import block
from owslib.wms import WebMapService

# %%
### Config and describe service
wms = WebMapService('http://localhost/geoserver/ows?service=WMS&version=1.1.1&request=GetCapabilities')#http://idezar.zaragoza.es/wms/IDEZar_base/IDEZar_base')
wms = WebMapService('https://usage.geocat.live/mapping/ows?SERVICE=WMS&')

print(wms.identification.type, 
      wms.identification.version, 
      wms.identification.title,
      wms.identification.abstract)

# %%
# List capabilities
print(list(wms.contents))
item = "green_roof_suitability:roof_suitability" #"FE_FBK_single_tree_detection_v2:fbk_single_tree_detection_v2"
print(wms[item].title, "\n",
      wms[item].boundingBoxWGS84, "\n",
      wms[item].crsOptions, "\n",
      wms[item].styles, "\n",
      [op.name for op in wms.operations])
print(wms.getOperationByName('GetMap').methods, "\n",
      wms.getOperationByName('GetMap').formatOptions)

# %%
### Extract data
data = wms.getmap(  layers=[item],
                    styles=[item],#'IDEZar_base_Distritos'],
                    srs='EPSG:4326',
                    bbox= wms[item].boundingBoxWGS84,
                    size=(300, 250),
                    format='application/atom+xml',
                    transparent=True
                    )
# %%
### Store data
out = open('data/WMS/'+item+'/raw/'+item+'.xml', 'wb')
out.write(data.read())
out.close()

