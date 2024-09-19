FROM ghcr.io/cyclus/cymetric_22.04_conda/cymetric:latest AS base-image
ARG BUILDDIR=gh-preview

RUN mamba install -y sphinx sphinxcontrib-bibtex cloud_sptheme

COPY . /cyclus.github.com
WORKDIR /cyclus.github.com
RUN make gh-preview

WORKDIR /cyclus/build
RUN make cyclusdoc && \
    mkdir -p /cyclus.github.com/${BUILDDIR}/cyclus/api && \
    cp -r doc/html/* /cyclus.github.com/${BUILDDIR}/cyclus/api/

WORKDIR /cycamore/build
RUN make cycamoredoc && \
    mkdir -p /cyclus.github.com/${BUILDDIR}/cycamore/api && \
    cp -r doc/html/* /cyclus.github.com/${BUILDDIR}/cycamore/api/


FROM scratch
ARG BUILDDIR=gh-preview  
COPY --from=base-image /cyclus.github.com/${BUILDDIR} /${BUILDDIR}
