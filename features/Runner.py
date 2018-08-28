# Created By Rahul Ranjan on 24/06/2018.

import glob
from json2html import *
import sys
from behave import __main__ as runner_with_options
from shutil import rmtree
import os

if __name__ == '__main__':
    sys.stdout.flush()
    reporting_folder_name = 'allure-results'
    # reporting_folder_allure = 'allureReport'
    path = os.path.dirname(__file__)
    print("path", path)
    #
    # remove if any reporting folder exists
    if os.path.exists(reporting_folder_name):
        rmtree(reporting_folder_name)
    os.makedirs(reporting_folder_name)

    #
    # allure reporting related command line arguments
    reportingRelated = ' -f allure_behave.formatter:AllureFormatter -o ' + reporting_folder_name + '  '

    # run Behave + BDD + Python code
    tagList = '--tags=test_all'
    featureFilePath = path + "/couponsAPI"
    # feature file path
    # #featureFileFolderPath1 = " " \
    #                          ".." \
    #                          "../features/couponsAPI/"
    # features/Runner.py
    # #featureFileFolderPath2 = " " \
    #                          "../features/featureFiles2/"
    # #multipleFeatureFIlePath = featureFileFolderPath1 + " " + featureFileFolderPath2

    commonRunnerOptions = ' --no-capture --no-capture-stderr -f plain '
    fullRunnerOptions = featureFilePath + reportingRelated + commonRunnerOptions + tagList
    runner_with_options.main(fullRunnerOptions)

    # read resultant json file
    listOfJson = glob.glob(reporting_folder_name + "/*.json")
    finalJson = ''
    for cnt in range(0, len(listOfJson)):
        listOfJson[cnt] = ' {"' + "Scenario_" + str(cnt) + '"' + ' : ' + open(listOfJson[cnt], 'r').read() + '}'
        if cnt < (-1 + len(listOfJson)):
            listOfJson[cnt] = listOfJson[cnt] + ','
        finalJson = finalJson + listOfJson[cnt]
    finalJson = '[ ' + finalJson + ' ]'

    # convert json to html using simple utility and publish report
    html_content = json2html.convert(json=finalJson)
    html_report_file = open(reporting_folder_name + '/' + 'index.html', 'w')
    html_report_file.write(html_content)
    html_report_file.close()

    # convert json to html report in more graphical format.
    # os.system("allure generate --clean ./reporting_folder_json_html")
    # os.system("allure open")
