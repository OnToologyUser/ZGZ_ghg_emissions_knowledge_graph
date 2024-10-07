# %%
### Import block
from owslib.wfs import WebFeatureService
import geopandas as gpd
# %%
### Config and describe service
wfs = WebFeatureService('https://usage.geocat.live/mapping/ows?service=WFS&version=1.0.0&')

print(wfs.identification.type, "\n",
      wfs.identification.version, "\n",
      wfs.identification.title, "\n",
      wfs.identification.abstract)

# %%
# List capabilities
print(list(wfs.contents))
item = "green_roof_suitability:roof_suitability" #"FE_FBK_single_tree_detection_v2:fbk_single_tree_detection_v2"
print(wfs[item].title, "\n",
      wfs[item].boundingBoxWGS84, "\n",
      wfs[item].crsOptions, "\n",
      wfs[item].styles, "\n",
      [op.name for op in wfs.operations])
print(wfs.getOperationByName('GetFeature').methods, "\n",
      wfs.getOperationByName('GetFeature').formatOptions)
# %%
### Extract data
data = wfs.getfeature(  typename=[item],
                        # styles=[item],#'IDEZar_base_Distritos'],
                        srsname='EPSG:4326',
                        # bbox= wfs[item].boundingBoxWGS84,
                        # size=(300, 250),
                        outputFormat='SHAPE-ZIP',
                        # transparent=True
                    )
# %%
### Store data
out = open('data/WMS/'+item+'/raw/'+item+'.zip', 'wb')
out.write(data.read())
out.close()


# %%
gdf = gpd.read_file('data/WMS/'+item+'/raw/'+item+'.zip')
# %%
