from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.units import inch
 
doc = SimpleDocTemplate("pdfs/simple_table.pdf", pagesize=A4)

# container for the 'Flowable' objects
elements = []
 
data= [['00', '01', '02', '03', '04'],
       ['10', '11', '12', '13', '14'],
       ['20', '21', '22', '23', '24'],
       ['30', '31', '32', '33', '34']]
t=Table(data)
t.setStyle(TableStyle(
                [
                    ('GRID', (0, 0), (-1, -1), 1, colors.black),
                    ('BACKGROUND', (0, 0), (-1, -1), colors.green),
                    ('FONTSIZE', (0, 0), (-1, -1), 8),
                    ('ALIGN',(0,0),(-1,-1),'LEFT'),
                    ('VALIGN',(0,0),(-1,-1),'TOP'),
                ]
            ))
for x in range(10):
    elements.append(t)
    Story = [Spacer(1,2*inch)]
    elements.append(Spacer(1,2*inch))

# write the document to disk
doc.build(elements)


