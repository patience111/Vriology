from survey import AnonymousSurvey
#define a question and make a survey.
question='What language did you first learn to speak?'
my_survey=AnonymousSurvey(question)
#show the question and store the answer to the question.
my_survey.show_question()
print("Enter 'a' at any time to quit.\n")
while True:
    response=input("Languge:")
    if response=='q':
        break
    my_survey.store_response(response)
#show the survey results.
print("\n Thank you to every who paticipate in the survey!")
my_survey.show_results()

