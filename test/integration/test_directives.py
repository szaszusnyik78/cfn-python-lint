"""
Copyright 2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
"""
from cfnlint import Template, Runner  # pylint: disable=E0401
from cfnlint.rules import RulesCollection
from cfnlint.core import DEFAULT_RULESDIR  # pylint: disable=E0401
import cfnlint.decode.cfn_yaml  # pylint: disable=E0401
from testlib.testcase import BaseTestCase


class TestDirectives(BaseTestCase):
    """Test Directives """

    def setUp(self):
        """ SetUp template object"""
        self.rules = RulesCollection(include_rules=['I'])
        rulesdirs = [DEFAULT_RULESDIR]
        for rulesdir in rulesdirs:
            self.rules.create_from_directory(rulesdir)

    def test_templates(self):
        """Test ignoring certain rules"""
        filename = 'test/fixtures/templates/bad/core/directives.yaml'
        failures = 5

        template = cfnlint.decode.cfn_yaml.load(filename)
        runner = Runner(self.rules, filename, template, ['us-east-1'])
        matches = []
        matches.extend(runner.transform())
        if not matches:
            matches.extend(runner.run())
        assert len(matches) == failures, 'Expected {} failures, got {} on {}'.format(
            failures, len(matches), filename)
