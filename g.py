import geopandas as gpd

# 输入 Shapefile 文件路径
shp_path = 'wmap/ne_110m_admin_0_countries_lakes.shp'

# 读取 Shapefile
gdf = gpd.read_file(shp_path)

# 输出 GeoJSON 文件路径
geojson_path = 'output.geojson'

# 将 GeoDataFrame 保存为 GeoJSON
gdf.to_file(geojson_path, driver='GeoJSON')
