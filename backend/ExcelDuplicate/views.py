from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.http import HttpResponse
import pandas as pd
import numpy as np
from .models import ExcelFile, DuplicateResult
from .serializers import ExcelFileSerializer, DuplicateResultSerializer
from .services import DuplicateChecker
import logging
import os  # 导入 os 模块

# 创建一个 logger
logger = logging.getLogger('myapp')

class ExcelViewSet(viewsets.ViewSet):
    
    @action(detail=False, methods=['POST'])
    def analyze(self, request):
        """分析上传的Excel文件"""
        logger.debug("Received request for analyze.")
        try:
            # 从请求中获取上传的文件
            file = request.FILES.get('file')
            print("上传的文件:", file.name)  # 打印上传的文件名
            
            # 如果没有找到文件，返回400错误
            if not file:
                logger.error("No file found in the request.")
                return Response({'error': '未找到文件'}, status=status.HTTP_400_BAD_REQUEST)

            # 使用pandas读取Excel文件
            df = pd.read_excel(file)
            print("成功读取Excel文件，行数:", len(df), "列数:", len(df.columns))  # 打印行数和列数
            
            # 创建ExcelFile记录，保存文件的相关信息
            excel_file = ExcelFile.objects.create(
                file=file,  # 保存文件对象
                original_filename=file.name,  # 保存原始文件名
                user=request.user,  # 记录上传用户
                rows=len(df),  # 记录行数
                columns=len(df.columns),  # 记录列数
                headers=df.columns.tolist()  # 记录列头
            )
            print("创建ExcelFile记录，ID:", excel_file.id)  # 打印创建的记录ID

            logger.info(f"Excel file {file.name} processed successfully with ID {excel_file.id}.")

            # 返回分析结果，包括文件ID、文件名、行数、列数和列头
            return Response({
                'fileId': excel_file.id,
                'name': file.name,
                'rows': len(df),
                'columns': len(df.columns),
                'headers': df.columns.tolist()
            })

        except Exception as e:
            logger.exception("An error occurred during the analyze process.")
            # 捕获异常并返回错误信息
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['POST'])
    def check_duplicates(self, request):
        """执行查重操作"""
        file_id = request.data.get('fileId')
        columns = request.data.get('columns', [])
        
        if not file_id or not columns:
            return Response({'error': '参数错误'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            checker = DuplicateChecker(file_id, columns)
            checker.load_data()
            duplicates = checker.find_duplicates()

            if duplicates is None:
                return Response({'groupCount': 0, 'rowCount': 0})

            checker.sort_duplicates()  # 在样式应用后进行排序
            styled_df = checker.style_duplicates()
            result_file_path = checker.save_results(styled_df)
            result = checker.create_duplicate_result(result_file_path)

            return Response({
                'groupCount': result.duplicate_groups,
                'rowCount': result.duplicate_rows
            })

        except ExcelFile.DoesNotExist:
            logger.error("Excel file does not exist.")
            return Response({'error': '文件不存在'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            logger.exception("An error occurred during the check_duplicates process.")
            # 捕获其他异常并返回错误信息
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['GET'])
    def download_results(self, request):
        """下载查重结果"""
        logger.debug("Received request for download_results.")
        print(f"当前工作目录: {os.getcwd()}")  # 打印当前工作目录
        print(f"当前文件路径: {os.path.abspath(__file__)}")  # 打印当前文件路径
        print(f"当前文件名: {__file__}")  # 打印当前文件名

        try:
            # 从请求参数中获取文件ID
            file_id = request.query_params.get('fileId')
            print("接收到的下载请求文件ID:", file_id)  # 打印下载请求的文件ID
            
            # 获取最新的查重结果记录
            result = DuplicateResult.objects.filter(excel_file_id=file_id).latest('created_at')
            print("找到的查重结果记录ID:", result.id)  # 打印找到的查重结果ID

            # 检查文件路径并修正
            result_file_path = self._get_corrected_file_path(result.result_file.path)
            print("查重结果文件路径:", result_file_path)  # 打印查重结果文件路径

            if not os.path.exists(result_file_path):
                logger.error(f"File does not exist: {result_file_path}")
                return Response({'error': '结果文件不存在'}, status=status.HTTP_404_NOT_FOUND)

            # 打开结果文件并返回给用户
            with open(result_file_path, 'rb') as f:
                response = HttpResponse(
                    f.read(),
                    content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
                )
                response['Content-Disposition'] = f'attachment; filename=duplicate_result.xlsx'
                logger.info(f"Results downloaded for file ID {file_id}.")
                return response

        except DuplicateResult.DoesNotExist:
            logger.error("Duplicate result does not exist.")
            return Response({'error': '结果文件不存在'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            logger.exception("An error occurred during the download_results process.")
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def _get_corrected_file_path(self, file_path):
        """修正文件路径，确保没有重复的'media'目录"""
        print("原始查重结果文件路径:", file_path)  # 打印原始路径
        if 'media/media/' in file_path:
            file_path = file_path.replace('media/media/', 'media/')
        if 'media\\media\\' in file_path:
            file_path = file_path.replace('media\\media\\', 'media\\')
        return os.path.normpath(file_path)  # 规范化路径
