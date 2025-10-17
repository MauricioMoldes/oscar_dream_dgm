import psycopg2

def insert_care_site(care_site_id, care_site_name, place_of_service, location_id, conn):
    """
    Inserts a record into the CARE_SITE table.

    :param care_site_id: Unique ID for the care site
    :param care_site_name: Name of the care site
    :param place_of_service: Description of the service
    :param location_id: Location ID
    :param conn: Active database connection
    """
    query = """
    INSERT INTO CARE_SITE (care_site_id, care_site_name, place_of_service, location_id)  
    VALUES (%s, %s, %s, %s);
    """
    try:
        with conn.cursor() as cur:
            cur.execute(query, (care_site_id, care_site_name, place_of_service, location_id))
            conn.commit()
            print("Care Site inserted successfully.")
    except Exception as e:
        conn.rollback()
        print("Error inserting record:", e)

def insert_person(person_id, gender, birth_year, race, care_site_id, conn):
    """
    Inserts a record into the into the PERSON table.
    
    :param person_id: Unique ID for the person
    :param gender: Gender of the person
    :param birth_year: Birth year of the person
    :param race: Race of the person
    :param care_site_id: Associated care site ID
    :param conn: Active PostgreSQL database connection
    """
    query = """
    INSERT INTO PERSON (person_id, gender, birth_year, race, care_site_id) VALUES (%s, %s, %s, %s, %s);
    """

    try:
        with conn.cursor() as cur:
            cur.execute(query, (person_id, gender, birth_year, race, care_site_id))            
            conn.commit()
            print("Person inserted successfully")
    except Exception as e:
        conn.rollback()
        print("Error inserting person:", e)



def insert_specimen(person_id, procedure_occurrence_id, specimen_concept_id, specimen_date, anatomic_site, disease_status, conn):
    """
    Calls the PL/pgSQL function to insert a specimen into the SPECIMEN table.

    :param specimen_id: Unique ID for the specimen
    :param person_id: ID of the person associated with the specimen
    :param procedure_occurrence_id: ID of the procedure occurrence
    :param specimen_concept_id: Concept ID for the specimen
    :param specimen_date: Date of specimen collection
    :param anatomic_site: Anatomic site ID
    :param disease_status: Disease status ID
    :param conn: Active PostgreSQL database connection
    """
    query = "INSERT INTO SPECIMEN (person_id, procedure_occurrence_id, specimen_concept_id, specimen_date, anatomic_site, disease_status) VALUES(%s, %s, %s, %s, %s, %s);"
    
    try:
        with conn.cursor() as cur:
            cur.execute(query, (person_id, procedure_occurrence_id, specimen_concept_id, specimen_date, anatomic_site, disease_status))           
            conn.commit()
            print("Specimen inserted successfully")
    except Exception as e:
        conn.rollback()
        print("Error inserting specimen:", e)

def insert_genomic_test(genomic_test_id, care_site_id, genomic_test_name, genomic_test_version, 
                        reference_genome, sequencing_device, target_capture, read_type, read_length, 
                        alignment_tools, variant_calling_tools, chromosome_coordinate, annotation_tools, 
                        annotation_databases, conn):
    """
    Inserts a genomic test into the GENOMIC_TEST table.
    """
    query = """
    INSERT INTO GENOMIC_TEST (
        genomic_test_id, care_site_id, genomic_test_name, genomic_test_version, reference_genome, 
        sequencing_device, target_capture, read_type, read_length, alignment_tools, 
        variant_calling_tools, chromosome_coordinate, annotation_tools, annotation_databases
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
    """
    
    try:
        with conn.cursor() as cur:
            cur.execute(query, (genomic_test_id, care_site_id, genomic_test_name, genomic_test_version, 
                                reference_genome, sequencing_device, target_capture, read_type, read_length, 
                                alignment_tools, variant_calling_tools, chromosome_coordinate, 
                                annotation_tools, annotation_databases))
            conn.commit()
            print("Genomic test inserted successfully")
    except Exception as e:
        conn.rollback()
        print("Error inserting genomic test:", e)


def insert_target_gene(target_gene_id, genomic_test_id, hgnc_id, chromosome, start_position, end_position, conn):
    """
    Inserts a target gene into the TARGET_GENE table.
    """
    query = """
    INSERT INTO TARGET_GENE (
        target_gene_id, genomic_test_id, hgnc_id, chromosome, start_position, end_position
    ) VALUES (%s, %s, %s, %s, %s, %s);
    """
    
    try:
        with conn.cursor() as cur:
            cur.execute(query, (target_gene_id, genomic_test_id, hgnc_id, chromosome, start_position, end_position))
            conn.commit()
            print("Target gene inserted successfully")
    except Exception as e:
        conn.rollback()
        print("Error inserting target gene:", e)

def insert_variant_occurrence( variant_occurrence_id, procedure_occurrence_id, specimen_id, reference_specimen_id, target_gene_id, reference_sequence, rs_id, hgvs_c, hgvs_p, variant_read_depth , total_read_depth, variant_exon_number, sequence_alteration,variant_feature, conn):
    """
    Inserts a variant occurrence into the VARIANT_OCCURRENCE table.
    """
    query = """
    INSERT INTO VARIANT_OCCURRENCE (
        variant_occurrence_id, procedure_occurrence_id, specimen_id, reference_specimen_id, target_gene_id, reference_sequence, rs_id, hgvs_c, hgvs_p, variant_read_depth , total_read_depth, variant_exon_number, sequence_alteration,variant_feature
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
    """
    
    try:
        with conn.cursor() as cur:
            cur.execute(query, (variant_occurrence_id, procedure_occurrence_id, specimen_id, reference_specimen_id, target_gene_id, reference_sequence, rs_id, hgvs_c, hgvs_p, variant_read_depth , total_read_depth, variant_exon_number, sequence_alteration,variant_feature, ))
            conn.commit()
            print("Variant occurrence inserted successfully")
    except Exception as e:
        conn.rollback()
        print("Error inserting variant occurrence:", e)

def insert_variant_annotation(variant_annotation_id, variant_occurrence_id, annotation_database, 
                              variant_origin, variant_pathogenicity, variant_class_level, allele_frequency, 
                              medication, clinical_trial_information, conn):
    """
    Inserts a variant annotation into the VARIANT_ANNOTATION table.
    """
    query = """
    INSERT INTO VARIANT_ANNOTATION (
        variant_annotation_id, variant_occurrence_id, annotation_database, variant_origin, 
        variant_pathogenicity, variant_class_level, allele_frequency, medication, clinical_trial_information
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
    """
    
    try:
        with conn.cursor() as cur:
            cur.execute(query, (variant_annotation_id, variant_occurrence_id, annotation_database, 
                                variant_origin, variant_pathogenicity, variant_class_level, allele_frequency, 
                                medication, clinical_trial_information))
            conn.commit()
            print("Variant annotation inserted successfully")
    except Exception as e:
        conn.rollback()
        print("Error inserting variant annotation:", e)

def insert_condition_occurrence(condition_occurrence_id, person_id, condition_concept_id, condition_start_date, 
                                condition_end_date, condition_type_concept_id, stop_reason, conn):
    """
    Inserts a condition occurrence into the CONDITION_OCCURRENCE table.
    """
    query = """
    INSERT INTO CONDITION_OCCURRENCE (
        condition_occurrence_id, person_id, condition_concept_id, condition_start_date, 
        condition_end_date, condition_type_concept_id, stop_reason
    ) VALUES (%s, %s, %s, %s, %s, %s, %s);
    """
    
    try:
        with conn.cursor() as cur:
            cur.execute(query, (condition_occurrence_id, person_id, condition_concept_id, 
                                condition_start_date, condition_end_date, condition_type_concept_id, 
                                stop_reason))
            conn.commit()
            print("Condition occurrence inserted successfully")
    except Exception as e:
        conn.rollback()
        print("Error inserting condition occurrence:", e)

def insert_procedure_occurrence( person_id, procedure_concept_id, procedure_date, 
                                procedure_type_concept_id, conn):
    """
    Inserts a procedure occurrence into the PROCEDURE_OCCURRENCE table.
    """
    query = """
    INSERT INTO PROCEDURE_OCCURRENCE (
         person_id, procedure_concept_id, procedure_date, 
        procedure_type_concept_id
    ) VALUES (%s, %s, %s, %s)
    RETURNING procedure_occurrence_id;
    """
    
    try:
        with conn.cursor() as cur:
            cur.execute(query, ( person_id, procedure_concept_id, 
                                procedure_date, procedure_type_concept_id))
            procedure_occurrence_id = cur.fetchone()[0]
            conn.commit()
            print("Procedure occurrence inserted successfully with ID:", procedure_occurrence_id)
            return procedure_occurrence_id            
    except Exception as e:
        conn.rollback()
        print("Error inserting procedure occurrence:", e)



def extract_age_gender(sample_name: str):

    import re
    from datetime import datetime

    match = re.match(r"(\d{2})([a-zA-Z]+)([mf])", sample_name)
    if match:
        birth_year_prefix, _, gender = match.groups()
        birth_year = int(birth_year_prefix) + (1900 if int(birth_year_prefix) > 30 else 2000)  # Adjust for century
        #current_year = datetime.now().year
        #age = current_year - birth_year
        if gender == "f":
            gender_omop = 8532
        if gender =="m":
            gender_omop = 8507
        return birth_year, gender_omop
    return None, None

def extract_person(sample_name: str):

    age, gender_omop=extract_age_gender(sample_name)

    person_id=1 
    gender=gender_omop 
    birth_year=1998  
    race="Danish" 
    care_site_id=1
    return person_id, gender, birth_year, race, care_site_id 

def extract_date(filename: str) -> str:
    import re

    match = re.search(r'-(\d{6})-', filename)
    if match:
        date_part = match.group(1)
        formatted_date = f"20{date_part[:2]}-{date_part[2:4]}-{date_part[4:]}"
        return formatted_date
    return "No date found"


def extract_procedure_occurence(sample_name: str):
    procedure_occurrence_id=1
    person_id=1
    procedure_concept_id=1
    procedure_date='1995-08-25'
    procedure_type_concept_id=44786630
    return procedure_occurrence_id, person_id, procedure_concept_id, procedure_date, procedure_type_concept_id


def extract_specimen(sample_name: str):
    specimen_id=1
    person_id=1
    procedure_occurrence_id=1
    specimen_concept_id=1
    specimen_date='1995-08-25'
    anatomic_site=411459
    disease_status=4066212
    return specimen_id, person_id, procedure_occurrence_id, specimen_concept_id, specimen_date, anatomic_site, disease_status

# 
def extract_condition_occurence():
    condition_occurrence_id=1
    person_id=1
    condition_concept_id=4262123
    condition_start_date='1995-08-25'
    condition_end_date='1995-08-25'
    condition_type_concept_id=44786627
    stop_reason="Discharged"
    return condition_occurrence_id, person_id, condition_concept_id, condition_start_date, condition_end_date, condition_type_concept_id, stop_reason

def extract_care_site():
    care_site_id=1
    care_site_name="Rigshospitalet"
    place_of_service="Department of Genomic Medicine"
    location_id=1
    return care_site_id, care_site_name, place_of_service, location_id



def extract_genomic_test():
    """
    Techincal specification of genomic test performed in the site 
    """
    genomic_test_id=1
    care_site_id=1
    genomic_test_name="DGM_WGS"
    genomic_test_version="v5.5"
    reference_genome="GRC38"
    sequencing_device="Illumina NovaSeq6000"
    target_capture="Illumina DNA PCR-free (tagmentation) kit"
    read_type="Paired-End"
    read_length=150
    alignment_tools="BWA"
    variant_calling_tools="GATK"
    chromosome_coordinate="0-based"
    annotation_tools="Ensembl Variant Effect Predictor (V104.3)"
    annotation_databases="ensembl-io_104.1d3bb6e, ensembl-funcgen_104.f1c7762, ensembl_104.1af1dce, ensembl-variation_104.6154f8b, Cosmic_92, Clinvar_20210102, ESP_V2-SSA137, HGMD-PUBLIC_20204, assembly_GRCh38.p13, dbSNP_154, gencode_GENCODE-38,  genebuild_2014-07, gnomAD_r2.1.1, polyphen_2.2.2, sift_sift5.2.2"
    return genomic_test_id, care_site_id, genomic_test_name, genomic_test_version, reference_genome, sequencing_device, target_capture, read_type, read_length, alignment_tools, variant_calling_tools, chromosome_coordinate, annotation_tools, annotation_databases



def extract_prefix(filename: str) -> str:

    import re

    match = re.match(r"^(\w+)-", filename)
    return match.group(1) if match else None    

def get_pipeline_version(file_path: str, sample_name: str) -> str:
    with open(file_path, "r") as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) == 2 and parts[1].startswith(sample_name):
                return parts[0]  # Return pipeline version
    return None  # Return None if sample name not found

def parse_person(sample_name: str):


    birth_year, gender_omop=extract_age_gender(sample_name)
    person_id=extract_prefix(sample_name)       
    race="Danish" 
    care_site_id=1
    return person_id, gender_omop, birth_year, race, care_site_id

def extract_condition_occurence():

    condition_occurrence_id=1
    person_id=extract_prefix(sample_name)
    condition_concept_id=4262123
    condition_start_date='1995-08-25'
    condition_end_date='1995-08-25'
    condition_type_concept_id=44786627
    stop_reason="Discharged"
    return condition_occurrence_id, person_id, condition_concept_id, condition_start_date, condition_end_date, condition_type_concept_id, stop_reason




def convert_to_date(date_str):

    from datetime import datetime
    # Assuming the input is in 'YYMMDD' format
    return datetime.strptime(date_str, '%y%m%d').date()    


def get_procedure_date(sample_name: str):
   
   # Find the part of the string that contains the number (after the last dash '-')
   split_string = sample_name.split('-')

   # Extract the number from the part that contains the digits
   number = split_string[4]  # Based on the position of '240628' in the string 
   
   date = number.split('_')
   
   datefinal=date[0]

   return datefinal 

def parse_procedure_occurence(sample_name: str): 

    
    person_id=extract_prefix(sample_name)
    procedure_concept_id=46257601
    procedure_date=convert_to_date(get_procedure_date(sample_name))

    procedure_type_concept_id=44786630 #hard coded ( genomic sequence procedure )
    return person_id, procedure_concept_id, procedure_date, procedure_type_concept_id

def parse_specimen(sample_name: str):

    #SNOMED codes
    #blood = "40461907"
    #malignant="4066212" 
    #normal ="4069590"  
      
    specimen_concept_id=46274042
    specimen_date=convert_to_date(get_procedure_date(sample_name))
    anatomic_site=40461907
    disease_status=4069590
    return specimen_concept_id,specimen_date, anatomic_site, disease_status



def parse_genomic_test(sample_name: str):
    """
    Parses the genomic test data  
    """
    
    genomic_test_id=extract_prefix(sample_name)
    care_site_id=1 # hardcoded rigshospitalet 
    genomic_test_name="DGM_WGS" # hardcoded pipelinename, WGS_v1_IlluminaDNAPCRFree_X ?
     
    filepath="/mnt/oscar-dream/data/oscar_pipeline_version.txt" 
    genomic_test_version=get_pipeline_version(filepath,sample_name)    

    reference_genome="GRC38"# vcf 
    sequencing_device="Illumina NovaSeq6000"
    target_capture="Illumina DNA PCR-free (tagmentation) kit"    
    read_type="Paired-End"
    read_length=150
    alignment_tools="BWA"
    variant_calling_tools="GATK"
    chromosome_coordinate="0-based"
    annotation_tools="Ensembl Variant Effect Predictor (V104.3)"
    annotation_databases="ensembl-io_104.1d3bb6e, ensembl-funcgen_104.f1c7762, ensembl_104.1af1dce, ensembl-variation_104.6154f8b, Cosmic_92, Clinvar_20210102, ESP_V2-SSA137, HGMD-PUBLIC_20204, assembly_GRCh38.p13, dbSNP_154, gencode_GENCODE-38,  genebuild_2014-07, gnomAD_r2.1.1, polyphen_2.2.2, sift_sift5.2.2"
    
    return genomic_test_id, care_site_id, genomic_test_name, genomic_test_version, reference_genome, sequencing_device, target_capture, read_type, read_length, alignment_tools, variant_calling_tools, chromosome_coordinate, annotation_tools, annotation_databases
 

def extract_target_gene():
    """
    Gene list target in the test
    """
    target_gene_id=1
    genomic_test_id=1
    hgnc_id="EGFR"
    chromosome=7
    start_position=1199766
    end_position=1199789
    return target_gene_id, genomic_test_id, hgnc_id, chromosome, start_position, end_position


def extract_variant_occurrence():
    """
    Description of a variant occured in the gene 
    """
    variant_occurrence_id=1
    procedure_occurrence_id=1
    specimen_id=1
    reference_specimen_id=1
    target_gene_id=1
    reference_sequence="NM_020975.4"
    rs_id="rs1028345"
    hgvs_c="c.4873-53A>T"
    hgvs_p="p.Asp479Asp"
    variant_read_depth=3
    total_read_depth=89
    variant_exon_number=35
    sequence_alteration="SNP"
    variant_feature="Synonymous"
    

    return  variant_occurrence_id, procedure_occurrence_id, specimen_id, reference_specimen_id, target_gene_id, reference_sequence, rs_id, hgvs_c, hgvs_p, variant_read_depth , total_read_depth, variant_exon_number, sequence_alteration,variant_feature

def extract_variant_annotation():
    """
    Clinical Interpretation of the variant  
    """
    variant_annotation_id=1
    variant_occurrence_id=1
    annotation_database="GNOMAD"
    variant_origin="Somatic"
    variant_pathogenicity="Pathogenic"
    variant_class_level="Class 2"
    variant_tier_level="Tier 1"
    allele_frequency="0.08308" 
    medication="Gefitinib"
    clinical_trial_information="NCT00844506"

    return variant_annotation_id, variant_occurrence_id, annotation_database,variant_origin, variant_pathogenicity, variant_class_level, allele_frequency, medication, clinical_trial_information


def insert_hardcoded_oscar(sample_name):
    """
    Hardcoded example of OSCAR 
    """
  
    care_site_id, care_site_name, place_of_service, location_id = extract_care_site()
    insert_care_site(care_site_id, care_site_name, place_of_service, location_id, conn)
         
    person_id, gender, birth_year, race, care_site_id = extract_person(sample_name)
    insert_person(person_id, gender, birth_year, race, care_site_id, conn)

    condition_occurrence_id, person_id, condition_concept_id, condition_start_date, condition_end_date, condition_type_concept_id, stop_reason = extract_condition_occurence()
    insert_condition_occurrence (condition_occurrence_id, person_id, condition_concept_id, condition_start_date, condition_end_date, condition_type_concept_id, stop_reason, conn)

    procedure_occurrence_id, person_id, procedure_concept_id, procedure_date, procedure_type_concept_id = extract_procedure_occurence(sample_name) 
    insert_procedure_occurrence (procedure_occurrence_id, person_id, procedure_concept_id, procedure_date, procedure_type_concept_id, conn) 

    specimen_id, person_id, procedure_occurrence_id, specimen_concept_id, specimen_date, anatomic_site, disease_status = extract_specimen(sample_name)
    insert_specimen(specimen_id, person_id, procedure_occurrence_id, specimen_concept_id, specimen_date, anatomic_site, disease_status, conn)
     
    genomic_test_id, care_site_id, genomic_test_name, genomic_test_version, reference_genome, sequencing_device, target_capture, read_type, read_length, alignment_tools, variant_calling_tools, chromosome_coordinate, annotation_tools, annotation_databases = extract_genomic_test()
    insert_genomic_test (genomic_test_id, care_site_id, genomic_test_name, genomic_test_version, reference_genome, sequencing_device, target_capture, read_type, read_length, alignment_tools, variant_calling_tools, chromosome_coordinate, annotation_tools, annotation_databases, conn)  
    
    target_gene_id, genomic_test_id, hgnc_id, chromosome, start_position, end_position=extract_target_gene()
    insert_target_gene(target_gene_id, genomic_test_id, hgnc_id, chromosome, start_position, end_position, conn)

    variant_occurrence_id, procedure_occurrence_id, specimen_id, reference_specimen_id, target_gene_id, reference_sequence, rs_id, hgvs_c, hgvs_p, variant_read_depth , total_read_depth, variant_exon_number, sequence_alteration,variant_feature = extract_variant_occurrence()
    insert_variant_occurrence( variant_occurrence_id, procedure_occurrence_id, specimen_id, reference_specimen_id, target_gene_id, reference_sequence, rs_id, hgvs_c, hgvs_p, variant_read_depth , total_read_depth, variant_exon_number, sequence_alteration,variant_feature, conn)

    variant_annotation_id, variant_occurrence_id, annotation_database,variant_origin, variant_pathogenicity, variant_class_level, allele_frequency, medication, clinical_trial_information = extract_variant_annotation()
    insert_variant_annotation(variant_annotation_id, variant_occurrence_id, annotation_database,variant_origin, variant_pathogenicity, variant_class_level, allele_frequency, medication, clinical_trial_information,conn)



# Example usage for connecting locally, tokens have no security issue 
if __name__ == "__main__":
    conn = psycopg2.connect(
        dbname="oscar_dream_db",
        user="oscar_dream",
        password="oscar_dream",
        host="10.62.55.108",
        port="5432"
    )
     
    input_file = "/mnt/oscar_dream_dgm/data/oscar-dream-565.txt"


    care_site_id, care_site_name, place_of_service, location_id = extract_care_site()
    insert_care_site(care_site_id, care_site_name, place_of_service, location_id, conn)

# Open the file and process each line
with open(input_file, "r") as file:
    for line in file:
        line = line.strip()  # Remove leading/trailing spaces and newlines
        sample_name=line
        print(f"Processing: {sample_name}")  # Do something with the line (e.g., print)

        #insert_hardcoded_oscar(sample_name)
        person_id, gender, birth_year, race, care_site_id = parse_person(sample_name)
        insert_person(person_id, gender, birth_year, race, care_site_id, conn)

        person_id, procedure_concept_id, procedure_date, procedure_type_concept_id= parse_procedure_occurence(sample_name)
        procedure_occurrence_id = insert_procedure_occurrence( person_id, procedure_concept_id, procedure_date, procedure_type_concept_id,conn)
              
        specimen_concept_id,specimen_date, anatomic_site, disease_status= parse_specimen(sample_name)
        insert_specimen(person_id, procedure_occurrence_id, specimen_concept_id, specimen_date, anatomic_site, disease_status, conn)

    
 

    conn.close()
