import pandas as pd
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

# -----------------------------
# STEP 1: READ DATA FROM A FILE
# -----------------------------
# For demo purposes, we’ll create a sample dataset (You can replace with CSV)
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Score': [85, 92, 78, 90, 88],
    'Department': ['HR', 'IT', 'Finance', 'IT', 'HR']
}

df = pd.DataFrame(data)

# -----------------------------
# STEP 2: ANALYZE THE DATA
# -----------------------------
avg_score = df['Score'].mean()
top_scorer = df.loc[df['Score'].idxmax()]

# -----------------------------
# STEP 3: GENERATE PDF REPORT
# -----------------------------
file_name = "Automated_Report.pdf"
pdf = SimpleDocTemplate(file_name, pagesize=A4)

styles = getSampleStyleSheet()
elements = []

# Title
title = Paragraph("<b>Company Performance Report</b>", styles['Title'])
elements.append(title)
elements.append(Spacer(1, 12))

# Summary
summary_text = f"Average Score: {avg_score:.2f}<br/>Top Scorer: {top_scorer['Name']} ({top_scorer['Score']}) from {top_scorer['Department']} Department."
summary = Paragraph(summary_text, styles['Normal'])
elements.append(summary)
elements.append(Spacer(1, 12))

# Table Data
table_data = [df.columns.tolist()] + df.values.tolist()
table = Table(table_data)

# Table Style
table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ('GRID', (0, 0), (-1, -1), 1, colors.black)
]))

elements.append(table)

# Build PDF
pdf.build(elements)

print(f"✅ PDF report generated: {file_name}")
