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
        },
        {
          label: "Excel比对工具",
          icon: "i-heroicons-folder-open",
        },
      ],
      [
        {
          label: "导入数据",
          icon: "i-heroicons-arrow-down-tray",
        },
        {
          label: "导出数据",
          icon: "i-heroicons-arrow-up-tray",
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
        },
        {
          label: "打开公文",
          icon: "i-heroicons-folder-open",
        },
      ],
      [
        {
          label: "公文格式模板下载",
          icon: "i-heroicons-document-duplicate",
        },
        {
          label: "导出PDF",
          icon: "i-heroicons-arrow-up-tray",
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
        },
      ],
      [
        {
          label: "投诉管理平台",
          icon: "i-heroicons-pencil-square-20-solid",
          shortcuts: ["E"],
        },
        {
          label: "Duplicate",
          icon: "i-heroicons-document-duplicate-20-solid",
          shortcuts: ["D"],
        },
      ],
      [
        {
          label: "Archive",
          icon: "i-heroicons-archive-box-20-solid",
        },
        {
          label: "Move",
          icon: "i-heroicons-arrow-right-circle-20-solid",
        },
      ],
      [
        {
          label: "Delete",
          icon: "i-heroicons-trash-20-solid",
        },
        {
          label: "Restore",
          icon: "i-heroicons-arrow-left-circle-20-solid",
        },
      ],
    ],
  }
];
