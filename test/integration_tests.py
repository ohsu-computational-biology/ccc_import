#!/usr/bin/env python

#for debugging
import sys, os
import unittest
import tempfile
import csv
import json
import subprocess

path = os.path.abspath(__file__)
dir_path = os.path.dirname(path)
dir_path = os.path.dirname(dir_path)
sys.path.append(dir_path)


class TestCccClient(unittest.TestCase):

    def test_resource_registration(self):
        print("testing single resource registration...")

        sampleName = 'sample1'
        self.registerSample(sampleName)

        with tempfile.NamedTemporaryFile(mode='r', delete=False) as temp:
            results = subprocess.check_output(['python', self.getScriptPath(), 'publish_resource',
                  '--token=' + self.generateAuthToken(),
                  '--filePath=' + temp.name,
                  '--siteId=' + self.getSiteId(),
                  '--user=' + self.getUser(),
                  '--projectCode=' + self.getProject(),
                  '--workflowId=workflow1',
                  '--mimeType=mimeType',
                  '--property=sample_id:' + sampleName,
                  '-m'
            ]).decode("utf-8")

            results = json.loads(results)
            self.assertEqual(results['projectCode'], self.getProject())
            self.assertEqual(results['siteId'], self.getSiteId())
            #we dont know what it will assign, but it should be a valid GUID
            self.assertIsNotNone(results['ccc_did'])
            self.assertEqual(len(results['ccc_did']), 36)
            self.assertEqual(results['sampleId'], sampleName)
            self.assertEqual(results['propToCopy'], 'NotNull')


    def test_copy_properties(self):
        print("testing copying properties...")

        sampleName = 'sample2'
        self.registerSample(sampleName)

        with tempfile.NamedTemporaryFile(mode='r', delete=False) as temp:
            mockCCC_DID = 'mockCCC_DID'
            results = subprocess.check_output(['python', self.getScriptPath(), 'publish_resource',
                  '--token=' + self.generateAuthToken(),
                  '--filePath=' + temp.name,
                  '--siteId=' + self.getSiteId(),
                  '--user=' + self.getUser(),
                  '--projectCode=' + self.getProject(),
                  '--workflowId=workflow1',
                  '--mimeType=mime_type',
                  '--property=sample_id:' + sampleName,
                  '--property=ccc_did:' + mockCCC_DID,
                  '--property=siteId:thisShouldNotCopy',
                  '--property=projectCode:thisShouldNotCopy',
                  '-m'
            ]).decode("utf-8")

            results = json.loads(results)

            #these should match the projectCode argument, not the duplicate assigned through property=projectCode
            self.assertEqual(results['projectCode'], self.getProject())
            self.assertEqual(results['siteId'], self.getSiteId())

            self.assertEqual(results['ccc_did'], mockCCC_DID)

            #we expect these to be inherited from the sample
            self.assertEqual(results['sampleId'], sampleName)
            self.assertEqual(results['propToCopy'], 'NotNull')


    def registerSample(self, sampleId):
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as tsv:
            writer = csv.writer(tsv, delimiter='\t', lineterminator='\n')
            writer.writerow(['sampleId', 'propToCopy'])
            writer.writerow([sampleId, 'NotNull'])

        results = subprocess.call(['python', self.getScriptPath(), 'publish_batch',
              '--token=' + self.generateAuthToken(),
              '--tsv=' + tsv.name,
              '--siteId=' + self.getSiteId(),
              '--user=' + self.getUser(),
              '--projectCode=' + self.getProject(),
              '--domain=sample'
              ])

        print('published sample: ' + sampleId)


    def generateAuthToken(self):
        #not yet implemented
        return 'notYetImplemented'

    def getScriptPath(self):
        return os.path.join(dir_path, './bin/ccc_import')

    def getSiteId(self):
        return 'testSite'

    def getProject(self):
        return 'testProject'

    def getUser(self):
        return 'me'

if __name__ == '__main__':
    unittest.main()
