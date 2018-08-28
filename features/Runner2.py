#Created By Rahul Ranjan on 24/06/2018.
import sys
from behave import __main__ as runner_with_options
import os

if __name__ == '__main__':
    sys.stdout.flush()
    path = os.path.dirname(__file__)
    print("path", path)

    # run Behave + BDD + Python code
    tagList = '--tags=test_all'
    featureFilePath = path + "/couponsAPI"
    # feature file path
    # #featureFileFolderPath1 = " " \
    #                          ".." \
    #                          "../features/couponsAPI/"
    #features/Runner.py
    # #featureFileFolderPath2 = " " \
    #                          "../features/featureFiles2/"
    # #multipleFeatureFIlePath = featureFileFolderPath1 + " " + featureFileFolderPath2

    commonRunnerOptions = ' --no-capture --no-capture-stderr -f plain '
    fullRunnerOptions = featureFilePath  + commonRunnerOptions +tagList
    runner_with_options.main(fullRunnerOptions)
