import pandas as pd
import matplotlib.pyplot as plt
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from datetime import datetime
import os

# 註冊中文字型 (這裡用 HeiseiMin-W3 日文字型，支援繁體中文也可顯示)
pdfmetrics.registerFont(UnicodeCIDFont('HeiseiMin-W3'))

# ===== 1. 讀取數據 =====
data = pd.read_csv("sample_data.csv")

# ===== 2. 簡單數據分析 =====
mean_val = data["value"].mean()
max_val = data["value"].max()
min_val = data["value"].min()

# ===== 3. 畫圖 =====
plt.figure()
plt.plot(data["time"], data["value"], marker="o")
plt.title("Measurement Data")
plt.xlabel("Time")
plt.ylabel("Value")
chart_path = "report_chart.png"
plt.savefig(chart_path)
plt.close()

# ===== 4. 產生 PDF 報告 =====
report_path = "report_report.pdf"
doc = SimpleDocTemplate(report_path)
styles = getSampleStyleSheet()
story = []

styles["Normal"].fontName = "HeiseiMin-W3"
styles["Title"].fontName = "HeiseiMin-W3"
styles["Heading2"].fontName = "HeiseiMin-W3"

story.append(Paragraph("📑 測試報告", styles["Title"]))
story.append(Spacer(1, 20))
story.append(Paragraph(f"產生日期: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", styles["Normal"]))
story.append(Spacer(1, 20))

story.append(Paragraph("數據摘要:", styles["Heading2"]))
story.append(Paragraph(f"平均值: {mean_val:.2f}", styles["Normal"]))
story.append(Paragraph(f"最大值: {max_val}", styles["Normal"]))
story.append(Paragraph(f"最小值: {min_val}", styles["Normal"]))
story.append(Spacer(1, 20))

story.append(Paragraph("數據圖表:", styles["Heading2"]))
story.append(Image(chart_path, width=400, height=300))

doc.build(story)

print(f"✅ 報告已生成: {os.path.abspath(report_path)}")