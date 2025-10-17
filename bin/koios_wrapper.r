library(KOIOS)
setwd("C:/Users/ldyer/Documents/KOIOS2.0/KOIOS/")

##### Input #####

#Load the OMOP Genomic Concept library
concepts <- loadConcepts()

#Load the VCF file
vcf <- loadVCF(userVCF = "SomeVCF.vcf ")

#Set the reference genome to "auto"
ref <- "hg19"

##### Run - Single VCF #####
if(ref == "auto"){
  ref <- findReference(vcf)
}

ref.df <- loadReference(ref)

vcf.df <- processVCF(vcf)
vcf.df <- generateHGVSG(vcf = vcf.df, ref = ref.df)
vcf.df <- processClinGen(vcf.df, ref = ref, progressBar = F)
vcf.df <- addConcepts(vcf.df, concepts, returnAll = T)

##### Run - Multiple VCFs #####

#Load the VCF directory
vcf <- loadVCF(userVCF = "SomeDirectory/")

#Set ref to hg19
ref <- "hg19"

concepts.df <- multiVCFPipeline(vcf, ref, concepts)




#install.packages("BiocManager")
#BiocManager::install("GenomeInfoDb")


#install.packages("devtools")
#devtools::install_github("odyOSG/KOIOS")


print ("Load Libraries ")

library(GenomeInfoDb)
library(KOIOS)

print ("set working dir ")

setwd("/mnt/oscar-dream/data")


##### Input #####


print ("[Start] : Load the OMOP Genomic Concept library ")

#Load the OMOP Genomic Concept library
concepts <- loadConcepts()

print ("[Start] : Set the reference genome ")

#Set the reference genome to "auto"
ref <- "hg38"

print ("[End] : Set the reference genome ")

print ("[End] : Load the OMOP Genomic Concept library ")

print ("[Start] : Load the VCF file ")

#Load the VCF file
vcf <- loadVCF(userVCF = "")

print ("[End] : Load the VCF file ")

print ("[Start] : Load Reference ")

ref.df <- loadReference(ref)

print ("[End] : Load Reference ")

print ("[Start] : Process VCF ")

vcf.df <- processVCF(vcf)

print ("[End] : Process VCF ")

print ("[Start] : generate HGVSG ")
#Process VCF and generate all relevant HGVSG identifiers for input records
vcf.df <- generateHGVSG(vcf = vcf.df, ref = ref.df)

print ("[End] : generate HGVSG ")

print ("[Start] : process ClinGen ")

vcf.df <- processClinGen(vcf.df, ref = ref, progressBar = F)

print ("[End] : process ClinGe ")

print ("[Start] : add Concepts ")
#Combine this output data with the OMOP Genomic vocab to produce a DF containing a list of concept codes
vcf.df <- addConcepts(vcf.df, concepts, returnAll = T)

print ("[End] : add Concepts ")

print(vcf.df)

save(vcf.df,file="data.Rda")


