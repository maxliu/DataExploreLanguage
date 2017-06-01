# Generated from ../antlr/de.g4 by ANTLR 4.6
from antlr4 import *

# This class defines a complete generic visitor for a parse tree produced by deParser.

class deVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by deParser#parse.
    def visitParse(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by deParser#block.
    def visitBlock(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by deParser#stat.
    def visitStat(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by deParser#project.
    def visitProject(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by deParser#assignment.
    def visitAssignment(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by deParser#load.
    def visitLoad(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by deParser#barchart.
    def visitBarchart(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by deParser#subby.
    def visitSubby(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by deParser#header.
    def visitHeader(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by deParser#run.
    def visitRun(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by deParser#statics.
    def visitStatics(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by deParser#plot.
    def visitPlot(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by deParser#bycol.
    def visitBycol(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by deParser#cols.
    def visitCols(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by deParser#dbname.
    def visitDbname(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by deParser#aggDesc.
    def visitAggDesc(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by deParser#aggMean.
    def visitAggMean(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by deParser#aggStd.
    def visitAggStd(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by deParser#aggMedian.
    def visitAggMedian(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by deParser#aggVar.
    def visitAggVar(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by deParser#callFun.
    def visitCallFun(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by deParser#notExpr.
    def visitNotExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by deParser#unaryMinusExpr.
    def visitUnaryMinusExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by deParser#multiplicationExpr.
    def visitMultiplicationExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by deParser#orExpr.
    def visitOrExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by deParser#additiveExpr.
    def visitAdditiveExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by deParser#relationalExpr.
    def visitRelationalExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by deParser#equalityExpr.
    def visitEqualityExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by deParser#andExpr.
    def visitAndExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by deParser#parExpr.
    def visitParExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by deParser#intNumber.
    def visitIntNumber(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by deParser#floatNumber.
    def visitFloatNumber(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by deParser#booleanAtom.
    def visitBooleanAtom(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by deParser#idAtom.
    def visitIdAtom(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by deParser#stringAtom.
    def visitStringAtom(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by deParser#nilAtom.
    def visitNilAtom(self, ctx):
        return self.visitChildren(ctx)


