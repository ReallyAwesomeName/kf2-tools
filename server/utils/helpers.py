#
# main.py
# Driver code for backend
#
# Author: Rin | Discord: Rin#0304
# https://github.com/ReallyAwesomeName/kf2-tools
#
# =========================================================================== #
#     This program provides tools to calculate things for Killing Floor 2     #
#     Copyright (C) 2023  Rin                                                 #
#                                                                             #
#     This file is part of kf2-tools                                          #
#                                                                             #
#     This program is free software: you can redistribute it and/or modify    #
#     it under the terms of the GNU General Public License as published by    #
#     the Free Software Foundation, either version 3 of the License, or       #
#     (at your option) any later version.                                     #
#                                                                             #
#     This program is distributed in the hope that it will be useful,         #
#     but WITHOUT ANY WARRANTY; without even the implied warranty of          #
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the           #
#     GNU General Public License for more details.                            #
#                                                                             #
#     You should have received a copy of the GNU General Public License       #
#     along with this program.  If not, see <https://www.gnu.org/licenses/>.  #
# =========================================================================== #

# helper functions for data retrieval and manipulation


import pandas as pd

# google sheets api
import google.auth
from google.auth.transport.requests import Request


def get_text_data(
    sheet_name, spreadsheet_id="1GDpg2mN1l_86U_RaDug0glFx8cZCuErwxZLiBKl9SyY"
):
    """get data from google sheet

    Args:
        spreadsheet_id (string): sheet id from url
        sheet_name (string): name of sheet (tab) to pull data from

    Returns:
        string: csv data from sheet
    """

    # google.auth.
    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
    response = requests.get(url)
    response.raise_for_status()
    return response.text


def get_data_value(text_data, column_name, row_number):
    """use pandas to parse data from sheet

    Args:
        text_data (string): csv data from sheet
        column_name (string): name of column to pull data from
        row_number (int): row number to pull data from
    Returns:
        data (string): data from row/column
    """

    retval = pd.read_csv(text_data, sep=",", header=None)

    return retval
