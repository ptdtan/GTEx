#!/usr/bin/env Rscript
library(argparse)

#creat parser
parser <- ArgumentParser()
parser$add_argument("--input",type="character", help="Expression matrix")
parser$add_argument("--header",type="character", help="Gene id or transcriptid")
parser$add_argument("--output", type="character", help="top 100 Expression genes")

args<- parser$parse_args()

df <- read.table(args$input)
m <- apply(df, 1, median)
c <- read.table(args$header)
df.GeneObj <- data.frame(geneid=c, median=m)
df.GeneObj <- df.GeneObj[ order(df.GeneObj$median, decreasing=TRUE) ,]
write.table(df.GeneObj[1:100, ], file=args$output, sep="\t", col.names=FALSE, row.names=FALSE)
