#!/usr/bin/python3
"""
    The MIT License (MIT)

    Copyright (c) 2023 pkjmesra

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.

"""
import pytest 
import pandas as pd
from  pkscreener.classes.PortfolioXRay import * 

def test_summariseAllStrategies_returns_dataframe():
    result = summariseAllStrategies(testing=True)
    assert isinstance(result, pd.DataFrame)


@pytest.mark.parametrize('reportName', ['PKScreener_B_12_1_Insights_DateSorted.html'])
def test_bestStrategiesFromSummaryForReport_returns_dataframe(reportName):
    df = bestStrategiesFromSummaryForReport(reportName)
    assert isinstance(df, pd.DataFrame) 


@pytest.mark.parametrize('df_CCIAbove200, expected_CCIAbove200', [
    (pd.DataFrame({'CCI': [100, 150, 200, 250]}), pd.DataFrame({'CCI': [250]})),
    (pd.DataFrame({'CCI': [100, 150, 200, 250, 300]}), pd.DataFrame({'CCI': [250, 300]})),
    (pd.DataFrame({'CCI': [100, 150, 200]}), pd.DataFrame({'CCI':[]}).astype(int)),
    (pd.DataFrame({'CCI': []}), pd.DataFrame({'CCI':[]}))
])
def test_filterCCIAbove200(df_CCIAbove200, expected_CCIAbove200):
    result = filterCCIAbove200(df_CCIAbove200)
    pd.testing.assert_frame_equal(result.reset_index(drop=True), expected_CCIAbove200,check_dtype=False)

@pytest.mark.parametrize('df_CCI100To200, expected_CCI100To200', [
    (pd.DataFrame({'CCI': [100, 120, 150, 250]}), pd.DataFrame({'CCI': [120,150]})),
    (pd.DataFrame({'CCI': [100, 120, 150, 200, 300]}), pd.DataFrame({'CCI': [120,150, 200]})),
    (pd.DataFrame({'CCI': [100, 201]}), pd.DataFrame({'CCI':[]}).astype(int)),
    (pd.DataFrame({'CCI': []}), pd.DataFrame({'CCI':[]}))
])
def test_filterCCI100To200(df_CCI100To200, expected_CCI100To200):
    result = filterCCI100To200(df_CCI100To200)
    pd.testing.assert_frame_equal(result.reset_index(drop=True), expected_CCI100To200,check_dtype=False)

@pytest.mark.parametrize('df_CCI0To100, expected_CCI0To100', [
    (pd.DataFrame({'CCI': [0, 20, 50, 150]}), pd.DataFrame({'CCI': [0,20,50]})),
    (pd.DataFrame({'CCI': [0, 20, 50, 100, 200]}), pd.DataFrame({'CCI': [0,20,50,100]})),
    (pd.DataFrame({'CCI': [101, 201]}), pd.DataFrame({'CCI':[]}).astype(int)),
    (pd.DataFrame({'CCI': []}), pd.DataFrame({'CCI':[]}))
])
def test_filterCCIoTo100(df_CCI0To100, expected_CCI0To100):
    result = filterCCI0To100(df_CCI0To100)
    pd.testing.assert_frame_equal(result.reset_index(drop=True), expected_CCI0To100,check_dtype=False)

@pytest.mark.parametrize('df_CCIBelow0, expected_CCIBelow0', [
    (pd.DataFrame({'CCI': [-100, -90, -50, 0]}), pd.DataFrame({'CCI': [-90,-50]})),
    (pd.DataFrame({'CCI': [-99, -1, 0, -100, 50, 100, 200]}), pd.DataFrame({'CCI': [-99,-1]})),
    (pd.DataFrame({'CCI': [101, 201]}), pd.DataFrame({'CCI':[]}).astype(int)),
    (pd.DataFrame({'CCI': []}), pd.DataFrame({'CCI':[]}))
])
def test_filterCCIBelow0(df_CCIBelow0, expected_CCIBelow0):
    result = filterCCIBelow0(df_CCIBelow0)
    pd.testing.assert_frame_equal(result.reset_index(drop=True), expected_CCIBelow0,check_dtype=False)

@pytest.mark.parametrize('df_CCIBelowMinus100, expected_CCIBelowMinus100', [
    (pd.DataFrame({'CCI': [-100, -190, -50, 0]}), pd.DataFrame({'CCI': [-100,-190]})),
    (pd.DataFrame({'CCI': [-490, -100, 0, -90, 50, 100, 200]}), pd.DataFrame({'CCI': [-490,-100]})),
    (pd.DataFrame({'CCI': [101, 201]}), pd.DataFrame({'CCI':[]}).astype(int)),
    (pd.DataFrame({'CCI': []}), pd.DataFrame({'CCI':[]}))
])
def test_filterCCIBElowMinus100(df_CCIBelowMinus100, expected_CCIBelowMinus100):
    result = filterCCIBelowMinus100(df_CCIBelowMinus100)
    pd.testing.assert_frame_equal(result.reset_index(drop=True), expected_CCIBelowMinus100,check_dtype=False)
