# Multi-revision ncov-ingest output

This workflow creates open ncov-ingest outputs allowing multiple versions of a sequence to be present.

The workflow downloads the latest ingest outputs and outputs from January 2023. Sequences/metadata from the January 2023 files is added to the latest outputs iff the sequence revision differs between January 2023 and latest.
