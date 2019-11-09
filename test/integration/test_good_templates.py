"""
Copyright 2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
"""
from cfnlint import Template, Runner  # pylint: disable=E0401
from cfnlint.rules import RulesCollection
from cfnlint.core import DEFAULT_RULESDIR  # pylint: disable=E0401
import cfnlint.decode.cfn_yaml  # pylint: disable=E0401
from testlib.testcase import BaseTestCase


class TestQuickStartTemplates(BaseTestCase):
    """Test QuickStart Templates Parsing """

    def setUp(self):
        """ SetUp template object"""
        self.rules = RulesCollection(include_rules=['I'])
        rulesdirs = [DEFAULT_RULESDIR]
        for rulesdir in rulesdirs:
            self.rules.create_from_directory(rulesdir)

        self.filenames = {
            'generic': {
                "filename": 'test/fixtures/templates/good/generic.yaml',
                "failures": 0
            },
            'minimal': {
                "filename": 'test/fixtures/templates/good/minimal.yaml',
                "failures": 0
            },
            'transform': {
                "filename": 'test/fixtures/templates/good/transform.yaml',
                "failures": 0
            },
            'transform_bad': {
                "filename": 'test/fixtures/templates/bad/transform_serverless_template.yaml',
                "failures": 3
            },
            'conditions': {
                "filename": 'test/fixtures/templates/good/conditions.yaml',
                "failures": 0
            },
            'resources_codepipeline': {
                'filename': 'test/fixtures/templates/good/resources_codepipeline.yaml',
                'failures': 0
            },
            'transform_serverless_api': {
                'filename': 'test/fixtures/templates/good/transform_serverless_api.yaml',
                'failures': 0
            },
            'transform_serverless_function': {
                'filename': 'test/fixtures/templates/good/transform_serverless_function.yaml',
                'failures': 0
            },
            'transform_serverless_globals': {
                'filename': 'test/fixtures/templates/good/transform_serverless_globals.yaml',
                'failures': 1
            },
            'transform_list': {
                'filename': 'test/fixtures/templates/good/transform/list_transform.yaml',
                'failures': 0
            },
            'transform_list_many': {
                'filename': 'test/fixtures/templates/good/transform/list_transform_many.yaml',
                'failures': 0
            },
            'transform_list_not_sam': {
                'filename': 'test/fixtures/templates/good/transform/list_transform_not_sam.yaml',
                'failures': 0
            }
        }

    def test_templates(self):
        """Test Successful JSON Parsing"""
        for _, values in self.filenames.items():
            filename = values.get('filename')
            failures = values.get('failures')
            template = cfnlint.decode.cfn_yaml.load(filename)

            runner = Runner(self.rules, filename, template, ['us-east-1'])
            matches = []
            matches.extend(runner.transform())
            if not matches:
                matches.extend(runner.run())
            assert len(matches) == failures, 'Expected {} failures, got {} on {}'.format(
                failures, len(matches), filename)
