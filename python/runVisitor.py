
from antlr4 import *
from antlr.deVisitor import *
from antlr.deParser import deParser

# import numpy  as np
import pandas as pd

from bokeh.charts import Bar, output_file, Histogram, save, BoxPlot
from bokeh.layouts import gridplot

from html_merge import mergeHtml

import os

import webbrowser


class runVisitor(deVisitor):

    # (str, DataFrame) pair, store dataframe
    dbs = dict()

    # a global varible for DataFrame
    cur_df = pd.DataFrame()

    # a list of html file names
    htmlFileList = list()

    # project name
    project = ""

    # folder name for generated html files
    htmlDir = "html/"

    # project
    # : 'project' ID '{' stat*  '}'
    # ;
    def visitProject(self, ctx):

        # initialize global varibles
        self.project = ctx.ID().getText()
        self.htmlFileList = list()
        # self.dbs = dict()

        print "Project : ", self.project

        # run scripts inside of { }
        for s in ctx.stat():
            self.visit(s)

        # merge all html files to one html file
        htmlFN = os.path.join(self.htmlDir, self.project + ".html")
        mergeHtml(htmlFN, self.htmlFileList)

        webbrowser.open_new_tab(htmlFN)

        print "%s generated. " % (htmlFN)
        return

    # run
    # : 'run' STRING
    # ;
    def visitRun(self, ctx):
        runStr = str(ctx.STRING().getText()).replace("\"", "")
        try:
            print "run ", runStr
            exec(runStr)
        except:
            print "wrong python scripts"

        return

    # load
    # : LOAD  STRING TO dbname
    # ;
    def visitLoad(self, ctx):

        fileName = str(ctx.STRING().getText()).replace("\"", "")

        dfName   = self.visit(ctx.dbname())

        self.dbs[dfName] = pd.read_csv(fileName)

        print "loading ", fileName, "to ", dfName
        return self.visitChildren(ctx)



    def visitDbname(self, ctx):

        return ctx.ID().getText()

    # statics
    # : aggfuns 'of' cols 'in' dbname
    # ;
    def visitStatics(self, ctx):

        htmlName = str(ctx.getText()) + ".html"

        dfName   = self.visit(ctx.dbname())

        print "descriptions for ", dfName

        if 'object' in ctx.getText():
            df = self.dbs[dfName].astype('object')
        else:
            df = self.dbs[dfName]

        self.cur_df = df

        cols_it = self.visit(ctx.cols())

        num_cols = [col for col in cols_it if df[col].dtypes != 'object']

        if len(num_cols) > 0:

            print "desc of : ", " ,".join(num_cols)

            df_num = df[num_cols].describe()
            htmlFileTmp = os.path.join(self.htmlDir, 'A_' + htmlName)
            df_num.to_html(htmlFileTmp)
            self.htmlFileList += [["desc: " + ", ".join(num_cols), htmlFileTmp]]

        obj_cols = [col for col in cols_it if df[col].dtypes == 'object']

        if len(obj_cols) > 0:

            print "desc of : ", " ,".join(obj_cols)
            htmlFileTmp = os.path.join(self.htmlDir, 'B_' + htmlName)

            df[obj_cols].describe().to_html(htmlFileTmp)

            self.htmlFileList += [["desc: " + ", ".join(obj_cols), htmlFileTmp]]

        return

    # plot
    # : 'distribution' 'of' cols ('by' bycol)? 'in' dbname
    # ;
    def visitPlot(self, ctx):

        htmlName = str(ctx.getText()) + ".html"

        dfName = self.visit(ctx.dbname())

        #df = self.dbs[dfName].dropna(axis=0)
        df = self.dbs[dfName].fillna(0)

        self.visit(ctx.cols())

        if len(ctx.cols().ID()) == 0:

            cols = list(df.columns)
        else:
            cols = [str(colID.getText()) for colID in ctx.cols().ID()]

        pList = []

        if ctx.bycol() is None:
            bycolor = None
        else:
            bycolor = str(ctx.bycol().ID().getText())

        for col in cols:
            print "plot ", col
            if df[col].dtypes == 'object' or len(set(df[col].values)) < 10:
                p = Bar(df, col, group=bycolor, title=col + " by " + bycolor)
                if bycolor is None:
                    pList += [[p]]
                else:
                    q = Bar(df, bycolor, group=col, title=col + " by " + bycolor)
                    pList += [[p, q]]
            else:
                p = Histogram(df, values=col, color=bycolor, title=col)
                q = BoxPlot(df,
                            values=col,
                            label=bycolor,
                            color=bycolor,
                            title=col)
                pList += [[p, q]]

        if len(pList) > 0:
            htmlName = os.path.join(self.htmlDir, 'B_' + htmlName)
            output_file(htmlName)
            self.htmlFileList += [["plot: " + ", ".join(cols), htmlName]]
            save(gridplot(pList))

        return


    # barchart
    # : 'bar' 'of' ID 'by' cols 'in' dbname
    # ;
    def visitBarchart(self, ctx):
        htmlName = str(ctx.getText()) + ".html"

        dfName = self.visit(ctx.dbname())

        #df  = self.dbs[dfName]
        df = self.dbs[dfName].fillna(0)

        col = str(ctx.ID().getText())


        if len(ctx.cols().ID()) == 0:
            cols = None
        else:
            cols = [str(colID.getText()) for colID in ctx.cols().ID()]

        print 'col = ', col, type(col)
        print 'group = ', cols

        # q = Bar(df, label= ['Survived','Sex'], group=['Pclass'], title=col)
        # q = Bar(df, [col,'Sex'], group=cols, title=col)
        htmlName = os.path.join(self.htmlDir, 'C_' + htmlName)
        output_file(htmlName)
        self.htmlFileList += [["plot: " + ", ".join(cols), htmlName]]

        if ctx.subby() is None:
            q = Bar(df, col, group=cols, title=col + " by  " + ", ".join(cols),
                    legend='top_right')

            save(q)

        else:
            pList = []
            subby_col = str(ctx.subby().ID())
            print "subby_col ",subby_col
            print set(df[subby_col].values)

            for v in set(df[subby_col].values):
                print v

                pList.append(
                    Bar(df[df[subby_col]==v], col, group=cols, title = col
                           + " by " + ", ".join(cols)+ " when " + subby_col + " is " + v,
                        legend='top_right'
                        ) )

            save(gridplot([pList]))

        return


    def visitIdAtom(self, ctx):
        return self.visitChildren(ctx)

    # cols
    # : ID (',' ID)*
    # | 'all'
    # ;
    def visitCols(self, ctx):
        if len(ctx.ID()) == 0:
            cols = list(self.cur_df.columns)
        else:
            cols = [str(colID.getText()) for colID in ctx.ID()]
        return cols
