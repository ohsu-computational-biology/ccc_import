# CCC Import Tool

This a command line client for CCC.  The overall idea is to provide a lightweight
utility to facilitate import/registration of data with the CCC.  This could be run interactively,
scripted or as part of a workflow.

Usage:

    ccc_import publish_batch --token=<TOKEN> --tsv=<TSV> --siteId=<SITE_ID> --user=<USER> --projectName=<PROJECT_NAME> --domain=<DOMAIN>
    
    ccc_import publish_resource --token=<TOKEN> --filePath=<FILE> --siteId=<SITE_ID> --user=<USER> --projectName=<PROJECT_NAME> --workflowId=<WORKFLOW_ID> --fileType=<FILE_TYPE> [--inheritFrom=<CCC_DID>] --property <ATTR>...
    
    ccc_import (-h | --help)
    
    ccc_import --version

The import tool will handle basic validation of incoming data, and with support for field aliases, data type conversion, and will
automatically de-normalize fields (i.e. apply all attributes of that patient to the sample, attributes of the sample to the resource, etc.  It will automatically register a resource with DTS if you provide a filePath, but do not provide the CCC DID.

How To Install:

Until a release on PyPi, you can install this tool with:

    pip install git+git://github.com/ohsu-computational-biology/ccc_import
