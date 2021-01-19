FROM ubuntu:latest

WORKDIR /data

# installieren mit apt-get install ncbi-blast+
RUN apt-get update && apt-get install -y\
    ncbi-blast+\
    wget\
    curl

ENV PATH /opt/conda/bin:$PATH
RUN mkdir /usr/miniconda \
    && cd /usr/miniconda \
    && wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh \
    && bash Miniconda3-latest-Linux-x86_64.sh -b -p /opt/conda \
    && cd /root/ \
    && rm -rf /usr/miniconda

RUN conda create -c conda-forge -n snakemake bioconda::snakemake bioconda::snakemake-minimal --only-dep -y\
    && conda clean --all -y
ENV PATH /opt/conda/envs/snakemake/bin:${PATH}

# RUN export PATH=$PATH:$HOME/data/ncbi-blast-2.11.0+/bin
# lieber die Daten mounten mit -v
# RUN curl --remote-name --remote-time https://ftp.ncbi.nlm.nih.gov/blast/db/FASTA/swissprot.gz

# RUN gunzip -d /data/swissprot.gz && chmod 755 swissprot && echo UNZIPPED
# # makeblastdb im container
# RUN snakemake --cores all query0.fasta_blast.out