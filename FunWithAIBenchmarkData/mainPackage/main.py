# File Name : main.py
# Student Name: Uruz B, Shantele K, Nogaye G
# email:  bidiwaur@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date:  3/27/2025
# Course #/Section: IS 4010-001
# Semester/Year: Spring 2025
# Brief Description of the assignment: Created code for logoPackage and visualPackage to run the graph and picture

# Brief Description of what this module does.Added a chart and logo
# Citations: ChatGPT and Youtube

# Anything else that's relevant:

from readingLevelPackage.readingLevel import Reading_Level
from utilitiesPackage.utilities import *
from utilitiesPackage.CSV_Utilities import *
from PDFPackage.PDFUtilities import *
from logoPackage.logo import load_logo
from visualPackage.visual import load_data, preprocess_data, perform_kmeans_clustering, visualize_clusters


# Load the image
image = load_logo()

if image:
    # Display the image using the default image viewer
    image.show()


def main():
    filepath = 'C:dataPackage\MMLU\data\car_prices.csv'  # Ensure this points to the correct file path
    features = ['price', 'mileage']  # Replace with the actual feature names in your dataset
   
    df = load_data(filepath)  # Load the data
    scaled_data = preprocess_data(df, features)  # Preprocess the data
    clusters, _ = perform_kmeans_clustering(scaled_data, n_clusters=3)  # Perform KMeans clustering
    df['Cluster'] = clusters  # Add the cluster labels to the DataFrame
   
    visualize_clusters(df, features, clusters)  # Visualize the clusters

if __name__ == "__main__":
    main()


    CSV_Processor = MMLU_CSV_Processor("dataPackage/MMLU/data/", ["management_test.csv"])
    questions = CSV_Processor.read_data()
    print(len(questions), "questions read")

 
    myPDF = PDFUtilities()
    myPDF.create_question_PDF("Management Test", "MMLU", questions)
   
    print("The first question:")
    print(questions[0])
   
    text = convert_dictionaries_to_string(questions, ["prompt", "possible answers"])
    #print("\ntext from dictionaries:", text[0:500])

    #0. Append all the prompts into a big string - See utilities.convert_dictionaries_to_string()
   
   
    #1. Perform reading level analysis on the big string and print the results to the console.
    Reading_Level.compute_readability_indices("MMLU", text)

    #2. Process the big string to find the longest word


    #3. Process the big string to find the most prevalent word
   

    #4. Use the VS debugger: set a breakpoint somewhere to pause the project when a prompt containing the word "PEST" is read from the original CSV file
   

    #5. Perform some data visualization on the text. Research Data Vis libraries and apply one.
     

    #6a. Write all the questions and possible answers (without the correct answer) to a text file. Use a CSV format and create a unique identifier field for each question.
    #6b. Write the question identifier (see 6a, above) and the correct answer to another text file. Use a CSV format.
    questions_written = write_questions_to_text_files("MMLU", questions)
    print(questions_written, "questions written to the file.")
   
    """
    # This code is commented out
    #Reading_Level.test01()

    text = "This is a sentence that we can use to test the reading level computations. "
    reading_level_indices = Reading_Level.compute_readability_indices("Dummy Benchmark", text)
    for key in reading_level_indices.keys():
        print(key, ":", reading_level_indices[key])
           
    # A test with text at a higher reading level
    text = "Birds, employing a combination of aerodynamic principles and specialized anatomical adaptations, achieve flight through the generation of lift, which counteracts the force of gravity."
    reading_level_indices = Reading_Level.compute_readability_indices("Dummy Benchmark", text)
    for key in reading_level_indices.keys():
        print(key, ":", reading_level_indices[key])
    """


