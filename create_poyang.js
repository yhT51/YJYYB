const { Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell, WidthType, HeadingLevel, AlignmentType } = require('docx');
const fs = require('fs');
const xlsx = require('node-xlsx');

// 读取Excel文件
console.log('读取鄱阳工单数据...');
const workbook = xlsx.readFile('D:\\\\XLX\\XLXWJ\\鄱阳工单数据_1773391976677.xlsx');
const sheetName = workbook.SheetNames[0];
const worksheet = workbook.Sheets[sheetName];
const jsonData = xlsx.utils.sheet_to_json(worksheet, { header: 1 });

console.log(`共 ${jsonData.length} 条工单`);

// 获取表头
const headers = Object.keys(jsonData[0]);

// 创建Word文档
const doc = new Document({
  sections: [{
    properties: {},
    children: [
      // 标题
      new Paragraph({
        heading: HeadingLevel.HEADING_1,
        alignment: AlignmentType.CENTER,
        children: [
          new TextRun({
            text: "鄱阳县中医院云净血透系统运维报告",
            bold: true,
            size: 32
          })
        ]
      }),

      // 表格
      new Table({
        width: { size: 12240, type: WidthType.DXA },
        columnWidths: new Array(headers.length).fill(12240 / headers.length),
        rows: [
          // 表头
          new TableRow({
            children: headers.map(header =>
              new TableCell({
                width: { size: 12240 / headers.length, type: WidthType.DXA },
                children: [
                  new Paragraph({
                    children: [new TextRun({ text: header, bold: true })]
                  })
                ]
              })
            )
          }),
          // 数据行
          ...jsonData.map(row =>
            new TableRow({
              children: headers.map(header =>
                new TableCell({
                  width: { size: 12240 / headers.length, type: WidthType.DXA },
                  children: [
                    new Paragraph({
                      children: [new TextRun({ text: String(row[header] || '') })]
                    })
                  ]
                })
              )
            })
          )
        ]
      })
    ]
  }]
});

// 保存文档
Packer.toBuffer(doc).then(buffer => {
  fs.writeFileSync('D:\\\\XLX\\XLXWJ\\鄱阳中医院云净血透系统运维报告.docx', buffer);
  console.log('报告已保存');
});
