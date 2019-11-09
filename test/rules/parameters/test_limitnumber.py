"""
Copyright 2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
"""
from cfnlint.rules.parameters.LimitNumber import LimitNumber  # pylint: disable=E0401
from .. import BaseRuleTestCase


class TestParameterLimitNumber(BaseRuleTestCase):
    """Test parameters limit number"""
    def setUp(self):
        """Setup"""
        super(TestParameterLimitNumber, self).setUp()
        self.collection.register(LimitNumber())

    def test_file_positive(self):
        """Test Positive"""
        self.helper_file_positive()

    def test_file_negative(self):
        """Test failure"""
        self.helper_file_negative('test/fixtures/templates/bad/limit_numbers.yaml', 1)
