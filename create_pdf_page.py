
from fpdf import FPDF

# table data
table_data = (
    ("Heading 1", "Heading 2", "Heading 3", "Heading 4"),
    ("sample 11", "sample 12", " sample 13", "sample 14"),
    ("sample 21", "sample 22", " sample 23", "sample 24"),
    ("sample 31", "sample 32", " sample 33", "sample 34"),
)

# create instance of PDF class
pdf = FPDF()

# add page to pdf
pdf.add_page()
# set font 
pdf.set_font("Times", size=16)


# add text to pdf width, height, text, border, line breaks, allignment, fill, link
with pdf.table() as table:
    for data_row in table_data:
        row = table.row()
        for datum in data_row:
            row.cell(datum)


# save pdf to file
pdf.output("test_pdf.pdf")
print("pdf generated")
