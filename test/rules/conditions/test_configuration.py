"""
Copyright 2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
"""
from cfnlint.rules.conditions.Configuration import Configuration  # pylint: disable=E0401
from .. import BaseRuleTestCase


class TestMappingConfiguration(BaseRuleTestCase):
    """Test template mapping configurations"""
    def setUp(self):
        """Setup"""
        super(TestMappingConfiguration, self).setUp()
        self.collection.register(Configuration())

    def test_file_positive(self):
        """Test Positive"""
        self.helper_file_positive()

    def test_file_negative(self):
        """Test failure"""
        self.helper_file_negative('test/fixtures/templates/bad/conditions.yaml', 2)
