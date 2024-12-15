from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.core.files.storage import FileSystemStorage
import os
import pandas as pd
from docx import Document

# Create your views here.

class FileUploadView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        uploaded_files = request.FILES.getlist('files')
        file_paths = []
        all_table_data = []  # 用于存储所有文件的表格数据

        for file in uploaded_files:
            fs = FileSystemStorage(location='media/complicates/')
            filename = fs.save(file.name, file)
            file_path = fs.url(filename)
            file_paths.append(file_path)

            # 读取表格数据
            table_data = self.read_table_from_docx(os.path.join('media/complicates/', file.name))
            all_table_data.append({
                'file_name': file.name,
                'table_data': table_data
            })

        return Response({'file_paths': file_paths, 'table_data': all_table_data}, status=201)

    def read_table_from_docx(self, file_path):
        # 使用 python-docx 读取 Word 文档
        doc = Document(file_path)
        table_data = []

        for table in doc.tables:
            # 将表格数据转换为 pandas DataFrame
            for row in table.rows:
                row_data = [cell.text.strip() for cell in row.cells]
                table_data.append(row_data)

        # 将表格数据转换为 DataFrame
        df = pd.DataFrame(table_data)
        return df.to_dict(orient='records')  # 返回字典格式的表格数据
