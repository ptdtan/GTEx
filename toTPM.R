#!/usr/bin/env Rscript
#load the necessary libraries
library(clusterSim)
library(argparse)

#creat argument object
parser <- ArgumentParser()
parser$add_argument("--rpkm",type="character", help="RPKM matrix")
parser$add_argument("--tpm", type="character", help="TPM_matrix")

args<- parser$parse_args()

df <- read.table(args$rpkm, header=TRUE)
df <- data.Normalization(df, type="n10", normalization="column")
df <- 1e+06*df
write.table(df, file=args$tpm, sep="\t", col.names=FALSE, row.names=FALSE)
