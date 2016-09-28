import xlrd
oligo_sheet = (xlrd.open_workbook("kh_oligos.xlsx")).sheet_by_index(0)
reference = (open("reference.txt")).read()


def reverse_complement(text):
    text = text[::-1].upper().replace(' ','')
    reverse_complement_text = text.translate(str.maketrans('ACGT','TGCA'))
    return reverse_complement_text


def oligo_search(reference, oligo_sheet):
    oligo_column = 2
    reference = reference.upper().replace(' ','')
    rc_reference = reverse_complement(reference)
    matching_oligos = []

    for i in range(oligo_sheet.nrows):
        oligo = (oligo_sheet.cell_value(
                    rowx=i,
                    colx=oligo_column)
                    .upper().replace(" ",""))
        if i < oligo_sheet.nrows and oligo != "" and ((oligo in reference) or (oligo in rc_reference)):
            matching_oligos.append(oligo_sheet.cell_value(rowx=i, colx=oligo_column-1))

    if not matching_oligos:
        return("No oligos match the reference.")
    else:
        return(matching_oligos)


print(oligo_search(reference, oligo_sheet))