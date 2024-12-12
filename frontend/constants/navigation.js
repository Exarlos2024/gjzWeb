/*
 * @Author: Exarlos
 * @Date: 2024-12-07 00:31:43
 * @LastEditors: Exarlos
 * @LastEditTime: 2024-12-08 13:47:37
 * @Description: 世界上没有低级的法术,只有低级的法师!
 */
export const navMenus = [
  {
    label: "Excel工具",
    items: [
      [
        {
          label: "Excel查重工具",
          icon: "i-heroicons-plus",
          to: "/excel/duplicate"
        },
        {
          label: "Excel比对工具",
          icon: "i-heroicons-folder-open",
          to: "/excel/compare"
        },
      ],
      [
        {
          label: "导入数据",
          icon: "i-heroicons-arrow-down-tray",
          to: "/excel/import"
        },
        {
          label: "导出数据",
          icon: "i-heroicons-arrow-up-tray",
          to: "/excel/export"
        },
      ],
    ],
  },
  {
    label: "Word公文工具",
    items: [
      [
        {
          label: "公文格式化工具",
          icon: "i-heroicons-document-plus",
          to: "/word/format"
        },
        {
          label: "打开公文",
          icon: "i-heroicons-folder-open",
          to: "/word/open"
        },
      ],
      [
        {
          label: "公文格式模板下载",
          icon: "i-heroicons-document-duplicate",
          to: "/word/templates"
        },
        {
          label: "导出PDF",
          icon: "i-heroicons-arrow-up-tray",
          to: "/word/export-pdf"
        },
      ],
    ],
  },
  {
    label: "PDF转换工具",
    items: [
      [
        {
          label: "PDF转Word",
          icon: "i-heroicons-document-arrow-up-20-solid",
          to: "/pdf/to-word"
        },
        {
          label: "PDF转Excel",
          icon: "i-heroicons-table-cells-20-solid",
          to: "/pdf/to-excel"
        },
      ],
      [
        {
          label: "批量转换",
          icon: "i-heroicons-document-duplicate-20-solid",
          to: "/pdf/batch"
        },
        {
          label: "历史记录",
          icon: "i-heroicons-clock-20-solid",
          to: "/pdf/history"
        },
      ],
    ],
  },
  {
    label: "医政医管科",
    items: [
      [
        {
          label: "Profile",
          avatar: {
            src: "/images/Exarlos2.png",
          },
          to: "/medical/profile"
        },
      ],
      [
        {
          label: "投诉管理平台",
          icon: "i-heroicons-pencil-square-20-solid",
          to: "/medical/complaints"
        },
        {
          label: "归档管理",
          icon: "i-heroicons-document-duplicate-20-solid",
          to: "/medical/archive"
        },
      ],
    ],
  }
];
