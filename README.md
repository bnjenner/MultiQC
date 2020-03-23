# ![MultiQC](https://raw.githubusercontent.com/ewels/MultiQC/master/docs/images/MultiQC_logo.png)


### Aggregate bioinformatics results across many samples into a single report.

##### Find [documentation](http://multiqc.info/docs) and [example reports](http://multiqc.info/examples/rna-seq/multiqc_report.html) at [http://multiqc.info](http://multiqc.info)

[![PyPI Version](https://img.shields.io/pypi/v/multiqc.svg?style=flat-square)](https://pypi.python.org/pypi/multiqc/)
[![Conda Version](https://anaconda.org/bioconda/multiqc/badges/version.svg)](https://anaconda.org/bioconda/multiqc)
[![Docker](https://img.shields.io/docker/automated/ewels/multiqc.svg?style=flat-square)](https://hub.docker.com/r/ewels/multiqc/)
[![GitHub Workflow Status - Linux](https://img.shields.io/github/workflow/status/ewels/MultiQC/MultiQC%20-%20Linux?label=build%20-%20Linux&logo=ubuntu&logoColor=white&style=flat-square)](https://github.com/ewels/MultiQC/actions?query=workflow%3A%22MultiQC+-+Linux%22)
[![GitHub Workflow Status - Windows](https://img.shields.io/github/workflow/status/ewels/MultiQC/MultiQC%20-%20Windows?label=build%20-%20Windows&logo=windows&style=flat-square)](https://github.com/ewels/MultiQC/actions?query=workflow%3A%22MultiQC+-+Windows%22)

[![Gitter](https://img.shields.io/badge/gitter-%20join%20chat%20%E2%86%92-4fb99a.svg?style=flat-square)](https://gitter.im/ewels/MultiQC)
[![DOI](https://img.shields.io/badge/DOI-10.1093%2Fbioinformatics%2Fbtw354-lightgrey.svg?style=flat-square)](http://dx.doi.org/10.1093/bioinformatics/btw354)

-----

MultiQC is a tool to create a single report with interactive plots
for multiple bioinformatics analyses across many samples.

MultiQC is written in Python (tested with v2.7, 3.4, 3.5 and 3.6). It is
available on the [Python Package Index](https://pypi.python.org/pypi/multiqc/)
and through conda using [Bioconda](http://bioconda.github.io/).

Reports are generated by scanning given directories for recognised log files.
These are parsed and a single HTML report is generated summarising the statistics
for all logs found. MultiQC reports can describe multiple analysis steps and
large numbers of samples within a single plot, and multiple analysis tools making
it ideal for routine fast quality control.

Currently, supported tools include:


|Read QC & pre-processing         | Aligners / quantifiers  | Post-alignment processing   | Post-alignment QC                    |
|---------------------------------|-------------------------|-----------------------------|--------------------------------------|
|[Adapter Removal][adapterremoval]|[BBMap][bbmap]           |[Bamtools][bamtools]         |[biobambam2][biobambam2]              |
|[AfterQC][afterqc]               |[BISCUIT][biscuit]       |[Bcftools][bcftools]         |[BUSCO][busco]                        |
|[Bcl2fastq][bcl2fastq]           |[Bismark][bismark]       |[GATK][gatk]                 |[Conpair][conpair]                    |
|[BBTools][bbmap]                 |[Bowtie][bowtie-1]       |[HOMER][homer]               |[DamageProfiler][damageprofiler]      |
|[BioBloom Tools][biobloomtools]  |[Bowtie 2][bowtie-2]     |[HTSeq][htseq]               |[DeDup][dedup]                        |
|[ClipAndMerge][clipandmerge]     |[HiCUP][hicup]           |[MACS2][macs2]               |[deepTools][deeptools]                |
|[Cluster Flow][clusterflow]      |[HiC-Pro][hicpro]        |[Picard][picard]             |[Disambiguate][disambiguate]          |
|[Cutadapt][cutadapt]             |[HISAT2][hisat2]         |[Prokka][prokka]             |[goleft][goleft]                      |
|[leeHom][leehom]                 |[Kallisto][kallisto]     |[RSEM][rsem]                 |[HiCExplorer][hicexplorer]            |
|[InterOp][interop]               |[Long Ranger][longranger]|[Samblaster][samblaster]     |[methylQA][methylqa]                  |
|[FastQC][fastqc]                 |[Salmon][salmon]         |[Samtools][samtools]         |[miRTrace][mirtrace]                  |
|[FastQ Screen][fastq-screen]     |[Slamdunk][slamdunk]     |[SnpEff][snpeff]             |[mosdepth][mosdepth]                  |
|[Fastp][fastp]                   |[STAR][star]             |[Subread featureCounts][featurecounts]|[Peddy][peddy]               |
|[fgbio][fgbio]                   |[Tophat][tophat]         |[Stacks][stacks]             |[phantompeakqualtools][phantompeakqualtools]|
|[FLASh][flash]                   |                         |[THetA2][theta2]             |[Preseq][preseq]                      |
|[Flexbar][flexbar]               |                         |                             |[QoRTs][qorts]                        |
|[Jellyfish][jellyfish]           |                         |                             |[Qualimap][qualimap]                  |
|[KAT][kat]                       |                         |                             |[QUAST][quast]                        |
|[MinIONQC][minionqc]             |                         |                             |[RNA-SeQC][rna_seqc]                  |
|[Skewer][skewer]                 |                         |                             |[RSeQC][rseqc]                        |
|[SortMeRNA][sortmerna]           |                         |                             |[Sargasso][sargasso]                  |
|[SeqyClean][seqyclean]           |                         |                             |[Sex.DetERRmine][sexdeterrmine]       |
|[HTStream][htstream]             |                         |                             |[Supernova][supernova]                |
|                                 |                         |                             |[VCFTools][vcftools]                  |
|                                 |                         |                             |[VerifyBAMID][verifybamid]            |


MultiQC can also easily parse data from custom scripts, if correctly formatted / configured.
See the [MultiQC documentation](http://multiqc.info/docs/#custom-content) for more information.

Please note that some modules only recognise output from certain tool subcommands. Please follow the
links in the above table to the [module documentation](http://multiqc.info/docs/#multiqc-modules)
for more information.

More modules are being written all of the time. Please suggest any ideas as a new
[issue](https://github.com/ewels/MultiQC/issues) _(include an example log file if possible)_.

## Installation

You can install MultiQC from [PyPI](https://pypi.python.org/pypi/multiqc/)
using `pip` as follows:
```bash
pip install multiqc
```

Alternatively, you can install using [Conda](http://anaconda.org/)
from the [bioconda channel](https://bioconda.github.io/):
```bash
conda install -c bioconda multiqc
```

If you would like the development version instead, the command is:
```bash
pip install --upgrade --force-reinstall git+https://github.com/ewels/MultiQC.git
```

MultiQC is also available in the
[Galaxy Toolshed](https://toolshed.g2.bx.psu.edu/view/engineson/multiqc/).

## Usage
Once installed, you can use MultiQC by navigating to your analysis directory
(or a parent directory) and running the tool:
```bash
multiqc .
```

That's it! MultiQC will scan the specified directory (`.` is the current dir)
and produce a report detailing whatever it finds.

The report is created in `multiqc_report.html` by default. Tab-delimited data
files are also created in `multiqc_data/`, containing extra information.
These can be easily inspected using Excel (use `--data-format` to get `yaml`
or `json` instead).

For more detailed instructions, run `multiqc -h` or see the
[documentation](http://multiqc.info/docs/#running-multiqc).

## Citation
Please consider citing MultiQC if you use it in your analysis.

> **MultiQC: Summarize analysis results for multiple tools and samples in a single report** <br/>
> _Philip Ewels, Måns Magnusson, Sverker Lundin and Max Käller_ <br/>
> Bioinformatics (2016) <br/>
> doi: [10.1093/bioinformatics/btw354](http://dx.doi.org/10.1093/bioinformatics/btw354) <br/>
> PMID: [27312411](http://www.ncbi.nlm.nih.gov/pubmed/27312411)

```TeX
@article{doi:10.1093/bioinformatics/btw354,
author = {Ewels, Philip and Magnusson, Måns and Lundin, Sverker and Käller, Max},
title = {MultiQC: summarize analysis results for multiple tools and samples in a single report},
journal = {Bioinformatics},
volume = {32},
number = {19},
pages = {3047},
year = {2016},
doi = {10.1093/bioinformatics/btw354},
URL = { + http://dx.doi.org/10.1093/bioinformatics/btw354},
eprint = {/oup/backfile/Content_public/Journal/bioinformatics/32/19/10.1093_bioinformatics_btw354/3/btw354.pdf}
}
```

## Contributions & Support

Contributions and suggestions for new features are welcome, as are bug reports!
Please create a new [issue](https://github.com/ewels/MultiQC/issues) for any
of these, including example reports where possible. MultiQC has extensive
[documentation](http://multiqc.info/docs) describing how to write new modules,
plugins and templates.

There is a chat room for the package hosted on Gitter where you can discuss
things with the package author and other developers:
https://gitter.im/ewels/MultiQC

If in doubt, feel free to get in touch with the author directly:
[@ewels](https://github.com/ewels) (phil.ewels@scilifelab.se)

### Contributors
Project lead and main author: [@ewels](https://github.com/ewels)

Code contributions from:
[@ahvigil](https://github.com/ahvigil),
[@aledj2](https://github.com/aledj2),
[@apeltzer](https://github.com/apeltzer),
[@avilella](https://github.com/avilella),
[@boulund](https://github.com/boulund),
[@bschiffthaler](https://github.com/bschiffthaler),
[@chuan-wang](https://github.com/chuan-wang),
[@cpavanrun](https://github.com/cpavanrun),
[@dakl](https://github.com/dakl),
[@elizabethcook21](https://github.com/elizabethcook21),
[@ehsueh](https://github.com/ehsueh),
[@epruesse](https://github.com/epruesse),
[@florianduclot](https://github.com/florianduclot/),
[@guillermo-carrasco](https://github.com/guillermo-carrasco),
[@HLWiencko](https://github.com/HLWiencko),
[@iimog](https://github.com/iimog),
[@joachimwolff](https://github.com/joachimwolff),
[@jrderuiter](https://github.com/jrderuiter),
[@lpantano](https://github.com/lpantano),
[@matthdsm](https://github.com/matthdsm),
[@MaxUlysse](https://github.com/MaxUlysse),
[@mlusignan](https://github.com/mlusignan),
[@moonso](https://github.com/moonso),
[@noirot](https://github.com/noirot),
[@remiolsen](https://github.com/remiolsen),
[@rdali](https://github.com/rdali),
[@rlegendre](https://github.com/rlegendre),
[@robinandeer](https://github.com/robinandeer),
[@Rotholandus](https://github.com/Rotholandus),
[@sachalau](https://github.com/sachalau/),
[@smeds](https://github.com/smeds/),
[@t-neumann](https://github.com/t-neumann),
[@vladsaveliev](https://github.com/vladsaveliev),
[@winni2k](https://github.com/winni2k),
[@wkretzsch](https://github.com/wkretzsch),
[@nservant](https://github.com/nservant),

and many others. Thanks for your support!

MultiQC is released under the GPL v3 or later licence.

[adapterremoval]: http://multiqc.info/docs/#adapter-removal
[afterqc]:        http://multiqc.info/docs/#afterqc
[bamtools]:       http://multiqc.info/docs/#bamtools
[bbmap]:          http://multiqc.info/docs/#bbmap
[bcftools]:       http://multiqc.info/docs/#bcftools
[bcl2fastq]:      http://multiqc.info/docs/#bcl2fastq
[biobambam2]:     http://multiqc.info/docs/#biobambam2
[biobloomtools]:  http://multiqc.info/docs/#biobloom-tools
[biscuit]:        http://multiqc.info/docs/#biscuit
[bismark]:        http://multiqc.info/docs/#bismark
[bowtie-1]:       http://multiqc.info/docs/#bowtie-1
[bowtie-2]:       http://multiqc.info/docs/#bowtie-2
[busco]:          http://multiqc.info/docs/#busco
[clipandmerge]:   http://multiqc.info/docs/#clipandmerge
[clusterflow]:    http://multiqc.info/docs/#cluster-flow
[conpair]:        http://multiqc.info/docs/#conpair
[cutadapt]:       http://multiqc.info/docs/#cutadapt
[damageprofiler]: http://multiqc.info/docs/#damageprofiler
[dedup]:          http://multiqc.info/docs/#dedup
[deeptools]:      http://multiqc.info/docs/#deeptools
[disambiguate]:   http://multiqc.info/docs/#disambiguate
[fastq-screen]:   http://multiqc.info/docs/#fastq-screen
[fastqc]:         http://multiqc.info/docs/#fastqc
[fastp]:          http://multiqc.info/docs/#fastp
[featurecounts]:  http://multiqc.info/docs/#featurecounts
[fgbio]:          http://multiqc.info/docs/#fgbio
[flash]:          http://multiqc.info/docs/#flash
[flexbar]:        http://multiqc.info/docs/#flexbar
[gatk]:           http://multiqc.info/docs/#gatk
[goleft]:         http://multiqc.info/docs/#goleft-indexcov
[hicexplorer]:    http://multiqc.info/docs/#hicexplorer
[hicup]:          http://multiqc.info/docs/#hicup
[hicpro]:         http://multiqc.info/docs/#hic-pro
[hisat2]:         http://multiqc.info/docs/#hisat2
[homer]:          http://multiqc.info/docs/#homer
[htseq]:          http://multiqc.info/docs/#htseq
[htstream]:       http://multiqc.info/docs/#htstream
[interop]:        http://multiqc.info/docs/#interop
[jellyfish]:      http://multiqc.info/docs/#jellyfish
[kallisto]:       http://multiqc.info/docs/#kallisto
[kat]:            http://multiqc.info/docs/#kat
[leehom]:         http://multiqc.info/docs/#leehom
[longranger]:     http://multiqc.info/docs/#longranger
[macs2]:          http://multiqc.info/docs/#macs2
[methylqa]:       http://multiqc.info/docs/#methylqa
[minionqc]:       http://multiqc.info/docs/#minionqc
[mirtrace]:       http://multiqc.info/docs/#mirtrace
[mosdepth]:       http://multiqc.info/docs/#mosdepth
[peddy]:          http://multiqc.info/docs/#peddy
[phantompeakqualtools]: http://multiqc.info/docs/#phantompeakqualtools
[picard]:         http://multiqc.info/docs/#picard
[preseq]:         http://multiqc.info/docs/#preseq
[prokka]:         http://multiqc.info/docs/#prokka
[qorts]:          http://multiqc.info/docs/#qorts
[qualimap]:       http://multiqc.info/docs/#qualimap
[quast]:          http://multiqc.info/docs/#quast
[rna_seqc]:       http://multiqc.info/docs/#rna_seqc
[rsem]:           http://multiqc.info/docs/#rsem
[rseqc]:          http://multiqc.info/docs/#rseqc
[salmon]:         http://multiqc.info/docs/#salmon
[samblaster]:     http://multiqc.info/docs/#samblaster
[samtools]:       http://multiqc.info/docs/#samtools
[sargasso]:       http://multiqc.info/docs/#sargasso
[seqyclean]:      http://multiqc.info/docs/#seqyclean
[sexdeterrmine]:  http://multiqc.info/docs/#sex.deterrmine
[skewer]:         http://multiqc.info/docs/#skewer
[slamdunk]:       http://multiqc.info/docs/#slamdunk
[snpeff]:         http://multiqc.info/docs/#snpeff
[sortmerna]:      http://multiqc.info/docs/#sortmerna
[stacks]:         http://multiqc.info/docs/#stacks
[star]:           http://multiqc.info/docs/#star
[supernova]:      http://multiqc.info/docs/#supernova
[theta2]:         http://multiqc.info/docs/#theta2
[tophat]:         http://multiqc.info/docs/#tophat
[trimmomatic]:    http://multiqc.info/docs/#trimmomatic
[vcftools]:       http://multiqc.info/docs/#vcftools
[verifyBAMID]:    http://multiqc.info/docs/#verifybamid
