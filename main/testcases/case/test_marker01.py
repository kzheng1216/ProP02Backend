import sys

import pytest as pytest


@pytest.mark.ui
@pytest.mark.api
def test_api01():
    assert 1 == 1


@pytest.mark.ui
def test_ui01():
    assert 1 == 1


