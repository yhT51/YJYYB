const { Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
        AlignmentType, BorderStyle, WidthType, ShadingType, VerticalAlign } = require('docx');
const fs = require('fs');

const borderStyle = { style: BorderStyle.SINGLE, size: 4, color: "4472C4" };
const borders = { top: borderStyle, bottom: borderStyle, left: borderStyle, right: borderStyle };
const noBorder = { style: BorderStyle.NONE, size: 0, color: "FFFFFF" };
const noBorders = { top: noBorder, bottom: noBorder, left: noBorder, right: noBorder };

function cell(text, opts = {}) {
  const {
    bold = false, color = "000000", fontSize = 22,
    align = AlignmentType.CENTER, shading = null,
    colSpan = 1, width = 1600, verticalAlign = VerticalAlign.CENTER
  } = opts;

  return new TableCell({
    columnSpan: colSpan,
    width: { size: width, type: WidthType.DXA },
    borders,
    shading: shading || { fill: "FFFFFF", type: ShadingType.CLEAR },
    margins: { top: 100, bottom: 100, left: 120, right: 120 },
    verticalAlign,
    children: [new Paragraph({
      alignment: align,
      children: [new TextRun({ text, bold, color, size: fontSize, font: "宋体" })]
    })]
  });
}

function labelCell(text, opts = {}) {
  return cell(text, {
    bold: true, color: "1F497D", fontSize: 22,
    shading: { fill: "DCE6F1", type: ShadingType.CLEAR },
    ...opts
  });
}

const totalWidth = 9360;
// 列宽分配：序号800 | 内容3760 | 数量1600 | 单价1600 | 总价1600
const col = [800, 3760, 1600, 1600, 1600];

const doc = new Document({
  sections: [{
    properties: {
      page: {
        size: { width: 12240, height: 15840 },
        margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 }
      }
    },
    children: [
      // 标题
      new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { before: 200, after: 400 },
        children: [new TextRun({ text: "云净报价单", bold: true, size: 44, font: "宋体", color: "1F3864" })]
      }),

      // 主表格
      new Table({
        width: { size: totalWidth, type: WidthType.DXA },
        columnWidths: col,
        rows: [
          // 第一行：报价单位
          new TableRow({ children: [
            labelCell("报价单位", { width: col[0] }),
            cell("深圳云净之信息技术有限公司", { width: col[1] + col[2], colSpan: 2, align: AlignmentType.CENTER }),
            labelCell("联系人", { width: col[3] }),
            cell("尹浩", { width: col[4] }),
          ]}),
          // 第二行：联系电话
          new TableRow({ children: [
            labelCell("联系电话", { width: col[0] }),
            cell("16620994974", { width: col[1] + col[2], colSpan: 2, align: AlignmentType.CENTER }),
            labelCell("报价日期", { width: col[3] }),
            cell("2026/3/13", { width: col[4] }),
          ]}),
          // 第三行：客户名称
          new TableRow({ children: [
            labelCell("客户名称", { width: col[0] }),
            cell("民望血液透析中心", { width: col[1] + col[2] + col[3], colSpan: 3, align: AlignmentType.CENTER }),
          ]}),
          // 表头行
          new TableRow({ children: [
            cell("序  号", { bold: true, color: "1F497D", shading: { fill: "DCE6F1", type: ShadingType.CLEAR }, width: col[0] }),
            cell("内  容", { bold: true, color: "1F497D", shading: { fill: "DCE6F1", type: ShadingType.CLEAR }, width: col[1] }),
            cell("数  量", { bold: true, color: "1F497D", shading: { fill: "DCE6F1", type: ShadingType.CLEAR }, width: col[2] }),
            cell("单  价", { bold: true, color: "1F497D", shading: { fill: "DCE6F1", type: ShadingType.CLEAR }, width: col[3] }),
            cell("总  价", { bold: true, color: "1F497D", shading: { fill: "DCE6F1", type: ShadingType.CLEAR }, width: col[4] }),
          ]}),
          // 数据行
          new TableRow({ children: [
            cell("1", { width: col[0] }),
            cell("云净定制平板", { width: col[1] }),
            cell("1台", { width: col[2] }),
            cell("2000", { width: col[3] }),
            cell("2000", { width: col[4] }),
          ]}),
          // 总价行
          new TableRow({ children: [
            cell("总价", { bold: true, color: "1F497D", colSpan: 4, width: col[0]+col[1]+col[2]+col[3],
              shading: { fill: "DCE6F1", type: ShadingType.CLEAR } }),
            cell("2000元", { bold: true, color: "C00000", width: col[4] }),
          ]}),
          // 备注行
          new TableRow({ children: [
            new TableCell({
              columnSpan: 5,
              width: { size: totalWidth, type: WidthType.DXA },
              borders,
              margins: { top: 100, bottom: 100, left: 200, right: 200 },
              children: [new Paragraph({
                alignment: AlignmentType.CENTER,
                children: [new TextRun({
                  text: "备注：1、此方案截止日期为2026年3月31日",
                  size: 20, font: "宋体", color: "595959"
                })]
              })]
            })
          ]}),
        ]
      }),

      // 落款
      new Paragraph({ spacing: { before: 600 } }),
      new Paragraph({
        alignment: AlignmentType.CENTER,
        children: [new TextRun({ text: "深圳云净之信息技术有限公司", bold: true, size: 26, font: "宋体", color: "1F3864" })]
      }),
      new Paragraph({ spacing: { before: 100 } }),
      new Paragraph({
        alignment: AlignmentType.CENTER,
        children: [new TextRun({ text: "2026年  3月  13日", size: 24, font: "宋体", color: "1F3864" })]
      }),
    ]
  }]
});

Packer.toBuffer(doc).then(buffer => {
  fs.writeFileSync('D:\\XLX\\XLXWJ\\民望血液透析中心报价单.docx', buffer);
  console.log('报价单已生成');
});
