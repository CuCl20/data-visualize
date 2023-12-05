我们小组计划使用d3.js来实现对自然灾害数据（台风和地震）的可视化。
数据集来源：
typhoon.csv 来自中国科学院海洋科学研究中心的中国近海台风路径集合数据集。
链接：http://msdc.qdio.ac.cn/data/metadata-special-detail?id=1422759994058625025
earthquake.csv 来自国家地震科学数据中心的中国台网正式地震目录。
链接：https://data.earthquake.cn/datashare/report.shtml?PAGEID=earthquake_zhengshi
项目中的g.py用于将世界地图（.shp格式）转为.geojson的格式，用于在d3.js的可视化中生成世界地图。
python的实现.png是一位小组成员使用python做出来的台风数据可视化粗略形态，图中展示了台风数据集前1000条所表示的台风的路径，其线条粗细和颜色区分了台风的强度。
对于地震数据集，我们的设想是采用大小不一的圆表示强度不同的地震。
我们计划在d3.js的可视化中加入交互，包括拖动地图，选择时间，鼠标滑动查看具体数据等操作，目前已将地图可视化。
