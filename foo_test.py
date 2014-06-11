#!/usr/bin/env python
#
# Copyright 2014 Steven Le (stevenle08@gmail.com)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Description."""

__author__ = 'stevenle08@gmail.com (Steven Le)'

import unittest
import foo


class FooTest(unittest.TestCase):

  def testAdd(self):
    self.assertEqual(3, foo.add(1, 2))
    self.assertEqual(1, foo.add(1, 2))


if __name__ == '__main__':
  unittest.main()
