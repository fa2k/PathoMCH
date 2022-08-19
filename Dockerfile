FROM continuumio/miniconda3
COPY environment.yml /tmp/environment.yml
RUN conda env create -f /tmp/environment.yml && rm /tmp/environment.yml
RUN echo "source activate pathomch" > ~/.bashrc
ENV PATH /opt/conda/envs/pathomch/bin:$PATH
