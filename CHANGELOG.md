# Change Log

## [Unreleased]

The main feature of this release is the new support for custom
gauge adapters. This allows the use of a Python file from the
ReBench config, which can parse arbitrary output from a benchmark, see #209.

Furthermore, ReBench dropped support for Python 2. If you require ReBench to
run with Python 2, please see #208 for the removed supported code, or use
version 1.1.0, which was the last version with Python 2 support.


Other new features:
 - add command-line option `-D` to disable the use of denoise (#217)

Other changes:
 - fix handling of environment variables when sudo is used (#210)
 - try `gtime` from MacPorts as alternative `time` command on macOS (#212)
 - update py-cpuinfo to work on macOS with ARM-base CPUs (#212)
 - make error more readable when executor is not available (#213)

## [1.1.0] Denoise - 2023-02-21

This release focuses on reducing the noise from the system  (#143, #144).
For this purpose, it introduces the `rebench-denoise` tool, which will adapt
system parameters to:

- change CPU governor to the performance setting
- disables turbo boost
- reduces the sampling frequency allowed by the kernel
- execute benchmarks with CPU shielding and `nice -n-20`

`rebench-denoise` can also be used as stand-alone tool, is documented here:
https://rebench.readthedocs.io/en/latest/denoise/

The use of `rebench-denoise` will require root rights.

Other new features include:

 - add support for configuring environment variables (#174)
 - add support for recording profiling information (#190)
 - add support for printing the execution plan without running it (#171)
 - add marker in configuration to make setting important, which overrides
   previous settings, giving more flexibility in composing
   configuration values (#170)
 - add support for filtering experiments by machines (#161)

Thanks to @tobega, @qinsoon, @cmccandless, @OctaveLarose, and @raehik for their contributions.

Other notable improvements:

 - `-R` now disables data reporting, replacing the previous `-S` (#145)
 - added support to report experiment completion to ReBenchDB (#149)
 - fixed JMH support (#147)
 - fixed string/byte encoding issues between Python 2 and 3 (#142)
 - updated py-cpuinfo (#137, #138, #141)
 - allow the use of float values in the ReBenchLogAdapter parser (#201)
 - make gauge adapter names in configurations case-insensitive (#202)
 - improve documentation (#197, #198)
 - use PyTest for unit tests (#192)
 
**Full Changelog**: https://github.com/smarr/ReBench/compare/v1.0.1...v1.1.0
 

## [1.0.1] - 2020-06-23

This is a bug fix release.

 - adopt py-cpuinfo 6.0.0 and pin version to avoid issues with changing APIs (#138)
   Thanks to @tobega for the fix!

## [1.0.0] Foundations - 2020-05-02

This is the first official release of ReBench as a "feature-complete" product.
Feature-complete here means, it is a tried and tested tool for benchmark
execution. It is highly 
[configurable](https://rebench.readthedocs.io/en/latest/config/),
[documented](https://rebench.readthedocs.io/en/latest/),
and [successfully used](https://github.com/smarr/ReBench#use-in-academia).

This 1.0 release does not signify any new major features, but instead marks a
point where ReBench has been stable and relieable for a long time.

ReBench is designed to

 - enable reproduction of experiments;
 - document all benchmark parameters;
 - provide a flexible execution model,
   with support for interrupting and continuing benchmarking;
 - enable the definition of complex sets of comparisons
   and their flexible execution;
 - report results to continuous performance monitoring systems,
   e.g., Codespeed or ReBenchDB;
 - provide basic support for building/compiling benchmarks/experiments
   on demand;
 - be extensible to parse output of custom benchmark harnesses.

ReBench isn't

 - a framework for microbenchmarks.
   Instead, it relies on existing harnesses and can be extended to parse their
   output.
 - a performance analysis tool. It is meant to execute experiments and
   record the corresponding measurements.
 - a data analysis tool. It provides only a bare minimum of statistics,
   but has an easily parseable data format that can be processed, e.g., with R.

To use ReBench, install it with Python's pip:

```bash
pip install rebench
```

### Acknowledgements

ReBench has been used by a number of people over the years, and their feedback
and [contributions](https://github.com/smarr/ReBench/graphs/contributors)
made it what it is today. Not all of these contributions are recorded,
but I'd still like to thank everyone, from the annoymous reviewer of artifacts,
to the students who had to wade through bugs and missing documentation.
Thank you!

### Changes Since 1.0rc2

 - moved CI to use GitHub Actions (#134)
 - added testing of Python 3.7 (#121) and ruamel.yaml (#123)
 - ensure config is YAML 1.2 compliant (#123)
 - added support for ReBenchDB (#129, #130)
 
 - fixed issues with error reporting (#128)
 - fixed handling of input size configuration (#117)

## [1.0rc2] - 2019-06-09

 - added `--setup-only` option, to run one benchmark for each setup (#110, #115)
 - added `ignore_timeout` setting to accept known timeouts without error (#118)
 - added `retries_after_failure` setting (#107, #108)
 
 - fixed data loading, which ignored warmup setting (#111, #116)
 - fixed how settings are inherited for follow documentation (#112, #113)
 - fixed message for consecutive failures (#109)
 - fixed some reporting issues (#106)

## [1.0rc1] - 2018-08-02

 - made user interface more consistent and concise (#83, #85, #92, #101, #102)
 - added concept of iterations/invocations (#82, #87)
 - added executor and suite name as command variables (#95, #101)
 - added and improved support for building suites before execution (#59, #78, #84, #96)
 - revised configuration format to me more consistent and add schema (#74, #82, #66, #94, #101)
 - fixed memory usage, avoid running out of memory for large experiments (#103)
 - added support to verify parameter and config file (#104)
 - added [documentation][docs] (#66, #101)
 - use PyLint (#79)

## [0.10.1] - 2018-06-08

 - fixed experiment filters and reporting on codespeed submission errors (#77)

## [0.10.0] - 2018-06-08

 - restructured command-line options in help, and use argparse (#73)
 - added support for Python 3 and PyPy (#65)
 - added support for extra criteria (things beside run time) (#64)
 - added support for path names in ReBenchLog benchmark names

## [0.9.1] - 2017-12-21

 - fixed time-left reporting of invalid times (#60)
 - take the number of data points per run into account for estimated time left (#62)
 - obtain process output on timeout to enable results of partial runs
 - fixed incompatibility with latest setuptools

## [0.9.0] - 2017-04-23

 - added support for building VMs before execution (#58)
 - added support for using binaries on system's path, `path` does not need
   to be provided for VM anymore (#57)

## [0.8.0] - 2016-06-25

 - added support for rerun experiments, see `-r` option (#50)
   This option will drop existing data for the selected experiment from
   the data file, and then execute them normally.
 - added support for filtering VM's and suites/benchmarks on CLI (#50)
 - directly output a programs stdout/stderr in verbose mode `-v` (#52)

 - fixed CLI reporting showing multiple summaries (#30)
 - fixed problem with quick termination (#51)

 - removed reporting to IRC, was never made to work properly
 - removed support for displaying confidence interval
   proper statistical evaluation needs to be done externally to ReBench
 - removed old support for Caliper output

## [0.7.5] - 2016-06-11

 - indicate failed runs as return code (#49)
 - added keep-alive message every 10min
 - changed debug output to show only last 20 data points
 - fixed `setup.py install`, remove non-existing package
 - started change log

## Untracked Releases
 - [0.7.4] - 2016-05-20
 - [0.7.3] - 2016-03-21
 - [0.7.2] - 2015-02-11
 - [0.7.1] - 2014-02-05
 - [0.6.0] - 2014-05-19
 - [0.5.0] - 2014-03-25

[Unreleased]: https://github.com/smarr/ReBench/compare/v1.1.0...HEAD
[1.1.0]:  https://github.com/smarr/ReBench/compare/v1.0.1...v1.1.0
[1.0.1]:  https://github.com/smarr/ReBench/compare/v1.0.0...v1.0.1
[1.0.0]:  https://github.com/smarr/ReBench/compare/v1.0rc2...v1.0.0
[1.0rc2]: https://github.com/smarr/ReBench/compare/v1.0rc1...v1.0rc2
[1.0rc1]: https://github.com/smarr/ReBench/compare/v0.10.1...v1.0rc1
[0.10.1]: https://github.com/smarr/ReBench/compare/v0.10.0...v0.10.1
[0.10.0]: https://github.com/smarr/ReBench/compare/v0.9.1...v0.10.0
[0.9.1]: https://github.com/smarr/ReBench/compare/v0.9.0...v0.9.1
[0.9.0]: https://github.com/smarr/ReBench/compare/v0.8.0...v0.9.0
[0.8.0]: https://github.com/smarr/ReBench/compare/v0.7.5...v0.8.0
[0.7.5]: https://github.com/smarr/ReBench/compare/v0.7.4...v0.7.5
[0.7.4]: https://github.com/smarr/ReBench/compare/v0.7.3...v0.7.4
[0.7.3]: https://github.com/smarr/ReBench/compare/v0.7.2...v0.7.3
[0.7.2]: https://github.com/smarr/ReBench/compare/v0.7.1...v0.7.2
[0.7.1]: https://github.com/smarr/ReBench/compare/v0.6.0...v0.7.1
[0.6.0]: https://github.com/smarr/ReBench/compare/v0.5.0...v0.6.0
[0.5.0]: https://github.com/smarr/ReBench/compare/05dfc4b...v0.5.0
[docs]: http://rebench.readthedocs.io/
