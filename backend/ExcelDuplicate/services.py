import pandas as pd
import os
from .models import ExcelFile, DuplicateResult
from .utils import generate_random_color, highlight_rows

class DuplicateChecker:
    def __init__(self, file_id, columns):
        self.file_id = file_id
        self.columns = columns
        self.excel_file = ExcelFile.objects.get(id=file_id)
        self.duplicate_df = None

    def load_data(self):
        """加载Excel文件数据"""
        df = pd.read_excel(self.excel_file.file.path)
        self.duplicate_df = df[df.duplicated(subset=self.columns, keep=False)].copy()
        return self.duplicate_df

    def find_duplicates(self):
        """查找重复数据并分配组号"""
        if self.duplicate_df.empty:
            return None
        self.duplicate_df['重复组'] = self.duplicate_df.groupby(self.columns).ngroup() + 1
        return self.duplicate_df

    def style_duplicates(self):
        """为每组数据分配随机颜色并应用样式"""
        unique_groups = self.duplicate_df['重复组'].unique()
        colors = {group: generate_random_color() for group in unique_groups}
        styled_df = self.duplicate_df.style.apply(lambda row: highlight_rows(row, colors), axis=1)
        return styled_df

    def sort_duplicates(self):
        """根据重复组对数据进行排序"""
        self.duplicate_df = self.duplicate_df.sort_values(by='重复组').reset_index(drop=True)

    def save_results(self, styled_df):
        """保存结果到Excel文件"""
        result_dir = os.path.join('media', 'duplicate_results')
        os.makedirs(result_dir, exist_ok=True)
        result_file_path = os.path.join(result_dir, f'{self.excel_file.id}_result.xlsx')
        styled_df.to_excel(result_file_path, engine='openpyxl', index=False)
        return result_file_path

    def create_duplicate_result(self, result_file_path):
        """创建DuplicateResult记录"""
        return DuplicateResult.objects.create(
            excel_file=self.excel_file,
            result_file=os.path.relpath(result_file_path, start='media'),
            checked_columns=self.columns,
            duplicate_groups=self.duplicate_df['重复组'].nunique(),
            duplicate_rows=len(self.duplicate_df)
        )
