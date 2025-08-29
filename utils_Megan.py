"""
File: utils_Megan.py

Purpose: Reusable header/tagline module for analytics projects.

Description:
A short, first-week module to demonstrate key skills:
- declare basic variables (bool, int, str, list)
- compose a reusable f-string "tagline" (a formatted-string header block)
- expose a function named get_tagline() that can be imported into other modules
- run this file as a script via main() using the if __name__ == '__main__' pattern

Author: Megan Chastain



TOD
"""

#####################################
# Import Modules
#####################################

# For a summary list of key modules that come pre-packaged with Python,
# see the notes in the requirements.txt file (included in all projects).

# Import modules from the Python Standard library
import statistics

# Additional external packages must be listed in requirements.txt or pyproject.toml
# and installed in the active .venv

# Import external packages
import loguru  # Easy logging
import pyttsx3  # type: ignore # Text-to-speech engine

#####################################
# Configure Simple Logger (better than print statements)
#####################################

logger = loguru.logger
logger.add(
    "project.log",
    level="INFO",
    rotation="100 KB",
    backtrace=False,
    diagnose=False,
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {name}:{line} | {message}",
)
logger.info("Logger loaded.")

#####################################
# Declare Global Variables
#####################################

# ----------------------------------
# Define Boolean variables (True/False)
# ----------------------------------
is_accepting_clients: bool = True
offers_remote_workshops: bool = True
is_hiring: bool = False


# ----------------------------------
# Define Integer variables
# ----------------------------------
current_year: int = 2025
year_started: int = 2020
number_of_employees: int = 25


# ----------------------------------
# Define String variables
# ----------------------------------
author: str = "Megan Chastain"  
organization: str = "Spondiferous Analytics"  
motto: str = "Embrace the Unplanned."  
location: str = "Columbia, Missouri"


# ----------------------------------
# Define List variables
# ----------------------------------
# example list of strings
services: list[str] = ["Data Analysis", "Machine Learning", "Business Intelligence"]

# example list of floating point numbers
satisfaction_scores: list[float] = [4.8, 4.6, 4.9, 5.0, 4.7]
office_locations: list[str] = ["Salem, Maine", "Beloit, Wisconsin", "Seattle, Washington"]



# ----------------------------------
# Use built-in Python operators (such as - + * /)
# and built-in Python functions (such as min, max, len, upper, lower, etc.)
# ----------------------------------
years_active: int = current_year - year_started
min_score: float = min(satisfaction_scores)
max_score: float = max(satisfaction_scores)
count_of_services: int = len(services)
count_of_scores: int = len(satisfaction_scores)
count_of_locations: int = len(office_locations)



# ----------------------------------
# Use the built-in statistics module functions (such as mean, stdev, etc.)
# ----------------------------------
mean_score: float = statistics.mean(satisfaction_scores)
stdev_score: float = statistics.stdev(satisfaction_scores)

# ----------------------------------
# Compose a reusable formatted string (f-string) using triple quotes
# ----------------------------------
byline: str = f"""
**********************************************************
{organization} — Project Header
**********************************************************
Author:                     {author}
Motto:                      {motto}
Years Active:               {years_active}
Location:                  {location}
Office Locations:           {office_locations} (Total: {count_of_locations})
Number of Employees:        {number_of_employees}
Accepting New Clients?:     {is_accepting_clients}
Remote Workshops?:          {offers_remote_workshops}
Services:                   {services}
Client Satisfaction Scores: {satisfaction_scores}
Minimum Satisfaction Score: {min_score}
Maximum Satisfaction Score: {max_score}
Mean Satisfaction Score:    {mean_score:.2f}
     Standard Deviation:    {stdev_score:.2f}
**********************************************************
"""

# TODO: Modify the byline f-string to display your new variables as well. Use curly braces {} to embed each variable.

#####################################
# Define Global Functions
#####################################


def get_byline() -> str:
    """
    Return the reusable byline/tagline string.
    """
    return byline


def read_byline_aloud() -> None:
    """
    Use text-to-speech to read the byline aloud.
    """
    engine = pyttsx3.init()
    if engine is not None:
        engine.say(str(get_byline()))
        engine.runAndWait()


#####################################
# Define Function main() function for this module.
#####################################


def main() -> None:
    """
    Use this main() function to test this module when
    running it as a script.
    """

    loguru.logger.info("STARTING main()..")
    loguru.logger.info("Byline:\n" + get_byline())

    try:
        
        # read_byline_aloud()
        pass
    except KeyboardInterrupt:
        logger.info("Speech interrupted by user (Ctrl+C).")
    except Exception as ex:
        logger.warning(f"Text-to-speech skipped: {ex}")

    loguru.logger.info("This module is organized like all Python modules.")
    loguru.logger.info("We write professional Python from the start.")
    loguru.logger.info("END main()...")


#####################################
# Conditional Execution
#####################################

# If we are running this file as a script then call main()
# and verify our code works as expected.

if __name__ == "__main__":
    main()


""" 
    More about functions:

    - A function is a block of code that performs a task.
    - We wrote a reusable function that returns our byline.
    - Functions let us write code once and reuse it.
    - Defining good functions is a valuable skill.
    - Know what you want to name it, what information it needs to do its job,
      and what it should return (if anything).
    - Our byline function doesn't need any additional information passed in,
        so there's nothing inside the parentheses.
    - AI tools can help us write functions, but WE must specify what we want.
    - Recommended: 
        - Use `type hints` to indicate what kind of value (if any) the function returns.
        - Use `type hints` to indicate what type of information each parameter should be.
        - Use a docstring at the start to describe what the function does.
    - Everything after the colon must be indented consistently (usually 4 spaces)
"""