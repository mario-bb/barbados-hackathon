# third party
import json
import pandas as pd
from dash import dcc, Input, Output
import dash_mantine_components as dmc

# project
from app import app
from .functions.graphs import math_scores_box_plot

# Load student data from multiple files
def load_student_data():
    files = {
        2022: "data/Sample_Data_BSSEE_results_2022.csv",
        2023: "data/Sample_Data_BSSEE_results_2023.csv",
        2024: "data/Sample_Data_BSSEE_results_2024.csv",
    }

    # Load each file into a dictionary
    dataframes = {year: pd.read_csv(file) for year, file in files.items()}

    # Add the year column to each dataframe
    for year, df in dataframes.items():
        df["examYear"] = year

    # Combine all years into one dataframe
    all_years_df = pd.concat(dataframes.values(), ignore_index=True)

    return all_years_df

# Load school parish data
def load_school_parish_data():
    school_parish_df = pd.read_csv("data/barbados_schools_parishes.csv")
    return school_parish_df

# Load all data
df = load_student_data()
school_parish_df = load_school_parish_data()

# Merge student data with school parish data using Primary School
df = df.merge(school_parish_df, left_on="primaryschool", right_on="School Name", how="left")

# Extract available filter options
available_years = sorted(df["examYear"].unique().tolist())
available_years.insert(0, "All Years")

available_genders = sorted(df["sex"].dropna().unique().tolist())
available_genders.insert(0, "All Genders")

available_primary_schools = sorted(df["primaryschool"].dropna().unique().tolist())
available_primary_schools.insert(0, "All Primary Schools")

available_student_parishes = sorted(df["StudentParish"].dropna().unique().tolist())
available_student_parishes.insert(0, "All Student Parishes")

available_primary_school_parishes = sorted(df["Parish"].dropna().unique().tolist())  # Parish column from school dataset
available_primary_school_parishes.insert(0, "All Primary School Parishes")

dashboard_layout = [
    dmc.Grid(
        gutter=10,
        grow=True,
        children=[
            dmc.GridCol(
                dmc.Alert(
                    "The Barbados Secondary School Entrance Examination (BSSEE) Analysis Dashboard provides a comprehensive overview of student performance, school placements, and key insights into the annual examination process. Designed to help educators, policymakers, and stakeholders understand trends and outcomes, this interactive dashboard presents data-driven insights on scores, subject performance, school allocations, and demographic breakdowns. Explore historical trends, compare results across schools, and identify areas for improvement in student readiness and educational equity.",
                    title="Mathematics Score Analysis – Barbados Secondary School Entrance Examination (BSSEE)",
                ),
                span=12,
            ),
            dmc.GridCol(
                [
                    dcc.Dropdown(
                        options=[{"label": str(year), "value": year} for year in available_years],
                        value="All Years",
                        id="year-selector",
                        className="pr-5",
                    ),
                    dcc.Dropdown(
                        options=[{"label": str(gender), "value": gender} for gender in available_genders],
                        value="All Genders",
                        id="gender-selector",
                        className="pr-5",
                    ),
                    dcc.Dropdown(
                        options=[{"label": str(parish), "value": parish} for parish in available_student_parishes],
                        value="All Student Parishes",
                        id="student-parish-selector",
                        className="pr-5",
                    ),
                    dcc.Dropdown(
                        options=[{"label": str(primary_school_parish), "value": primary_school_parish} for primary_school_parish in available_primary_school_parishes],
                        value="All Primary School Parishes",
                        id="primary-school-parish-selector",
                        className="pr-5",
                    ),
                    dcc.Dropdown(
                        options=[{"label": str(primary_school), "value": primary_school} for primary_school in available_primary_schools],
                        value="All Primary Schools",
                        id="primary-school-selector",
                        className="pr-5",
                    ),
                    dcc.Graph(id="math-score-parish-boxplot", className="pr-5"),
                ],
                span=12,
            ),
            dmc.GridCol(
                dmc.Alert(
                    "This data shows...",
                    title="To-Do - A.I Analysis of Dataset will go here...",
                ),
                span=12,
            ),
        ],
    )
]

@app.callback(
    Output("math-score-parish-boxplot", "figure"),
    Input("year-selector", "value"),
    Input("gender-selector", "value"),
    Input("student-parish-selector", "value"),
    Input("primary-school-parish-selector", "value"),
    Input("primary-school-selector", "value"),
)
def update_parish_chart(selected_year, selected_gender, selected_student_parish, selected_primary_school_parish, selected_primary_school):
    filtered_df = df

    if selected_year != "All Years":
        filtered_df = filtered_df[filtered_df["examYear"] == int(selected_year)]
    
    if selected_gender != "All Genders":
        filtered_df = filtered_df[filtered_df["sex"] == selected_gender]

    if selected_student_parish != "All Student Parishes":
        filtered_df = filtered_df[filtered_df["StudentParish"] == selected_student_parish]

    if selected_primary_school_parish != "All Primary School Parishes":
        filtered_df = filtered_df[filtered_df["Parish"] == selected_primary_school_parish]

    if selected_primary_school != "All Primary Schools":
        filtered_df = filtered_df[filtered_df["primaryschool"] == selected_primary_school]

    fig = math_scores_box_plot(filtered_df)
    return fig
