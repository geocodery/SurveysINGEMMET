import os, arcpy

jsonCaract  = r'D:\APPS\SURVEY\BDG_DGR_GEOPEDOLOGIA\json\Caracterizacion.json'
# jsonQeoquim = r'D:\APPS\SURVEY\BDG_DGR_GEOPEDOLOGIA\json\Geoquimica.json'

pathGdb = r'D:\APPS\SURVEY\BDG_DGR_GEOPEDOLOGIA\GPT_MS_POG.gdb'

tbcarac   = 'TB_MS_LAB_CARACT'
# tbgeoquim = 'TB_MS_LAB_GEOQUIM2'

# os.path.join(pathGdb, tbcarac)

def main():
    for x in [tbcarac]:
        ftx = arcpy.JSONToFeatures_conversion(jsonCaract, 'in_memory\\ft_%s' % x)
        copy = arcpy.TableToTable_conversion(ftx, pathGdb, x)

if __name__ == '__main__':
    main()