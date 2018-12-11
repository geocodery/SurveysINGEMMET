import arcpy
import os

inTable = r'D:\APPS\SURVEY\BDG_DGR_GEOPEDOLOGIA\GPT_MS_POG.gdb\TB_MS_FOTOS'
fileLocation = r'D:\APPS\SURVEY\BDG_DGR_GEOPEDOLOGIA\photos'

i = 0
with arcpy.da.SearchCursor(inTable, ['IMAGE', 'NOMBRE']) as cursor:
    for item in cursor:
    	i=i+1
        attachment = item[0]
        filename = item[1] + str(i) + ".jpg"
        open(fileLocation + os.sep + filename, 'wb').write(attachment.tobytes())
        del item
        del filename
        del attachment
