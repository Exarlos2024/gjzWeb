from django.urls import path
from .views import ExcelViewSet

# # 创建视图集的实例
# excel_viewset = ExcelViewSet.as_view({
#     'post': 'analyze',  # POST请求对应analyze方法
#     'post': 'check_duplicates',  # POST请求对应check_duplicates方法
#     'get': 'download_results'  # GET请求对应download_results方法
# })

# urlpatterns = [
#     path('analyze/', excel_viewset, name='analyze_excel'),  # 分析上传的Excel文件
#     path('check-duplicates/', excel_viewset, name='check_duplicates'),  # 执行查重操作
#     path('download-results/', excel_viewset, name='download_results'),  # 下载查重结果
# ]

# 创建视图集的实例
analyze_viewset = ExcelViewSet.as_view({'post': 'analyze'})
check_duplicates_viewset = ExcelViewSet.as_view({'post': 'check_duplicates'})
download_results_viewset = ExcelViewSet.as_view({'get': 'download_results'})

urlpatterns = [
    path('analyze/', analyze_viewset, name='analyze_excel'),  # 分析上传的Excel文件
    path('check-duplicates/', check_duplicates_viewset, name='check_duplicates'),  # 执行查重操作
    path('download-results/', download_results_viewset, name='download_results'),  # 下载查重结果
]

