# Student Grade Prediction

## Overview
The **Student Grade Prediction** project uses machine learning techniques to predict students' academic performance based on various features such as study hours, attendance, and previous grades. This project provides an end-to-end solution from data preprocessing to model deployment.

## Table of Contents
1. [Project Description](#project-description)
2. [Installation](#installation)
3. [Dependencies](#dependencies)
4. [Usage](#usage)
5. [Dataset](#dataset)

## Project Description
This project predicts student grades using machine learning models, specifically trained on datasets containing information about student behavior and academic history. The objective is to provide an automated system that can forecast grades, helping educators identify students in need of additional support.


## Installation

### Clone the Repository
First, clone the repository to your local machine:

```bash
git clone https://github.com/OrestBahlai/student_grade_prediction.git
```

## Dependencies

### Install Dependencies
Navigate into the project directory and install the required dependencies:
```bash
cd student_grade_prediction
pip install -r requirements.txt
```
### MacOS:
To ensure proper functionality of XGB Regressor, install libomp using Homebrew:
```bash
brew install libomp
```
### Linux (Ubuntu/Debian):
On Linux, make sure to install libomp using the following:
```bash
sudo apt-get install libomp-dev
```
## Usage

* Run the Server: Start the server by running the following command in your terminal:
```bash
python server/server.py
```
* Access the Application: Once the server is running, open the `index.html` file in your browser. You can do this either through the console or directly in your working environment.

## Dataset

Dataset - Student Performance Data Set (https://www.kaggle.com/datasets/larsen0966/student-performance-data-set).