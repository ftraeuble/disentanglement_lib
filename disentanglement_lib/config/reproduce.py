# coding=utf-8
# Copyright 2018 The DisentanglementLib Authors.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Different studies that can be reproduced."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from disentanglement_lib.config.abstract_reasoning_study_v1.stage1 import sweep as abstract_reasoning_study_v1
from disentanglement_lib.config.fairness_study_v1 import sweep as fairness_study_v1
from disentanglement_lib.config.tests import sweep as tests
from disentanglement_lib.config.unsupervised_study_v1 import sweep as unsupervised_study_v1
from disentanglement_lib.config.correlated_factors_study import sweep as correlated_factors_study
from disentanglement_lib.config.correlated_factors_study_ws_od import sweep as correlated_factors_study_ws_od
from disentanglement_lib.config.correlated_factors_study_ws_id1 import sweep as correlated_factors_study_ws_id1
from disentanglement_lib.config.correlated_factors_study_ws_id2 import sweep as correlated_factors_study_ws_id2

STUDIES = {
    "unsupervised_study_v1": unsupervised_study_v1.UnsupervisedStudyV1(),
    "abstract_reasoning_study_v1":
        abstract_reasoning_study_v1.AbstractReasoningStudyV1(),
    "fairness_study_v1":
        fairness_study_v1.FairnessStudyV1(),
    "correlation_study":
        correlated_factors_study.CorrelatedFactorsStudy(),
    "correlation_study_ws_od":
        correlated_factors_study_ws_od.CorrelatedFactorsStudyWSOD(),
    "correlation_study_ws_id1":
        correlated_factors_study_ws_id1.CorrelatedFactorsStudyWSID1(),
    "correlation_study_ws_id2":
        correlated_factors_study_ws_id2.CorrelatedFactorsStudyWSID2(),
    "test": tests.TestStudy(),
}
