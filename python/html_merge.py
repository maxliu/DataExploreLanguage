


upper = """

<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <title>Bokeh Plot</title>

<link rel="stylesheet" href="https://cdn.pydata.org/bokeh/release/bokeh-0.12.2.min.css" type="text/css" />

<script type="text/javascript" src="https://cdn.pydata.org/bokeh/release/bokeh-0.12.2.min.js"></script>
<script type="text/javascript">
    Bokeh.set_log_level("info");
</script>
        <style>
          html {
            width: 100%;
            height: 100%;
          }
          body {
            width: 90%;
            height: 100%;
            margin: auto;
          }
        </style>
    </head>
    <body>

"""

lower = """

    </body>
</html>

"""


def mergeHtml(newFile, fileList):
    with open(newFile, 'w') as fw:
        fw.write(upper)
        for title, fn in fileList:
            with open(fn, 'r') as fr:
                l = fr.readlines()
            if "table" in l[0]:
                lTemp = l
            else:

                lTemp  =[]
                flag = False
                for lx in l:
                    if flag:
                        lTemp.append(lx)
                    if "<body>" in lx:
                        flag = True
                    if "</body>" in lx:
                        break

            lTemp.insert(0, "<p>%s</p>" %(title))
            for lx in lTemp:
                fw.write(lx)

        fw.write(lower)

if __name__ == "__main__":

    newFile = "mergeTest.html"
    fileList = [["desc-A", 'A_descofallindf1.html'],
                ["desc-B", 'B_descofallindf1.html'],
                ["plot-A", 'distributionofcylbycylindf1.html'],
                ["plot-B", 'distributionofmodelbycylindf1.html']
                ]
    mergeHtml(newFile, fileList)
