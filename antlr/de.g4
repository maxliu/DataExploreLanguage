grammar de;

parse
 : block EOF
 ;

block
 : stat*
 | project*
 ;

stat
 : assignment
 | load
 | statics
 | plot
 | run
 | header
 | barchart
 ;

project
 : 'project' ID '{' stat*  '}'
 ;

assignment
 : ID ASSIGN expr SCOL
 ;

load
 : LOAD  STRING TO  dbname 
 ;

barchart
 : 'bar' 'of' ID 'by' cols subby? 'in' dbname
 ;

subby
 : 'subBy' ID
 ;

header
 : 'header' 'to' ID*
 ;

run
 : 'run' STRING
 ;

statics
 : aggfuns 'of' cols 'as'? 'object'?  'in' dbname 
 ;


plot
 : 'distribution' 'of' cols ('by' bycol)? 'in' dbname
 ;

bycol
 : ID 
 ;

cols
 : ID (',' ID)*
 | 'all'
 ;

dbname
 : ID
 ;

aggfuns
 : 'desc'            #aggDesc
 | 'mean'            #aggMean
 | 'std'             #aggStd
 | 'median'          #aggMedian
 | 'var'             #aggVar
 ;


expr
 : MINUS expr                           #unaryMinusExpr
 | NOT expr                             #notExpr
 | expr op=(MULT | DIV | MOD) expr      #multiplicationExpr
 | expr op=(PLUS | MINUS) expr          #additiveExpr
 | expr op=(LTEQ | GTEQ | LT | GT) expr #relationalExpr
 | expr op=(EQ | NEQ) expr              #equalityExpr
 | expr AND expr                        #andExpr
 | expr OR expr                         #orExpr
 | ID OPAR ID* CPAR                     #callFun
 ;

atom
 : OPAR expr CPAR #parExpr
 | INT            #intNumber
 | FLOAT          #floatNumber
 | (TRUE | FALSE) #booleanAtom
 | ID             #idAtom
 | STRING         #stringAtom
 | NIL            #nilAtom
 ;
LOAD : 'load';
TO   : 'to';
OR   : '||';
AND  : '&&';
EQ   : '==';
NEQ  : '!=';
GT   : '>';
LT   : '<';
GTEQ : '>=';
LTEQ : '<=';
PLUS : '+';
MINUS : '-';
MULT : '*';
DIV  : '/';
MOD  : '%';
POW  : '^';
NOT  : '!';

SCOL : ';';
ASSIGN : '=';
OPAR : '(';
CPAR : ')';
OBRACE : '{';
CBRACE : '}';

TRUE : 'true';
FALSE : 'false';
NIL  : 'nil';
IF   : 'if';
ELSE : 'else';
WHILE : 'while';
FUNDEF: 'def';
LOG  : 'log';
UNTIL: 'until';


ID
 : [a-zA-Z_] [a-zA-Z_0-9]*
 ;

INT
 : [0-9]+
 ;

FLOAT
 : [0-9]+ '.' [0-9]* 
 | '.' [0-9]+
 ;

STRING
 : '"' (~["\r\n] | '""')* '"'  // ~ means not, not \r, ", and \n
 ;

fragment
Comment_s
: '#' | '%' 
;

COMMENT
 : Comment_s  ~[\r\n]* -> skip
 ;

SPACE
 : [ \t\r\n] -> skip
 ;

OTHER
 : . 
 ;
